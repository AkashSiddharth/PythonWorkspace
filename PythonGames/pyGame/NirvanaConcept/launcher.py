import pygame
import sys
from physics import PhysicsEngine

# Initialize Pygame
pygame.init()

# Setup Display Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Side-Scroller Prototype - Greybox Phase 1")
clock = pygame.time.Clock()
FPS = 60

# World Constants & Physics Parameters
GRAVITY = 1200.0       # Pixels per second squared
MOVE_SPEED = 300.0     # Pixels per second
JUMP_FORCE = -550.0    # Initial upward velocity impulse

# Player Entity Data
player_rect = pygame.Rect(100, 100, 32, 48)  # x, y, width, height
player_velocity = [0.0, 0.0]                  # [vx, vy]
is_grounded = False

# Static Map Geometry (Platforms in world space)
platforms = [
    pygame.Rect(0, 500, 1600, 100),    # Main Ground
    pygame.Rect(300, 400, 200, 20),    # Low Platform
    pygame.Rect(600, 320, 180, 20),    # Mid Platform
    pygame.Rect(900, 240, 220, 20),    # High Platform
]

# Camera Tracking Offset
camera_x = 0

# --- MAIN LOOP ---
running = True
while running:
    # 1. Calculate Delta-Time (seconds per frame)
    dt = clock.tick(FPS) / 1000.0

    # 2. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if (event.key == pygame.K_SPACE or event.key == pygame.K_w) and is_grounded:
                player_velocity[1] = JUMP_FORCE

    # 3. Input Polling (Horizontal Movement)
    keys = pygame.key.get_pressed()
    player_velocity[0] = 0.0
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_velocity[0] = -MOVE_SPEED
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_velocity[0] = MOVE_SPEED

    # 4. Physics Pipeline Execution
    player_velocity[1] = PhysicsEngine.apply_gravity(player_velocity[1], GRAVITY, dt)
    collision_info = PhysicsEngine.move_and_collide(player_rect, player_velocity, platforms, dt)
    is_grounded = collision_info["on_ground"]

    # 5. Camera Tracking (Smoothly center viewport on player)
    target_camera_x = player_rect.centerx - (SCREEN_WIDTH // 2)
    camera_x += (target_camera_x - camera_x) * 0.1  # Smooth lerp interpolation

    # 6. Render Pipeline
    screen.fill((30, 30, 35))  # Dark gray backdrop

    # Render Platforms with Camera Offset
    for platform in platforms:
        rendered_platform = platform.move(-int(camera_x), 0)
        pygame.draw.rect(screen, (70, 80, 95), rendered_platform)

    # Render Player with Camera Offset
    rendered_player = player_rect.move(-int(camera_x), 0)
    pygame.draw.rect(screen, (50, 205, 50), rendered_player)  # Green player box

    # Swap Buffers
    pygame.display.flip()

pygame.quit()
sys.exit()