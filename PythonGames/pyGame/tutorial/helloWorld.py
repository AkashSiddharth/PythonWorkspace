import pygame

# Initialize Game
pygame.init()

WIDTH = 800
HEIGHT = 400

# Create Window
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello World")

# Game Loop
running = True
while running:
  # Get all the queued events
  for event in pygame.event.get():
    print(event)
    if event.type == pygame.QUIT:
      running = False

# Clear the memory
pygame.quit()