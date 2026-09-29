"""

Stacking Arrays in NumPy
Stacking means combining two or more NumPy arrays into a single array.

The main stacking methods are:

vstack() → vertical stacking

hstack() → horizontal stacking

stack() → stacking along a new axis
verticall
horizontally

v stack
h stack
"""

#v stack
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.vstack((a, b))

print(result)

#h sttack

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.hstack((a, b))

print(result)