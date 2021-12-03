from common import lines

from collections import Counter
from functools import partial
from itertools import count
import statistics

size = len(lines[0])

def invert_binary(n, size=size):
    return ~n & (2 ** size - 1)

gamma = ''

columns = list(zip(*lines))
for col in columns:
    majority = 0.5 < statistics.mean(map(int, col))
    gamma += str(int(majority))

gamma = int(gamma, 2)

print('Part 1:', gamma * invert_binary(gamma))


def prune(items, predicate):
    items = items.copy()

    for i in count(0):
        digit = predicate(item[i] for item in items)
        items = [item for item in items if item[i] == digit]

        if len(items) == 1:
            return items[0]

def more(it, default):
    c = Counter(it)
    c.update('01')

    (big, x), (small, y) = c.most_common()

    if x == y:
        return str(default)

    return [small, big][default]

a, b = [int(prune(lines, partial(more, default=default)), 2) for default in [1, 0]]

print('Part 2:', a * b)
