from common import lines

from collections import Counter
import string


data = []
for line in lines:
    inputs, outputs = line.split('|')
    data.append((inputs.split(), outputs.split()))

c = Counter(len(o) for _, outputs in data for o in outputs)

print('Part 1:', c[2] + c[3] + c[4] + c[7])


# Let's look at the canonical example presented at the very start of the puzzle:
#
#
#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg
#
#
# We can count the number of times each letter appears in this output, and we
# get this:
#
# {a: 8, b: 6, c: 8, d: 7, e: 4, f: 9, g: 7}
#
# After this we can also use this LUT of frequencies and apply it over each of
# the letters used in the digits to produce this list of sums:
#
# [42, 17, 34, 39, 30, 37, 41, 25, 49, 45]
#
# Notice these sums are unique.
#
# Now, since every line is guaranteed to contain exactly one set of the digits
# 0-9, this property must hold no matter which concrete letters have been chosen
# to represent which of the segments in the display. Thus we can use the sums
# as another LUT for the original digits.

canonical = [42, 17, 34, 39, 30, 37, 41, 25, 49, 45]
LUT = dict(zip(canonical, string.digits))


total = 0
for inputs, outputs in data:
    frequencies = Counter(letter for string in inputs for letter in string)
    output_sums = [
        sum(frequencies[letter] for letter in string)
        for string in outputs
    ]

    output_digits = ''.join(LUT[s] for s in output_sums)

    total += int(output_digits)

print('Part 2:', total)
