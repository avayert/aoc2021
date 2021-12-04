from common import raw

import itertools
import collections


class Board:
    def __init__(self, rows):
        self.rows = rows

    @property
    def columns(self):
        return list(zip(*self.rows))

    @property
    def done(self):
        def pred(line):
            return all(item is None for item in line)

        return any(pred(row) or pred(col) for row, col in zip(self.rows, self.columns))

    def prune(self, n):
        self.rows = [
            [num if num != n else None for num in row]
            for row in self.rows
        ]

        return self

    def sum(self):
        return sum(n for row in self.rows for n in row if n is not None)


num_text, _, board_text = raw.partition('\n')
nums = [int(num) for num in num_text.split(',')]

boards = []
for board in board_text.split('\n\n'):
    rows = [
        [int(num) for num in row.split()]
        for row in board.splitlines()
    ]
    boards.append(Board(rows))

won = collections.deque()
for num in nums:
    for board in boards.copy():
        if board.prune(num).done:
            boards.remove(board)
            won.append((board, num))

board, num = won.popleft()
print('Part 1:', board.sum() * num)

board, num = won.pop()
print('Part 2:', board.sum() * num)
