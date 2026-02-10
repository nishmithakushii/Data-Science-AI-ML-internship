import numpy as np
arr=np.arange(24)
reshaped=arr.reshape(4,3,2)
transpose=reshaped.transpose(0,2,1)
print("final shape:",transpose.shape)
print("reshaped array:\n",reshaped)
print("\nfinal array:\n",transpose)