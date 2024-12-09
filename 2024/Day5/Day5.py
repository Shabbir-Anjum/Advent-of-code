from collections import defaultdict, deque

def parse_input(filename):
    """Parse the input file into rules and updates."""
    with open(filename, 'r') as f:
        content = f.read().strip().split('\n\n')
    rules = defaultdict(set)
    for line in content[0].split('\n'):
        if not line:
            continue
        before, after = map(int, line.strip().split('|'))
        rules[after].add(before) 
    updates = []
    for line in content[1].split('\n'):
        if not line:
            continue
        update = list(map(int, line.strip().split(',')))
        updates.append(update)
    return rules, updates
def is_valid_order(pages, rules):
    """Check if the pages are in valid order according to rules."""
    page_set = set(pages)
    
    for i, page in enumerate(pages):
        if page in rules:
            required_predecessors = rules[page] & page_set
            predecessors_in_sequence = set(pages[:i])
            if not required_predecessors.issubset(predecessors_in_sequence):
                return False
    return True
def get_middle_number(arr):
    """Get the middle number from an array."""
    return arr[len(arr) // 2]
def topological_sort(pages, rules):
    """Sort pages according to the given rules using Kahn's algorithm."""
    page_set = set(pages)
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    for page in pages:
        if page in rules:
            deps = rules[page] & page_set
            for dep in deps:
                graph[dep].add(page)
                in_degree[page] += 1

    queue = deque([page for page in pages if in_degree[page] == 0])
    result = []
    
    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

def process_file(filename):
    """Process both parts of the puzzle."""
    rules, updates = parse_input(filename)
    
    # Part 1: Sum of middle numbers from valid updates
    part1_total = 0
    invalid_updates = []
    
    for update in updates:
        if is_valid_order(update, rules):
            part1_total += get_middle_number(update)
        else:
            invalid_updates.append(update)
    
    # Part 2: Sum of middle numbers from corrected invalid updates
    part2_total = 0
    for update in invalid_updates:
        corrected_order = topological_sort(update, rules)
        part2_total += get_middle_number(corrected_order)
    
    return part1_total, part2_total

if __name__ == "__main__":
    filename = r"D:\Coding\ADVENT-OF-CODE\2024\Day5\input.txt"
    part1_result, part2_result = process_file(filename)
    print(f"Part 1 - Sum of middle numbers from valid updates: {part1_result}")
    print(f"Part 2 - Sum of middle numbers from corrected invalid updates: {part2_result}")