from common import raw

from math import prod
import collections
import operator


bits = collections.deque(bit for digit in raw for bit in format(int(digit, 16), '04b'))

def pop_n(n):
    return ''.join(bits.popleft() for _ in range(n))

def parse_n(n):
    return int(pop_n(n), 2)


def unpack(op):
    return lambda input: op(*input)

operations = [
    sum,
    prod,
    min,
    max,
    next,
    unpack(operator.gt),
    unpack(operator.lt),
    unpack(operator.eq),
]


def read_children(type):
    if type == 4:
        n = ''
        remaining = True
        while remaining:
            remaining = parse_n(1)
            n += pop_n(4)
        yield int(n, 2)
    else:
        length_id = parse_n(1)

        if length_id:
            n_packets = parse_n(11)
            for _ in range(n_packets):
                yield parse_packet()
        else:
            length = parse_n(15)
            stop_at = len(bits) - length
            while stop_at < len(bits):
                yield parse_packet()

version_sum = 0

def parse_packet():
    global version_sum

    version = parse_n(3)
    type_id = parse_n(3)

    version_sum += version

    return operations[type_id](read_children(type_id))

n = parse_packet()

print('Part 1:', version_sum)
print('Part 2:', n)
