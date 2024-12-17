class Input:
    def __init__(self, data):
        self.data = data.strip()
        self.lines = self.data.split('\n')
        self.current_line = 0
    
    def is_empty(self):
        return self.current_line >= len(self.lines)
    
    def read_line(self):
        if self.is_empty():
            return None
        line = self.lines[self.current_line]
        self.current_line += 1
        return line

class Output:
    def __init__(self):
        self.results = []
    
    def print_line(self, value):
        self.results.append(str(value))
        print(value)
    
    def flush(self):
        pass

def parse_input_line(line, pattern):
    # Simple pattern matching for the input format
    if "Button A:" in pattern:
        parts = line.split(',')
        x = int(parts[0].split('+')[1])
        y = int(parts[1].split('+')[1])
        return x, y
    elif "Button B:" in pattern:
        parts = line.split(',')
        x = int(parts[0].split('+')[1])
        y = int(parts[1].split('+')[1])
        return x, y
    elif "Prize:" in pattern:
        parts = line.split(',')
        x = int(parts[0].split('=')[1])
        y = int(parts[1].split('=')[1])
        return x, y
    return None

def solve(input_obj, output_obj, test_case, pre_calc):
    data = []
    
    # Parse input
    while not input_obj.is_empty():
        line1 = input_obj.read_line()
        line2 = input_obj.read_line()
        line3 = input_obj.read_line()
        if input_obj.current_line < len(input_obj.lines):
            input_obj.read_line()  # Skip empty line
            
        x0, y0 = parse_input_line(line1, "Button A: X+@, Y+@")
        x1, y1 = parse_input_line(line2, "Button B: X+@, Y+@")
        x, y = parse_input_line(line3, "Prize: X=@, Y=@")
        data.append((x0, y0, x1, y1, x, y))
    
    # Part 1
    ans = 0
    for x0, y0, x1, y1, x, y in data:
        cur = float('inf')
        for a in range(101):  # 0 to 100 inclusive
            for b in range(101):
                xx = x0 * a + x1 * b
                yy = y0 * a + y1 * b
                if xx == x and yy == y:
                    cur = min(cur, 3 * a + b)
        if cur != float('inf'):
            ans += cur
    output_obj.print_line(ans)
    
    # Part 2
    ans = 0
    LARGE_NUMBER = 10000000000000
    for x0, y0, x1, y1, x, y in data:
        x += LARGE_NUMBER
        y += LARGE_NUMBER
        d = x0 * y1 - x1 * y0
        if d == 0:  # Avoid division by zero
            continue
            
        dy = x * y0 - y * x0
        if dy % d != 0:
            continue
            
        b = -dy // d
        dx = x * y1 - x1 * y
        if dx % d != 0:
            continue
            
        a = dx // d
        if a < 0 or b < 0:
            continue
            
        ans += 3 * a + b
    output_obj.print_line(ans)

def run_tests():
    # Example usage
    test_input = open(r"D:\Coding\ADVENT-OF-CODE\2024\Day13\input.txt").read().strip()
    
    input_obj = Input(test_input)
    output_obj = Output()
    solve(input_obj, output_obj, 1, None)
    return output_obj.results

if __name__ == "__main__":
    results = run_tests()
    print("Test Results:", results)