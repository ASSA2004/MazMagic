import pygame
import sys
from MazGenerator import generate_maze

# Initialize
pygame.init()

# Settings
TILE_SIZE = 20
COLS = 40  # WIDTH // TILE_SIZE
ROWS = 30  # HEIGHT // TILE_SIZE
WIDTH, HEIGHT = COLS * TILE_SIZE, ROWS * TILE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game (Auto-Generated)")
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Maze Generation
maze = generate_maze(ROWS, COLS)
walls = []

def build_walls():
    w = []
    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == 1:
                rect = pygame.Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                w.append(rect)
    return w

walls = build_walls()

# Entry/Exit
start_x, start_y = TILE_SIZE * 1 + 4, TILE_SIZE * 1 + 4
end_tile = (COLS-1, ROWS-2)
exit_rect = pygame.Rect(end_tile[0]*TILE_SIZE, end_tile[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)

# Player
player_size = TILE_SIZE - 8
player_speed = 3
player_rect = pygame.Rect(start_x, start_y, player_size, player_size)

# Movement with wall collision
def move_player(dx, dy):
    player_rect.x += dx
    for wall in walls:
        if player_rect.colliderect(wall):
            player_rect.x -= dx
            break
    player_rect.y += dy
    for wall in walls:
        if player_rect.colliderect(wall):
            player_rect.y -= dy
            break

# Game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    keys = pygame.key.get_pressed()
    dx = dy = 0
    if keys[pygame.K_w]: dy = -player_speed
    if keys[pygame.K_s]: dy = player_speed
    if keys[pygame.K_a]: dx = -player_speed
    if keys[pygame.K_d]: dx = player_speed
    move_player(dx, dy)

    # Win condition
    if player_rect.colliderect(exit_rect):
        print("🎉 YOU WIN!")
        running = False

    # Draw
    screen.fill(BLACK)
    for wall in walls:
        pygame.draw.rect(screen, GREY, wall)
    pygame.draw.rect(screen, GREEN, exit_rect)
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
