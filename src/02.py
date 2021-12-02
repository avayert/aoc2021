from common import lines

lines = [
    (direction, int(amount))
    for line in lines
    for direction, amount in [line.split()]
]


horizontal = vertical = 0

for direction, amount in lines:
    if direction == 'forward':
        horizontal += amount
    elif direction == 'down':
        vertical += amount
    elif direction == 'up':
        vertical -= amount

print('Part 1:', horizontal * vertical)

horizontal = vertical = aim = 0

for direction, amount in lines:
    if direction == 'forward':
        horizontal += amount
        vertical += aim * amount
    elif direction == 'down':
        aim += amount
    elif direction == 'up':
        aim -= amount

print('Part 2:', horizontal * vertical)
