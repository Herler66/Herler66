#1
# import  numpy as np
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr.shape) 
# print(arr.size)
# print(arr.ndim)   # dimensions
# arr2 = np.array([1,2,3])
# arr2 = np.append(arr2,4)
# print(arr2)
# arr2 = np.delete(arr2,0)
# print(arr2)

#2
# import  numpy as np 
# arr = np.zeros((2,3))
# print(arr)
# arr2 = np.ones((2,3,4))
# print(arr2)
# arr3 = np.arange(4,10,2) # 4 - 10 step = 2
# print(arr3)
# arr4 = np.linspace(1, 3, 6) # 分成6分
# print(arr4) 
# arr5 = np.full((2,2),8)
# print(arr5)
# arr6 = np.eye(3) # identity matrix
# print(arr6)
# arr7 = np.ones((3,3),dtype = int)

#3
import numpy as np 
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(np.sqrt(x))
v = np.array([9,10])
w = np.array([11,13])
v.dot(w) #  点积
w.dot(v) 
np.dot(v, w) 
v = np.array([[9,10], [98, 67]])

np.sum(v)  
print(np.sum(v, axis=0))  # array([107,  77]), this gives us the sum of the columns stored in an array
