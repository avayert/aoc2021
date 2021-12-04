from common import lines

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


l = iter(lines)

nums = list(map(int, next(l).split(',')))
next(l)  # consume empty line

boards = []
while True:
    board_lines = list(itertools.takewhile(lambda line: line != '', l))
    if not board_lines:
        break

    rows = [list(map(int, line.split())) for line in board_lines]
    boards.append(Board(rows))


def find_first():
    for num in nums:
        for board in boards:
            if board.prune(num).done:
                return board, num

board, num = find_first()
print('Part 1:', board.sum() * num)

def find_last():
    won = collections.deque(maxlen=1)

    for num in nums:
        for board in boards.copy():
            if board.prune(num).done:
                won.append(board)
                boards.remove(board)

        if not boards:
            return won[0], num

board, num = find_last()
print('Part 2:', board.sum() * num)
