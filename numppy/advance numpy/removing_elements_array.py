"""
Removing Elements from NumPy Arrays
In NumPy, there are several ways to remove elements. 
The most common method is np.delete().
np.delete()


1. Using np.delete()
Syntax
np.delete(array, index)
"""
"""
10 → index 0
20 → index 1
30 → index 2
40 → index 3
50 → index 4
"""
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

new_arr = np.delete(arr, 2)

print(new_arr)


"""
| Operation           | Example                     | Meaning                          |
| ------------------- | --------------------------- | -------------------------------- |
| Remove one element  | `np.delete(arr, 2)`         | Remove index 2                   |
| Remove multiple     | `np.delete(arr, [1, 3])`    | Remove indexes 1 and 3           |
| Remove row          | `np.delete(arr, 1, axis=0)` | Remove row 1                     |
| Remove column       | `np.delete(arr, 1, axis=1)` | Remove column 1                  |
| Conditional removal | `arr[arr <= 30]`            | Keep values satisfying condition |

"""