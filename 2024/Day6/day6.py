def read_map(filename):
    """Read the map from file and return as a 2D list along with guard's starting position and direction."""
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]
    
    # Find guard's starting position and direction
    start_pos = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                start_pos = (i, j, 'up')
                grid[i][j] = '.'  # Clear the guard's position
                return grid, start_pos
    return grid, None

def get_next_position(pos, direction):
    """Get the next position based on current position and direction."""
    i, j = pos
    if direction == 'up':
        return (i-1, j)
    elif direction == 'right':
        return (i, j+1)
    elif direction == 'down':
        return (i+1, j)
    else:  # left
        return (i, j-1)

def turn_right(direction):
    """Return the new direction after turning right."""
    directions = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    return directions[direction]

def is_valid_position(pos, grid):
    """Check if the position is within the grid."""
    i, j = pos
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def process_file(filename):
    """Process the input file and return the number of distinct positions visited."""
    grid, start_pos = read_map(filename)
    if not start_pos:
        return 0
    
    visited = set()
    current_i, current_j, direction = start_pos
    visited.add((current_i, current_j))
    
    while True:
        # Get next position based on current direction
        next_i, next_j = get_next_position((current_i, current_j), direction)
        
        # Check if guard has left the area
        if not is_valid_position((next_i, next_j), grid):
            break
            
        # Check if there's an obstacle ahead
        if grid[next_i][next_j] == '#':
            # Turn right
            direction = turn_right(direction)
        else:
            # Move forward
            current_i, current_j = next_i, next_j
            visited.add((current_i, current_j))
    
    return len(visited)

# Example usage
filename = r"D:\Coding\ADVENT-OF-CODE\2024\Day6\input.txt"
result = process_file(filename)
print(f"The guard will visit {result} distinct positions.")