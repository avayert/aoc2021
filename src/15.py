from common import lines

import collections
from queue import PriorityQueue


def search(graph, start, end):
    seen = set()

    remaining = PriorityQueue()
    remaining.put((0, (0, 0)))

    while remaining:
        cost, vertex = remaining.get()
        if vertex in seen:
            continue

        seen.add(vertex)

        for neighbour, distance in graph[vertex]:
            if neighbour == end:
                return cost + distance

            if neighbour in seen:
                continue

            remaining.put((cost + distance, neighbour))


def make_graph(grid):
    graph = collections.defaultdict(list)

    for i, row in enumerate(grid):
        for j, n in enumerate(row):
            for a, b in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if 0 <= i + a < len(grid) and 0 <= j + b < len(row):
                    graph[i, j].append(((i + a, j + b), grid[i + a][j + b]))

    return graph

grid = [
    [int(c) for c in line]
    for line in lines
]

graph = make_graph(grid)
print('Part 1:', search(graph, min(graph), max(graph)))

grid = [
    [
        ((n + a + b - 1) % 9 + 1)
        for a in range(5)
        for n in row
    ]
    for b in range(5)
    for row in grid
]

graph = make_graph(grid)
print('Part 2:', search(graph, min(graph), max(graph)))
