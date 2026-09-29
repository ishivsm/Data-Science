import numpy as np
arr_2d=np.array([[1,20],[1,60]])

print(arr_2d)

#insert a new row at index 1
new_arr2d=np.insert(arr_2d,1,[5,6],axis=0)
print(new_arr2d)

new_arr2d=np.insert(arr_2d,1,[5,6],axis=1)
print(new_arr2d)