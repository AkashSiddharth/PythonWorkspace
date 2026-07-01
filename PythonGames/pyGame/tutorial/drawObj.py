import pygame

# initialize pygame
pygame.init()

# Define display 
WIDTH = 800
HEIGHT = 400

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Objects")

# Define RGB Tuples
BLACK = (0, 0 , 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

display_surface.fill(BLUE)

# Draw Objects
#Line(surface, color, starting_coordinates, end_coordinates, thickness)
pygame.draw.line(display_surface, RED, (10,20), (235,200), 5)
pygame.draw.line(display_surface, MAGENTA, (235,200), (500,5), 3)

# Circle(surface, color, center, radius, thickness0 .. for solid circle)
pygame.draw.circle(display_surface, GREEN, (WIDTH//2, HEIGHT//2), 100, 2)
pygame.draw.circle(display_surface, CYAN, ((WIDTH // 2) - 100 , HEIGHT // 2), 50, 4)

# Rectangle(surface, color, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface, YELLOW, (550, 10, 50, 5 ))
# Game Loop
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Update display
  pygame.display.update()

# Cleanup
pygame.quit()