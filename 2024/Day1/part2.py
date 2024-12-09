def read_and_parse_input(filename):
    """Read the input file and parse into two lists of numbers."""
    with open(filename, 'r') as file:
        data = file.read().strip()
        
    # Parse each line into pairs of numbers and unzip into two lists
    pairs = [list(map(int, line.split())) for line in data.splitlines()]
    left_list = [pair[0] for pair in pairs]
    right_list = [pair[1] for pair in pairs]
    
    return left_list, right_list

def calculate_distance(left, right):
    """
    Calculate total distance between sorted lists by pairing smallest with smallest
    and summing the absolute differences.
    """
    # Sort both lists
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    
    # Calculate absolute difference between each pair
    return sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))

def calculate_similarity_score(left, right):
    """
    Calculate similarity score by multiplying each number in left list 
    by its frequency in right list.
    """
    return sum(right.count(num) * num for num in left)

def main():
    filename = r"D:\Coding\ADVENT-OF-CODE\2024\Day1\input.txt"
    
    # Read and parse input
    left_list, right_list = read_and_parse_input(filename)
    
    # Part 1: Calculate distance between lists
    distance = calculate_distance(left_list, right_list)
    print(f"Part 1 - Total distance between lists: {distance}")
    
    # Part 2: Calculate similarity score
    similarity = calculate_similarity_score(left_list, right_list)
    print(f"Part 2 - Similarity score: {similarity}")

if __name__ == "__main__":
    main()