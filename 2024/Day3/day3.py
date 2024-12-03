import re

def scan_memory(text):
    """
    Scan corrupted memory text for valid mul instructions and sum their results.
    
    Args:
        text (str): The corrupted memory text to scan
        
    Returns:
        int: Sum of all valid multiplication results
    """
    # Regular expression to match valid mul instructions
    # Matches mul(X,Y) where X and Y are 1-3 digit numbers
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all matches in the text
    matches = re.finditer(pattern, text)
    
    total = 0
    calculations = []
    
    # Process each match
    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        result = x * y
        calculations.append(f"{x} * {y} = {result}")
        total += result
    
    return total, calculations

def process_file(filename):
    """
    Read and process the input file.
    
    Args:
        filename (str): Path to the input file
        
    Returns:
        int: Sum of all multiplication results
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        total, calculations = scan_memory(content)
        
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


filename = r"D:\Coding\ADVENT-OF-CODE\2024\Day3\input.txt" 

result = process_file(filename)

if result is not None:
    print(f"\nFinal answer: {result}")