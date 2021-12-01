"""
This file is awful, but it's also very funny.
"""

import inspect
import pathlib


# the top-most entry in the call stack is the main module
*_, parent_frame = inspect.stack()

# now we can get the path to the file we import from
path = pathlib.Path(parent_frame.filename)

# and we can get the name of the input file
name = path.with_suffix('.txt').name

# then we can get the `input` folder from that path
input_file = path.parent.parent / 'input' / name

# and then we can read the lines.
lines = input_file.read_text().splitlines()
