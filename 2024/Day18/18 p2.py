import heapq

def parse_input(file_path):
    with open(file_path, 'r') as file:
        return [tuple(map(int, line.strip().split(','))) for line in file]

def simulate_falling_bytes(file_path, grid_size=70, byte_count=1024):
    # Parse the input to get the list of corrupted coordinates
    falling_bytes = parse_input(file_path)

    # Create the grid and mark falling byte positions
    grid = [[False for _ in range(grid_size + 1)] for _ in range(grid_size + 1)]

    # Implement Dijkstra's Algorithm for shortest path
    def find_shortest_path():
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
        pq = [(0, 0, 0)]  # (distance, x, y)
        visited = set()

        while pq:
            dist, x, y = heapq.heappop(pq)

            if (x, y) == (grid_size, grid_size):
                return True

            if (x, y) in visited:
                continue

            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= grid_size and 0 <= ny <= grid_size and not grid[ny][nx] and (nx, ny) not in visited:
                    heapq.heappush(pq, (dist + 1, nx, ny))

        return False  # No path found

    # Part 1: Simulate the first kilobyte (1024 bytes) falling
    for i, (x, y) in enumerate(falling_bytes):
        if i < byte_count:
            grid[y][x] = True

    part1_result = -1
    if find_shortest_path():
        part1_result = "Path found within first kilobyte of bytes."

    # Part 2: Find the first byte that blocks the path
    def find_blocking_byte():
        for i, (x, y) in enumerate(falling_bytes):
            grid[y][x] = True
            if not find_shortest_path():
                return x, y
        return None

    part2_result = find_blocking_byte()

    return part1_result, part2_result

# Example Usage
input_file_path = r"D:\Coding\ADVENT-OF-CODE\2024\Day18\input.txt"
part1_result, part2_result = simulate_falling_bytes(input_file_path)
print("Part 1 Result:", part1_result)
print("Part 2 Result:", ",".join(map(str, part2_result)) if part2_result else "No blocking byte found")
