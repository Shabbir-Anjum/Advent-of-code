def read_grid(filename):
    """Read the input file into a 2D grid."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def find_pattern(grid, pattern):
    """Find all occurrences of a pattern in all 8 directions."""
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Define all 8 directions: right, down-right, down, down-left, left, up-left, up, up-right
    directions = [
        (0, 1),   # right
        (1, 1),   # down-right
        (1, 0),   # down
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, -1), # up-left
        (-1, 0),  # up
        (-1, 1)   # up-right
    ]
    
    def is_valid_pattern(row, col, dr, dc):
        """Check if pattern exists starting at (row, col) in direction (dr, dc)."""
        if not (0 <= row < rows and 0 <= col < cols):
            return False
            
        for i, char in enumerate(pattern):
            r = row + i * dr
            c = col + i * dc
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if grid[r][c] != char:
                return False
        return True

    # Check each starting position
    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                if is_valid_pattern(row, col, dr, dc):
                    count += 1
    
    return count

def process_file(filename):
    """Process the input file and return the count of 'XMAS' occurrences."""
    grid = read_grid(filename)
    return find_pattern(grid, "XMAS")

# Main execution
if __name__ == "__main__":
    filename = r"D:\Coding\ADVENT-OF-CODE\2024\Day4\input.txt"
    result = process_file(filename)
    print(f"'XMAS' appears {result} times in the word search.")