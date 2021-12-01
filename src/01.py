from common import lines

lines = [int(line) for line in lines]

print('Part 1:', sum(a < b for a, b in zip(lines, lines[1:])))
print('Part 2:', sum(a < b for a, b in zip(lines, lines[3:])))
