from common import lines

import re
from collections import Counter


coordinates = Counter()
diagonals = Counter()

for line in lines:
    x1, y1, x2, y2 = map(int, re.findall('\d+', line))

    target = diagonals if x1 != x2 and y1 != y2 else coordinates

    length = max(abs(x2 - x1), abs(y2 - y1))
    dx, dy = (x2 - x1) // length, (y2 - y1) // length

    for i in range(length + 1):
        target[x1 + dx * i, y1 + dy * i] += 1


points = sum(p >= 2 for p in coordinates.values())
print('Part 1:', points)

coordinates += diagonals
points = sum(p >= 2 for p in coordinates.values())
print('Part 2:', points)
