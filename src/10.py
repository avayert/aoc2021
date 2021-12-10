from common import lines

import collections
import statistics


OPENING = 'X([{<'
CLOSING = {
    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137),
}

incomplete = []
corrupted = 0

for line in lines:
    stack = collections.deque()

    for char in line:
        if char in CLOSING:
            lead, value = CLOSING[char]
            if stack.pop() != lead:
                corrupted += value
                break
        else:
            stack.append(char)
    else:
        n = 0
        while stack:
            n *= 5
            n += OPENING.index(stack.pop())
        incomplete.append(n)

print('Part 1:', corrupted)
print('Part 2:', statistics.median(incomplete))
