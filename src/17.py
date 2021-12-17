from common import raw


from functools import cache
import operator
import re

x0, x1, y0, y1 = map(int, re.findall('-?\d+', raw))

# Since the ball takes steps of N, N - 1, ..., 1 when going up and 1, 2, ..., N
# when falling back down, it must come back to y=0 at some point.
#
# This means the next step will move the ball `y_vel + 1` distance down.
#
# This in turn means the maximum distance will be achieved when the step taken
# will reach the very bottom of the square - that is - y0.
#
# Since this step is taken at `y_vel + 1`, this maximum velocity must therefore
# simply be `abs(y0) - 1`, and the height must therefore be the sum of the
# natural numbers up to it.
vel = abs(y0) - 1
print('Part 1:', vel * (vel + 1) // 2)


# I wrote about 60 more lines about triangular numbers and combinatorics
# but this was just so much simpler.
def simulate(x_vel, y_vel):
    x = y = 0

    while y0 <= y:
        x += x_vel
        y += y_vel

        y_vel -= 1
        x_vel -= x_vel != 0

        if x0 <= x <= x1 and y0 <= y <= y1:
            return True
    return False

success = sum(
    simulate(x_vel, y_vel)
    for x_vel in range(0, x1 + 1)
    for y_vel in range(y0, abs(y0) + 1)
)

print('Part 2:', success)
