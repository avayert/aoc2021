from common import raw

import collections


ages = collections.deque([0] * 9)

for age in raw.split(','):
    ages[int(age)] += 1

for i in range(80):
    ages.rotate(-1)  # that's a rotate!
    ages[6] += ages[8]

print('Part 1:', sum(ages))

for i in range(256 - 80):
    ages.rotate(-1)
    ages[6] += ages[8]

print('Part 2:', sum(ages))
