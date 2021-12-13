from common import lines

import itertools
import re


lines = iter(lines)

points = {
    tuple(map(int, line.split(',')))
    for line in itertools.takewhile(bool, lines)
}


pattern = re.compile('(x|y)=(\d+)')
for i, fold in enumerate(lines):
    about, at = pattern.search(fold).groups()
    at = int(at)

    # this section really bugs me
    if about == 'x':
        points = {
            (at - abs(x - at), y)
            for x, y in points
        }
    else:
        points = {
            (x, at - abs(y - at))
            for x, y in points
        }

    if i == 0:
        print('Part 1:', len(points))

print('Part 2:')
for y in range(6):
    for x in range(40):
        print('@' if (x, y) in points else ' ', end='')
    print()
