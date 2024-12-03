import re

def scan_memory_with_conditionals(text):
    """
    Scan corrupted memory text for valid mul instructions, respecting do() and don't() conditionals.
    
    Args:
        text (str): The corrupted memory text to scan
        
    Returns:
        int: Sum of all valid and enabled multiplication results
    """
    # Regular expressions for instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Get all instructions with their positions
    instructions = []
    
    # Find all mul instructions
    for match in re.finditer(mul_pattern, text):
        instructions.append({
            'type': 'mul',
            'pos': match.start(),
            'x': int(match.group(1)),
            'y': int(match.group(2))
        })
    
    # Find all do() instructions
    for match in re.finditer(do_pattern, text):
        instructions.append({
            'type': 'do',
            'pos': match.start()
        })
    
    # Find all don't() instructions
    for match in re.finditer(dont_pattern, text):
        instructions.append({
            'type': 'dont',
            'pos': match.start()
        })
    
    # Sort instructions by position
    instructions.sort(key=lambda x: x['pos'])
    
    # Process instructions
    total = 0
    enabled = True  # Initially enabled
    calculations = []
    
    for instruction in instructions:
        if instruction['type'] == 'do':
            enabled = True
        elif instruction['type'] == 'dont':
            enabled = False
        elif instruction['type'] == 'mul' and enabled:
            x = instruction['x']
            y = instruction['y']
            result = x * y
            calculations.append(f"{x} * {y} = {result} (enabled: {enabled})")
            total += result
        elif instruction['type'] == 'mul':
            x = instruction['x']
            y = instruction['y']
            calculations.append(f"{x} * {y} = {x * y} (enabled: {enabled}, not counted)")
    
    return total, calculations

def process_file(filename):
    """
    Read and process the input file.
    
    Args:
        filename (str): Path to the input file
        
    Returns:
        int: Sum of all enabled multiplication results
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        total, calculations = scan_memory_with_conditionals(content)
        
        # Print each calculation for verification
        print("Individual calculations:")
        for calc in calculations:
            print(calc)
            
        print(f"\nTotal sum: {total}")
        return total
    except FileNotFoundError:
        print(f"Error: Could not find file {filename}")
        return None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None

filename = r"D:\Coding\ADVENT-OF-CODE\2024\Day3\input2.txt" 

result = process_file(filename)

if result is not None:
    print(f"\nFinal answer: {result}")