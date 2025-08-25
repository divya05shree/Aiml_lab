import os
import collections
import time

# --- ANSI Escape Codes for Colors ---
# These codes may not work on all terminals.
class Colors:
    PLAYER = '\033[34m'  # Blue
    START = '\033[32m'   # Green
    END = '\033[31m'     # Red
    POINT = '\033[33m'   # Yellow
    OBSTACLE = '\033[90m' # Grey
    RESET = '\033[0m'    # Reset to default

color_map = {
    'P': Colors.PLAYER,
    'S': Colors.START,
    'E': Colors.END,
    '1': Colors.POINT,
    '#': Colors.OBSTACLE,
    ' ': Colors.RESET,
}

# --- Game Board Definition ---
# This is a sample grid. You can change this to any valid grid layout.
grid = [
    ['#', 'S', ' ', ' ', '#'],
    [' ', '1', ' ', '#', '#'],
    ['#', ' ', ' ', '1', 'E'],
    ['#', '#', ' ', ' ', '#'],
]

# --- Game State Variables ---
player_pos = None
start_pos = None
for r_idx, row in enumerate(grid):
    for c_idx, cell in enumerate(row):
        if cell == 'S':
            player_pos = [r_idx, c_idx]
            start_pos = (r_idx, c_idx)
            break
    if player_pos:
        break

score = 0
game_over = False

# --- Helper Functions ---
def clear_screen():
    """Clears the terminal screen for a cleaner display."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(current_grid, player_position):
    """Prints the current state of the grid with colors."""
    clear_screen()
    display_grid = [row[:] for row in current_grid]
    if player_position:
        r, c = player_position
        display_grid[r][c] = 'P'

    # Determine the maximum width of each column for proper spacing
    max_len = max(len(str(cell)) for row in display_grid for cell in row) + 2

    # Print the top border
    print("+" + "---+" * len(display_grid[0]))

    for row in display_grid:
        line_parts = []
        for cell in row:
            color = color_map.get(cell, Colors.RESET)
            line_parts.append(f" {color}{cell}{Colors.RESET} ")
        print("|" + "|".join(line_parts) + "|")
        print("+" + "---+" * len(display_grid[0]))
        
    print(f"\nScore: {score}")

def find_path_bfs(start_node, end_node, current_grid):
    """
    Finds a path from a start_node to an end_node using Breadth-First Search (BFS).
    Returns the path as a list of coordinates or None if no path exists.
    """
    rows, cols = len(current_grid), len(current_grid[0])
    queue = collections.deque([(start_node, [start_node])])
    visited = {start_node}

    while queue:
        (r, c), path = queue.popleft()
        
        if (r, c) == end_node:
            return path
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc

            if 0 <= new_r < rows and 0 <= new_c < cols and \
               current_grid[new_r][new_c] != '#' and \
               (new_r, new_c) not in visited:
                
                visited.add((new_r, new_c))
                new_path = path + [(new_r, new_c)]
                queue.append(((new_r, new_c), new_path))
    return None

# --- Main Automated Game Loop ---
print("Welcome to the Automated Grid Game!")
print("The AI will now navigate from 'S' to 'E' and collect all points.")

# Find all point locations and the end
points = []
end_pos = None
for r_idx, row in enumerate(grid):
    for c_idx, cell in enumerate(row):
        if cell == '1':
            points.append((r_idx, c_idx))
        elif cell == 'E':
            end_pos = (r_idx, c_idx)

# Compute the full path
full_path = []
current_location = start_pos

# Find the shortest path to each point, then to the end.
for point_pos in points:
    path_to_point = find_path_bfs(current_location, point_pos, grid)
    if path_to_point:
        full_path.extend(path_to_point[1:])
        current_location = point_pos

if end_pos:
    path_to_end = find_path_bfs(current_location, end_pos, grid)
    if path_to_end:
        full_path.extend(path_to_end[1:])

if not full_path:
    print("Could not find a valid path to the end or to all points. Game Over.")
    game_over = True

# Main loop to follow the computed path
while not game_over:
    print_grid(grid, player_pos)
    
    if not full_path:
        game_over = True
        continue
    
    # Get the next step from the computed path
    next_pos = full_path.pop(0)
    new_row, new_col = next_pos

    current_row, current_col = player_pos
    cell_content = grid[new_row][new_col]
    
    # Update the grid
    if grid[current_row][current_col] != 'S':
        grid[current_row][current_col] = ' '
    
    # Update player position
    player_pos[0] = new_row
    player_pos[1] = new_col

    # Check for game-state changes
    if cell_content == '1':
        score += 1
        print("Point collected! Score +1.")
    
    if player_pos == list(end_pos):
        game_over = True
        print_grid(grid, player_pos)
        print("\nCongratulations! The AI reached the end!")
        print(f"Final score is: {score}")
        print("Game Over.")
        break
    
    # Add a short delay to make the movement visible
    time.sleep(1)
