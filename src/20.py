from common import lines

import itertools


algorithm, _, *picture = lines

size = range(len(picture))

algorithm = [val == '#' for val in algorithm]
picture = {
    (x, y): val == '#'
    for y, row in enumerate(picture)
    for x, val in enumerate(row)
}

default = 0

def pixel_for(x, y):
    index = sum(
        picture.get((x + dx, y + dy), default) << shift
        for shift, (dy, dx) in enumerate(itertools.product((1, 0, -1), repeat=2))
    )
    return algorithm[index]

def step():
    global size, default

    new = {}

    size = range(size.start - 1, size.stop + 1)

    for x, y in itertools.product(size, repeat=2):
        new[x, y] = pixel_for(x, y)

    default = not default

    picture.clear()
    picture.update(new)

for _ in range(2):
    step()

print('Part 1:', sum(picture.values()))

for _ in range(48):
    step()

print('Part 1:', sum(picture.values()))

