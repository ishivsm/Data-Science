
#nan.nan_to_num #default=0
import numpy as np
arr=np.array([1,2,3,np.nan,5,np.nan,6])

clr_arr=np.nan_to_num(arr,nan=50)
print(clr_arr)