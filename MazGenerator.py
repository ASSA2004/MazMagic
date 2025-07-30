import random

def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]

    def carve(x, y):
        dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 1 <= nx < rows-1 and 1 <= ny < cols-1:
                if maze[nx][ny] == 1:
                    maze[nx - dx//2][ny - dy//2] = 0  # Break wall between
                    maze[nx][ny] = 0
                    carve(nx, ny)

    # Start at (1,1)
    maze[1][1] = 0
    carve(1, 1)

    # Entry and Exit
    maze[1][0] = 0  # Entry
    maze[rows-2][cols-1] = 0  # Exit
    return maze
