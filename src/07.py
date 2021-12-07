from common import raw

import math
import statistics

positions = [int(pos) for pos in raw.split(',')]

middle = statistics.median(positions)
fuel = sum(abs(pos - middle) for pos in positions)

print('Part 1:', int(fuel))

def triangular(n):
    return n * (n + 1) / 2

middle = statistics.mean(positions)

low = sum(triangular(abs(pos - math.floor(middle))) for pos in positions)
high = sum(triangular(abs(pos - math.ceil(middle))) for pos in positions)

print('Part 2:', int(min(low, high)))
