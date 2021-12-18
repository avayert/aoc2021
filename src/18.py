# I chose a dynamically typed language so now I suffer

from common import lines

from dataclasses import dataclass
import itertools
import functools
import math


def add_left(num, n):
    match num:
        case [left, right]:
            return [add_left(left, n), right]
    return num + n

def add_right(num, n):
    match num:
        case [left, right]:
            return [left, add_right(right, n)]
    return num + n


def explode(num, depth=0):
    match num:
        case [left, right]:
            if depth == 4:
                return 0, left, right

            match explode(left, depth + 1):
                case new_left, carry_left, carry_right:
                    return [new_left, add_left(right, carry_right)], carry_left, 0

            match explode(right, depth + 1):
                case new_right, carry_left, carry_right:
                    return [add_right(left, carry_left), new_right], 0, carry_right

def split(num):
    match num:
        case [left, right]:
            match split(left):
                case [l, r]:
                    return [[l, r], right]
            match split(right):
                case [l, r]:
                    return [left, [l, r]]

            return None

    if num >= 10:
        return [math.floor(num / 2), math.ceil(num / 2)]


def step(num):
    match explode(num):
        case (exploded, _, _):
            return step(exploded)

    # I literally do not think you can do this with a `match`
    res = split(num)
    if res is not None:
        return step(res)

    return num

def magnitude(num):
    match num:
        case [left, right]:
            return 3 * magnitude(left) + 2 * magnitude(right)
    return num


numbers = [eval(line) for line in lines]

remaining = functools.reduce(lambda a, b: step([a, b]), numbers)
print('Part 1:', magnitude(remaining))

possible = [magnitude(step([a, b])) for a, b in itertools.permutations(numbers, r=2)]
print('Part 2:', max(possible))
