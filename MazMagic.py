import pygame
import pygame_gui
import sys
from MazGenerator import generate_maze

# --- Constants ---
TILE_SIZE = 20
COLS = 41  # Must be odd for maze algorithm
ROWS = 31
WIDTH, HEIGHT = COLS * TILE_SIZE, ROWS * TILE_SIZE + 60  # Extra for GUI

# Colors
BLACK = (0, 0, 0)
GREY = (70, 70, 70)
BLUE = (30, 144, 255)
GREEN = (0, 255, 100)
WHITE = (255, 255, 255)

# --- Initialization ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game with GUI")
clock = pygame.time.Clock()
FPS = 60

# --- GUI Manager ---
ui_manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Buttons
start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((20, HEIGHT - 50), (100, 40)),
    text='Start',
    manager=ui_manager
)
restart_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((140, HEIGHT - 50), (100, 40)),
    text='Restart',
    manager=ui_manager
)
exit_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((260, HEIGHT - 50), (100, 40)),
    text='Exit',
    manager=ui_manager
)

# Maze State Variables
maze = []
walls = []
player_rect = None
exit_rect = None
game_active = False
font = pygame.font.SysFont("segoeui", 28)

# --- Maze Functions ---
def build_maze():
    global maze, walls, player_rect, exit_rect
    maze = generate_maze(ROWS, COLS)
    walls = []

    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == 1:
                walls.append(pygame.Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Entry and Exit placement
    entry = (1, 1)
    exit = (COLS - 2, ROWS - 2)
    maze[entry[1]][entry[0]] = 0
    maze[exit[1]][exit[0]] = 0

    player_rect = pygame.Rect(entry[0]*TILE_SIZE+4, entry[1]*TILE_SIZE+4, TILE_SIZE-8, TILE_SIZE-8)
    exit_rect = pygame.Rect(exit[0]*TILE_SIZE, exit[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)

# --- Game Logic ---
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

def draw_maze():
    for wall in walls:
        pygame.draw.rect(screen, GREY, wall)
    pygame.draw.rect(screen, GREEN, exit_rect)
    pygame.draw.rect(screen, BLUE, player_rect)

# --- Initial Maze ---
build_maze()

# --- Game Loop ---
running = True
while running:
    time_delta = clock.tick(FPS) / 1000.0
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --- Button Events ---
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    game_active = True
                    build_maze()

                elif event.ui_element == restart_button:
                    game_active = True
                    build_maze()

                elif event.ui_element == exit_button:
                    pygame.quit()
                    sys.exit()

        ui_manager.process_events(event)

    keys = pygame.key.get_pressed()
    if game_active:
        dx = dy = 0
        if keys[pygame.K_w]: dy = -3
        if keys[pygame.K_s]: dy = 3
        if keys[pygame.K_a]: dx = -3
        if keys[pygame.K_d]: dx = 3
        move_player(dx, dy)

    # --- Game Drawing ---
    if game_active:
        draw_maze()
        if player_rect.colliderect(exit_rect):
            win_text = font.render("🎉 You Win!", True, WHITE)
            screen.blit(win_text, (WIDTH//2 - 60, HEIGHT//2 - 30))
            game_active = False

    # --- GUI Update ---
    ui_manager.update(time_delta)
    ui_manager.draw_ui(screen)
    pygame.display.flip()
