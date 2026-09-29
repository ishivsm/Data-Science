"""

Handling Missing Values in NumPy
A missing value means data is not available for a particular element.

In NumPy, missing numerical values are commonly
 represented using np.nan (NaN = Not a Number).
non--not a number  #we cant compare directly
"""
#np.isnan(array)
import numpy as np

arr=np.array([1,2,3,np.nan,5,np.nan,6])

print(np.isnan(arr))



