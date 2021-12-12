from common import lines


graph = {}

for line in lines:
    start, end = line.split('-')
    graph.setdefault(start, []).append(end)
    graph.setdefault(end, []).append(start)


def traverse(node, seen, twice):
    if node == 'end':
        return True

    if node in seen:
        if node == 'start':
            return False

        if twice:
            return False

        twice = True

    if node.islower():
        seen = seen | {node}

    return sum(traverse(neighbour, seen, twice) for neighbour in graph[node])

print('Part 1:', traverse('start', set(), True))
print('Part 1:', traverse('start', set(), False))
