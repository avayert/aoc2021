from common import lines

import collections
import heapq
import itertools


class Grid(list):
    def neighbours(self, x, y):
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(self) and 0 <= ny < len(self[0]):
                yield nx, ny

    def __getitem__(self, item):
        if not isinstance(item, tuple):
            return super().__getitem__(item)

        x, y = item
        return self[y][x]

grid = Grid([[int(c) for c in line] for line in lines])

low_points = []

width, height = len(grid[0]), len(grid)

for x, y in itertools.product(range(width), range(height)):
    h = grid[x, y]

    if all(h < grid[n] for n in grid.neighbours(x, y)):
        low_points.append((x, y))

print('Part 1:', sum(grid[x, y] + 1 for x, y in low_points))

goes_to = {}

def dfs_basin(x, y):
    for neighbour in grid.neighbours(x, y):
        if grid[neighbour] < grid[x, y]:
            break
    else:
        return (x, y)

    ret = dfs_basin(*neighbour)
    goes_to[x, y] = ret
    return ret


end_points = collections.Counter()

for x, y in itertools.product(range(width), range(height)):
    if grid[x, y] == 9:
        continue

    try:
        end_points[goes_to[x, y]] += 1
    except KeyError:
        end_points[dfs_basin(x, y)] += 1

a, b, c = [count for _, count in end_points.most_common(3)]
print('Part 2:', a * b * c)
