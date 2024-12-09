def is_safe_report(levels):
    """
    Check if a report is safe based on the rules:
    1. All numbers must be either increasing or decreasing
    2. Adjacent numbers must differ by 1-3
    """
    if len(levels) < 2:
        return True
    
    # Check the first difference to determine if we should be increasing or decreasing
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    # If first difference is positive, all should be positive (increasing)
    # If first difference is negative, all should be negative (decreasing)
    expected_sign = 1 if differences[0] > 0 else -1
    
    for diff in differences:
        # Check if direction changes or stays same
        if diff == 0 or (diff > 0) != (expected_sign > 0):
            return False
        # Check if difference is between 1 and 3 (inclusive)
        if abs(diff) > 3:
            return False
    
    return True

def is_safe_with_dampener(levels):
    """
    Check if a report is safe, considering the Problem Dampener which can remove one level.
    Returns True if either:
    1. The report is already safe
    2. Removing exactly one level makes the report safe
    """
    # First check if it's already safe without removing any level
    if is_safe_report(levels):
        return True
    
    # Try removing each level one at a time
    for i in range(len(levels)):
        # Create new list without the current level
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe_report(dampened_levels):
            return True
            
    return False

def count_safe_reports_with_dampener(filename):
    """Read the input file and count safe reports considering the Problem Dampener."""
    safe_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            # Convert line to list of integers, skip empty lines
            line = line.strip()
            if not line:
                continue
            levels = [int(x) for x in line.split()]
            if is_safe_with_dampener(levels):
                safe_count += 1
    
    return safe_count

# Run the analysis
filename = r"D:\Coding\ADVENT-OF-CODE\2024\Day2\input.txt"
result = count_safe_reports_with_dampener(filename)
print(f"Number of safe reports with Problem Dampener: {result}")