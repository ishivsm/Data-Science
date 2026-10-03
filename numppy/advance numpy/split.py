"""
Splitting Arrays in NumPy
Splitting means dividing one NumPy array into multiple smaller arrays.

The main functions are:

np.split() → equal-sized splits

np.array_split() → can handle unequal splits

np.vsplit() → split vertically

np.hsplit() → split horizontally

#np.split(array, number_of_parts)



| Function           | Purpose                 |
| ------------------ | ----------------------- |
| `np.split()`       | Equal splits            |
| `np.array_split()` | Equal or unequal splits |
| `np.vsplit()`      | Split rows              |
| `np.hsplit()`      | Split columns           |



split       → general splitting
array_split → flexible splitting
vsplit      → vertical / rows
hsplit      → horizontal / columns
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.split(arr, 3)

print(result)

"""#3. np.array_split()

The difference is that array_split()
can split an array into unequal parts."""

arr = np.array([10, 20, 30, 40, 50])

result = np.array_split(arr, 3)

print(result)


#vsplit
result = np.vsplit(arr, 2)

print(result)

#hsplit

result = np.hsplit(arr, 2)

print(result)