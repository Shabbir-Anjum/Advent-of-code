import re
from collections import defaultdict

data = open(r"D:\Coding\ADVENT-OF-CODE\2024\Day8\input.txt").read().strip()
l = data.split("\n")

dict_symbols = defaultdict(list)
for r in range(len(l)):
    for c in range(len(l[0])):
        if l[r][c] != '.':
            dict_symbols[l[r][c]].append((r, c))
# part 1
antinodes = set()
for a in dict_symbols.values():
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j: continue
            r1, c1 = a[i]
            r2, c2 = a[j]
            antinodes.add((2 * r1 - r2, 2 * c1 - c2))
            antinodes.add((2 * r2 - r1, 2 * c2 - c1))

print(len([0 for r, c in antinodes if 0<=r<len(l) and 0<=c<len(l[0])]))

# part 2
antinodes = set()
for a in dict_symbols.values():
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j: continue
            r1, c1 = a[i]
            r2, c2 = a[j]
            dr = r2 - r1
            dc = c2 - c1
            r, c = r1, c1
            while 0 <=r<len(l) and 0<=c<len(l[0]):
                antinodes.add((r, c))
                r += dr
                c += dc
print(len([0 for r, c in antinodes if 0<=r<len(l) and 0<=c<len(l[0])]))