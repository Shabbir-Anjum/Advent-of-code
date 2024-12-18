import heapq

def parse_input(file_path):
    with open(file_path, 'r') as file:
        return [tuple(map(int, line.strip().split(','))) for line in file]

def simulate_falling_bytes(file_path, grid_size=70, byte_count=1024):
    # Parse the input to get the list of corrupted coordinates
    falling_bytes = parse_input(file_path)

    # Create the grid and mark falling byte positions
    grid = [[False for _ in range(grid_size + 1)] for _ in range(grid_size + 1)]

    for i, (x, y) in enumerate(falling_bytes):
        if i >= byte_count:
            break
        grid[y][x] = True

    # Implement Dijkstra's Algorithm for shortest path
    def find_shortest_path():
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
        pq = [(0, 0, 0)]  # (distance, x, y)
        visited = set()

        while pq:
            dist, x, y = heapq.heappop(pq)

            if (x, y) == (grid_size, grid_size):
                return dist

            if (x, y) in visited:
                continue

            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= grid_size and 0 <= ny <= grid_size and not grid[ny][nx] and (nx, ny) not in visited:
                    heapq.heappush(pq, (dist + 1, nx, ny))

        return -1  # No path found

    return find_shortest_path()

# Example Usage
input_file_path = r"D:\Coding\ADVENT-OF-CODE\2024\Day18\input.txt"
result = simulate_falling_bytes(input_file_path)
print("Minimum steps needed to reach the exit:", result)