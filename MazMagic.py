import pygame
import sys

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player settings
player_size = 40
player_speed = 5
player_rect = pygame.Rect(100, 100, player_size, player_size)  # x, y, width, height

# Game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Handle Keys ---
    keys = pygame.key.get_pressed()  # Get state of all keys
    if keys[pygame.K_w]:
        player_rect.y -= player_speed
    if keys[pygame.K_s]:
        player_rect.y += player_speed
    if keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_d]:
        player_rect.x += player_speed

    # --- Draw Everything ---
    screen.fill((0, 0, 0))  # Clear screen with black
    pygame.draw.rect(screen, BLUE, player_rect)  # Draw player as a blue square
    pygame.display.flip()

pygame.quit()
sys.exit()
