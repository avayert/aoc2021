from common import raw

import collections


template, tail = raw.split('\n\n')
lines = tail.splitlines()

insertions = {}
for line in lines:
    (a, b), c = line.split(' -> ')
    insertions[a + b] = [a + c, c + b]

pairs = collections.Counter(a + b for a, b in zip(template, template[1:]))

def step():
    c = collections.Counter()
    for pair, n in pairs.items():
        for p in insertions[pair]:
            c[p] += n
    return c

def count_chars():
    c = collections.Counter()
    for (a, b), value in pairs.items():
        c[a] += value
        c[b] += value
    return max(c.values()) // 2 - min(c.values()) // 2 + 1

for i in range(10):
    pairs = step()

print('Part 1:', count_chars())

for i in range(30):
    pairs = step()

print('Part 1:', count_chars())
