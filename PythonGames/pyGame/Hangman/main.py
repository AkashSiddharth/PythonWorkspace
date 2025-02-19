import pygame
import configparser
import os
import math
import json
import random

class Hangman:
  def __init__(self):
    self.run = True
    self.hangman_status = 0

    # Establish Paths
    self.script_directory = os.path.dirname(os.path.realpath(__file__))
    self.asset_path = os.path.join(self.script_directory,'assets')
    properties_file = os.path.join(self.script_directory, 'game.properties')

    # Game Variables
    self.CATEGORY, self.WORD = self.get_word()
    self.guessed = list()

    # Load the properties files
    self.config = configparser.ConfigParser()
    self.config.read(properties_file)

    # Load Properties
    self.width = int(self.config['DISPLAY']['SCREEN_WIDTH'])
    self.height = int(self.config['DISPLAY']['SCREEN_HEIGHT'])
    self.FPS = int(self.config['DISPLAY']['FPS'])
    self.PADDING = 15
    self.B_RADIUS = (self.width - self.PADDING * 16) // 26

    # Load assets
    self.images = list(pygame.image.load(os.path.join(self.asset_path,entry.name))
                          for entry in os.scandir(self.asset_path) 
                            if entry.is_file)

    # Establish Button Coordinates
    self.buttons = self.get_button_coord()

    # initilize the runner
    pygame.init()

    # Setup Display
    self.win = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption("Hangman")

    # for font in pygame.font.get_fonts():
    #   print(font)

    # Setup Game Font
    self.keyboard_font = pygame.font.SysFont(self.config['FONTS']['FONT'], 
                                              int(self.config['FONTS']['BUTTON_FONT_SIZE']), bold=True)
    self.word_font = pygame.font.SysFont(self.config['FONTS']['FONT'], 
                                              int(self.config['FONTS']['WORD_FONT_SIZE']), bold=True, italic = True)
    self.title_font = pygame.font.SysFont(self.config['FONTS']['TITLE_FONT'], 
                                              int(self.config['FONTS']['TITLE_FONT_SIZE']))

  def get_color(self, color: str) -> tuple:
    # get the color values from config
    return tuple(map(lambda x: int(x), self.config['COLORS'][color.upper()].split(',')))

  def get_button_coord(self) -> list:
    buttons = list()
    CHAR = 65
    start_X = (self.width - ((self.PADDING + self.B_RADIUS * 2) * 13)) / 2
    start_y = 4 * self.height // 5
    

    # Get center coordinates for each button
    for i in range(26):
      x = start_X + (self.PADDING * 2) + ((self.B_RADIUS * 2 + self.PADDING) * (i % 13))
      y = start_y + ((self.B_RADIUS * 2 + self.PADDING) * (i // 13))
      buttons.append([x, y, chr(CHAR + i), True])
    
    return buttons

  def get_word(self) -> tuple:
    category = ''
    word = ''
    with open(os.path.join(self.script_directory,'words.json'), 'r') as in_f:
      data = json.load(in_f)

      category = list(data)[random.randint(0, len(data.keys()) - 1)]
      word = data[category][random.randint(0, len(data[category]) - 1)]

      # print(category, word)
    return (category.upper(), word.upper())

  # DRAW
  def draw_word(self, color: tuple):
    display_word = ""
    # print(self.WORD)
    # print(self.guessed)
    for character in self.WORD:
      if character in self.guessed:
        display_word += character + " "
      else:
        display_word += "_ "
    
    text = self.word_font.render(display_word, 1, color)
    x_pos = self.width / 2 - text.get_width() / 2
    y_pos = self.height / 2
    self.win.blit(text, (x_pos, y_pos))
  
  def draw_button(self, pos: tuple, letter: str, b_color: tuple, f_color: tuple, hover = False):
    x_pos, y_pos = pos

    if not hover:
      pygame.draw.circle(self.win, b_color, pos, self.B_RADIUS, 3)

      # Render Text
      text = self.keyboard_font.render(letter, 1, b_color)
      self.win.blit(text, (x_pos - text.get_width() / 2, y_pos - text.get_height() / 2))
    else:
      pygame.draw.circle(self.win, b_color, pos, self.B_RADIUS)

      # Render Text
      text = self.keyboard_font.render(letter, 1, f_color)
      self.win.blit(text, (x_pos - text.get_width() / 2, y_pos - text.get_height() / 2))
  
  def draw(self):
    self.win.fill(self.get_color('white'))

    # Draw Title
    title_text = self.title_font.render('HANGMAN', 1, self.get_color('black'))
    self.win.blit(title_text, (self.width / 2 - title_text.get_width() / 2, 0))

    # Load Hangman image
    self.win.blit(self.images[self.hangman_status], (320, 70))

    # Draw Word Section
    self.draw_word(self.get_color('black'))

    # Draw Buttons
    for button in self.buttons:
      x, y, letter, enabled = button
      if enabled:
        self.draw_button((x, y), letter, self.get_color('black'), self.get_color('black'))

    pygame.display.update()

  def display_message(self, message: str):
    pygame.time.delay(1000)
    text = self.word_font.render(message, 1, self.get_color('black'), self.get_color('white'))

    x_pos = self.width / 2 - text.get_width() / 2
    y_pos = self.height / 2 - text.get_height() / 2

    pygame.draw.rect(self.win, self.get_color('white'), (0, y_pos, self.width, self.height / 2))
    self.win.blit(text, (x_pos, y_pos))
    pygame.display.update((0, y_pos, self.width, self.height / 2))
    pygame.time.delay(3000)

  # EVENTS
  def event_quit(self):
    self.run = False

  def event_mousemotion(self):
    m_x, m_y = pygame.mouse.get_pos()

    for button in self.buttons:
      x, y, letter, enabled = button

      if enabled:
        # Calculate distance between 2 coordinates
        distance = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
        if distance < self.B_RADIUS:
          # print("on Letter: " + letter)
          self.draw_button((x, y), letter, self.get_color('black'), self.get_color('white'), True)
          update_rect = pygame.Rect(x - self.B_RADIUS, y - self.B_RADIUS, self.B_RADIUS * 2, self.B_RADIUS *2)
          pygame.display.update(update_rect)

  def event_mouse_l_click(self):
    m_x, m_y = pygame.mouse.get_pos()
    print(m_x, m_y)

    for index, button in enumerate(self.buttons):
      x, y, letter, enabled = button

      if enabled:
        # Calculate distance between 2 coordinates
        distance = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
        if distance < self.B_RADIUS:
          print("Letter " + letter + " selected and to be disabled.")
          self.buttons[index][-1] = False
          self.guessed.append(letter)

          if letter not in self.WORD:
            self.hangman_status += 1

  def launch(self): 
    clock = pygame.time.Clock()

    # Setup game loop
    while self.run:
      clock.tick(self.FPS)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.event_quit()
        
        if event.type == pygame.MOUSEMOTION:
          self.event_mousemotion()

        if event.type == pygame.MOUSEBUTTONDOWN:
          self.event_mouse_l_click()
          # print(self.hangman_status)

      self.draw()

      # Check win/loss:
      won = True
      for letter in self.WORD:
        if letter not in self.guessed:
          won = False
          break

      if won:
        self.display_message("You Won !!!")
        break

      if self.hangman_status == 7:
        self.display_message("You Lose !!!")
        break

    pygame.quit()

if __name__ == "__main__":
  hngmn = Hangman()
  hngmn.launch()