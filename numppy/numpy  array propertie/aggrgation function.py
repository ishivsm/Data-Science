#aggregation means summary like total,avg,highest,lowewst
"""
function
np.sum(array)--add all
np.mean(array)--calculate avg
np.min(array) -- min
np.max(array)-- max
np.std(array)--standard derivation
np.var(array)--varaince
"""

import numpy as np

arr=np.array([10,20,30,40,50,60])

print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))