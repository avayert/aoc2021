from common import lines


# terrible
class Octopus:
    def __init__(self, value):
        self.value = int(value)

    def increment(self):
        self.value += 1
        return self.value

    def reset(self):
        if 10 <= self.value:
            self.value = 0
        return self.value == 0

    def __eq__(self, other):
        return self.value == other


# I could have re-used the grid thing from a previous day but this was more funny
grid = {
    complex(x, y): Octopus(item)
    for x, row in enumerate(lines)
    for y, item in enumerate(row)
}

neighbours = [
    -1-1j, 0-1j, 1-1j,
    -1+0j,       1+0j,
    -1+1j, 0+1j, 1+1j,
]

def step():
    remaining = [k for k, v in grid.items() if 10 <= v.increment()]

    while remaining:
        pos = remaining.pop()

        for offset in neighbours:
            neighbour = pos + offset

            if neighbour not in grid:
                continue

            grid[neighbour].increment()

            if grid[neighbour] == 10:
                remaining.append(neighbour)

    return sum(o.reset() for o in grid.values())

flashes = sum(step() for _ in range(100))
print('Part 1:', flashes)

# works for my data good enough
part2 = 100
while True:
    part2 += 1
    if step() == 100:
        break

print('Part 2:', part2)
