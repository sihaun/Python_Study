def print_grid(grid):
    for row in grid:
        print(' '.join(['X' if cell else '.' for cell in row]))
    print()

def get_neighbors(grid, x, y):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            count += grid[nx][ny]
    return count

def next_generation(grid):
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            neighbors = get_neighbors(grid, x, y)
            if grid[x][y] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_grid[x][y] = 1
                else:
                    new_grid[x][y] = 0
            else:
                if neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid

def main():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    
    generations = 5
    for _ in range(generations):
        print_grid(grid)
        grid = next_generation(grid)

if __name__ == "__main__":
    main()
