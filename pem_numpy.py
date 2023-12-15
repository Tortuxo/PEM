import numpy as np 

#Tests sur les arrays
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.empty([2])
c = np.concatenate((a[0],a[1]))
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
z = np.concatenate((x, y))
z = np.reshape(z,newshape=(2,3))