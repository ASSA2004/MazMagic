import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (100, 100, 100)

# Maze layout (1 = wall, 0 = path)
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# Player
player_size = TILE_SIZE - 8
player_speed = 4
player_rect = pygame.Rect(TILE_SIZE + 4, TILE_SIZE + 4, player_size, player_size)

# Get wall rects
def get_walls():
    walls = []
    for row_index, row in enumerate(maze):
        for col_index, tile in enumerate(row):
            if tile == 1:
                wall_rect = pygame.Rect(col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                walls.append(wall_rect)
    return walls

# Collision check
def move_player(dx, dy, walls):
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

# Main game loop
running = True
while running:
    clock.tick(FPS)
    walls = get_walls()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_w]: dy = -player_speed
    if keys[pygame.K_s]: dy = player_speed
    if keys[pygame.K_a]: dx = -player_speed
    if keys[pygame.K_d]: dx = player_speed
    move_player(dx, dy, walls)

    # Draw
    screen.fill(BLACK)
    
    # Draw maze
    for wall in walls:
        pygame.draw.rect(screen, GREY, wall)

    # Draw player
    pygame.draw.rect(screen, BLUE, player_rect)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
