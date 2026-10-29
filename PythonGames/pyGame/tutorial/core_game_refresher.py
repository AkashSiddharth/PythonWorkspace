import pygame
import sys

# 1. Initialize Pygame subsystems
pygame.init()

# 2. Window & Clock Configuration
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Side-Scroller Prototype")
clock = pygame.time.Clock()
FPS = 60

running = True

while running:
    # 3. Delta-Time Calculation (Crucial for real-time physics)
    # clock.tick(FPS) returns milliseconds since the last frame. 
    # Convert to seconds (dt) so movement scales smoothly regardless of frame rate drops.
    dt = clock.tick(FPS) / 1000.0  

    # 4. Event Handling (Input Queue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 5. Continuous Input Polling (Great for smooth platformer movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        pass  # Handle player move left
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        pass  # Handle player move right

    # 6. State Update / Physics Pipeline (Multiplying by dt keeps it frame-rate independent)
    # player.update(dt)

    # 7. Render / Draw Pipeline
    screen.fill((30, 30, 30))  # Clear screen (dark gray background)
    
    # Draw your game objects here (rectangles, sprites, tiles)
    
    # 8. Frame Buffer Update
    pygame.display.flip()

pygame.quit()
sys.exit()