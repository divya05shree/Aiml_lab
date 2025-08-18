import os

# --- Game Board Definition ---
# This is a sample grid. You can change this to any valid grid layout.
# 'S' = Start, 'E' = End, '#' = Obstacle, '1' = Point
grid = [
    ['#', 'S', ' ', ' ', '#'],
    [' ', '1', ' ', '#', '#'],
    ['#', ' ', ' ', '1', 'E'],
    ['#', '#', ' ', ' ', '#'],
]

# --- Game State Variables ---
# Find the starting position 'S'
player_pos = None
for r_idx, row in enumerate(grid):
    for c_idx, cell in enumerate(row):
        if cell == 'S':
            player_pos = [r_idx, c_idx]
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
    """Prints the current state of the grid with the player."""
    clear_screen()
    display_grid = [row[:] for row in current_grid]  # Create a copy to modify for display
    r, c = player_position
    display_grid[r][c] = 'P'  # 'P' for Player

    for row in display_grid:
        print(' '.join(row))
    print(f"\nScore: {score}")

def get_move():
    """Gets and validates player input for movement."""
    valid_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    
    while True:
        move = input("Enter your move (up, down, left, right): ").lower().strip()
        if move in valid_moves:
            return valid_moves[move]
        print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")

# --- Main Game Loop ---
print("Welcome to the Grid Game!")
print("Navigate from 'S' to 'E'.")
print("Collect '1's for points. Avoid '#' obstacles.")
input("Press Enter to start...")

while not game_over:
    print_grid(grid, player_pos)
    
    dr, dc = get_move()
    
    current_row, current_col = player_pos
    new_row, new_col = current_row + dr, current_col + dc

    # Check for boundary conditions
    if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
        print("You can't move off the grid!")
        input("Press Enter to continue...")
        continue

    cell_content = grid[new_row][new_col]
    
    if cell_content == '#':
        print("That's an obstacle! You can't go there.")
        input("Press Enter to continue...")
    else:
        # Update the grid to mark the path taken
        grid[current_row][current_col] = ' '
        
        # Update player position
        player_pos[0] = new_row
        player_pos[1] = new_col

        # Check for game-state changes
        if cell_content == '1':
            score += 1
            print("You found a point! Score +1.")
        
        if cell_content == 'E':
            game_over = True
            grid[new_row][new_col] = ' ' # Clear the end cell for final display
            print_grid(grid, player_pos) # Final display
            print("\nCongratulations! You reached the end!")
            print(f"Your final score is: {score}")
            print("Game Over.")
            break
            
        input("Press Enter to continue...")