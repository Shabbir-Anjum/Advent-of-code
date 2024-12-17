import math, sys, re
from collections import defaultdict, Counter, deque

def read_lines(f):
    while True:
        line = f.readline()
        if not line:
            break
        line = line.rstrip('\n')  # Strip the newline character
        yield line

def emulate1(operator, operand, reg, out, ip):
    def get_combo(operand):
        if operand in range(4):
            return operand
        elif operand == 4:
            return reg['A']
        elif operand == 5:
            return reg['B']
        elif operand == 6:
            return reg['C']
        else:
            raise ValueError

    if operator == 0:  # adv
        reg['A'] = reg['A'] // (2 ** get_combo(operand))
    elif operator == 1:  # bxl
        reg['B'] ^= operand
    elif operator == 2:  # bst
        reg['B'] = get_combo(operand) % 8
    elif operator == 3:  # jnz
        if reg['A'] != 0:
            return operand
    elif operator == 4:  # bxc
        reg['B'] ^= reg['C']
    elif operator == 5:  # out
        out.append(get_combo(operand) % 8)
    elif operator == 6:  # bdv
        reg['B'] = reg['A'] // (2 ** get_combo(operand))
    elif operator == 7:  # cdv
        reg['C'] = reg['A'] // (2 ** get_combo(operand))
    else:
        raise ValueError
    return ip + 2

def read(lines):
    l = iter(lines)
    reg = {
        'A': int(re.fullmatch(r'Register A: (\d+)', next(l)).groups()[0]),
        'B': int(re.fullmatch(r'Register B: (\d+)', next(l)).groups()[0]),
        'C': int(re.fullmatch(r'Register C: (\d+)', next(l)).groups()[0]),
    }
    assert next(l) == ''
    program_text = re.fullmatch(r'Program: (.+)', next(l)).groups()[0]
    program = list(map(int, program_text.split(',')))
    return reg, program

def run1(reg, program):
    out = []
    ip = 0
    while True:
        try:
            operator, operand = program[ip], program[ip + 1]
        except IndexError:
            break
        ip = emulate1(operator, operand, reg, out, ip)
    return out

def part_1(lines):
    reg, program = read(lines)
    out = run1(reg, program)
    return ','.join(map(str, out))

def part_2(lines):
    reg, program = read(lines)

    def recu(program, reg, level, base):
        for i in range(8):
            r = reg.copy()
            r['A'] = base + 8 ** (level) * i
            if r['A'] < 0:
                continue
            out = run1(r, program)
            if out == program:
                return base + 8 ** (level) * i
            if len(out) == len(program) and out[level:] == program[level:]:
                ans = recu(program, reg, level - 1, base + 8 ** (level) * i)
                if ans is not None:
                    return ans
        return None

    s = recu(program, reg, len(program) - 1, 0)
    assert s is not None
    return s

def main():
    # Replace the file path with your desired input file location
    input_file_path = r"D:\Coding\ADVENT-OF-CODE\2024\Day17\input.txt"

    with open(input_file_path, 'r') as f:
        lines = list(read_lines(f))

    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))

if __name__ == '__main__':
    main()
