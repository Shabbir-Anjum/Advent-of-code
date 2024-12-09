def read_grid(filename):
    """Read the input file into a 2D grid."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def find_xmas_patterns(grid):
    """Find all X-shaped patterns where each diagonal is 'MAS' (forwards or backwards)."""
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def check_mas(r, c, dr, dc):
        """Check if 'MAS' exists starting at (r,c) in direction (dr,dc)."""
        if not (0 <= r < rows and 0 <= c < cols and 
                0 <= r + 2*dr < rows and 0 <= c + 2*dc < cols):
            return False
            
        pattern = grid[r][c] + grid[r+dr][c+dc] + grid[r+2*dr][c+2*dc]
        return pattern in ['MAS', 'SAM']
    
    # For each possible center point of the X
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            # Check all four possible combinations of forwards/backwards MAS
            # in the two diagonals
            
            # Check upper-left to lower-right diagonal
            for ulr_pattern in ['MAS', 'SAM']:
                r1, c1 = row-1, col-1  # Start of first diagonal
                
                # Check if first diagonal matches
                pattern1 = grid[r1][c1] + grid[row][col] + grid[row+1][col+1]
                if pattern1 != ulr_pattern:
                    continue
                
                # Check upper-right to lower-left diagonal
                for url_pattern in ['MAS', 'SAM']:
                    r2, c2 = row-1, col+1  # Start of second diagonal
                    
                    # Check if second diagonal matches
                    pattern2 = grid[r2][c2] + grid[row][col] + grid[row+1][col-1]
                    if pattern2 == url_pattern:
                        count += 1
    
    return count

def process_file(filename):
    """Process the input file and return the count of X-MAS patterns."""
    grid = read_grid(filename)
    return find_xmas_patterns(grid)

# Main execution
if __name__ == "__main__":
    filename = r"D:\Coding\ADVENT-OF-CODE\2024\Day4\input.txt"
    result = process_file(filename)
    print(f"Found {result} X-MAS patterns in the grid.")