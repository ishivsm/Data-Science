
"""Important NumPy Array Manipulation Functions

| Function        | Purpose                     |
| --------------- | --------------------------- |
| `reshape()`     | Change array shape          |
| `flatten()`     | Convert to 1D copy          |
| `ravel()`       | Convert to 1D               |
| `.T`            | Transpose                   |
| `transpose()`   | Transpose array             |
| `concatenate()` | Join arrays                 |
| `vstack()`      | Stack vertically            |
| `hstack()`      | Stack horizontally          |
| `split()`       | Split array                 |
| `np.newaxis`    | Add dimension               |
| `resize()`      | Change size/shape           |
| `squeeze()`     | Remove dimensions of size 1 |

"""
import numpy as np
arr1=np.array([[10,20,30]
             ,[40,50,60]])

arr2=np.array([[10,20,30]
             ,[40,50,60]])

arr3=np.concatenate((arr1,arr2))
print(arr3)