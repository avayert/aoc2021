from common import lines

import collections
import functools
import itertools


# this makes the mod stuff easier since we can just add 1 after mod 10
player1, player2 = [int(line.split(':')[1]) - 1 for line in lines]

def rolls():
    it = itertools.cycle(range(1, 100 + 1))
    while True:
        yield sum(itertools.islice(it, 3))

players = [(player1, 0), (player2, 0)]
for i, throw in enumerate(rolls()):
    current = i % 2
    position, score = players[current]

    position = (position + throw) % 10
    score += position + 1

    players[current] = (position, score)

    if score >= 1000:
        break

n_throws = (i + 1) * 3
_, loser_score = players[current - 1]
print('Part 1:', n_throws * loser_score)


@functools.cache
def who_won(current_player, opponent):
    pos, score = opponent
    if score >= 21:
        return 0, 1  # opponent won

    pos, score = current_player
    if score >= 21:
        return 1, 0  # current player won


    # if neither player has won, move
    current_wins = opponent_wins = 0

    for throws in itertools.product((1, 2, 3), repeat=3):
        move = sum(throws)

        lands_on = (pos + move) % 10

        # round swaps so the perspective of current and opponent does too
        opponent_won, current_won = who_won(opponent, (lands_on, score + lands_on + 1))

        current_wins += current_won
        opponent_wins += opponent_won

    return current_wins, opponent_wins

print('Part 2:', max(who_won((player1, 0), (player2, 0))))

