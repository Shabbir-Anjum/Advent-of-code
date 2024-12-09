def evaluate_expression(numbers, operators):
    """Evaluate expression left-to-right with given numbers and operators."""
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        else:  # '*'
            result *= numbers[i + 1]
    return result

def generate_operator_combinations(num_positions):
    """Generate all possible combinations of + and * operators."""
    operators = ['+', '*']
    if num_positions == 0:
        return [[]]
    combinations = []
    for combo in generate_operator_combinations(num_positions - 1):
        for op in operators:
            combinations.append(combo + [op])
    return combinations

def solve_calibration(filename):
    total = 0
    
    with open(filename, 'r') as file:
        for line in file:
            # Parse each line
            test_value, numbers = line.strip().split(': ')
            test_value = int(test_value)
            numbers = [int(x) for x in numbers.split()]
            
            # Number of operator positions is one less than number count
            num_operators_needed = len(numbers) - 1
            
            # Generate all possible operator combinations
            operator_combinations = generate_operator_combinations(num_operators_needed)
            
            # Try each combination
            for operators in operator_combinations:
                if evaluate_expression(numbers, operators) == test_value:
                    total += test_value
                    break  # Found at least one solution, move to next equation
                    
    return total

# Run the solution
if __name__ == "__main__":
    filename = r"D:\Coding\ADVENT-OF-CODE\2024\Day7\input.txt"
    result = solve_calibration(filename)
    print(f"The total calibration result is: {result}")