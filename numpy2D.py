import numpy as np

a=np.array([[1,2,3],[3,4,5],[5,6,7]])
print(a)
print("Type of the array")
print(type(a))
print("Datatype of array content")
print(a.dtype)
print("size of array")
print(a.size)
print("Dimension of array")
print(a.ndim)
print("Number of rows and columns")
print(a.shape)

print()
print("Element at a position")
print(a[0][1])

print("Elements in between")
print(a[0][1:3])
print(a[1:3,2])

#x=a[2,1]
#print(x)

#BASIC OPERATIONS

x=np.array([[1,0],[0,1]])
y=np.array([[2,1],[1,2]])
print()
print("Addition")
print(x+y)
print("Subtraction")
print(x-y)
print("Multiplication")
print(x*y)
print("scalar addition")
print(x+2)
print("scalar subtraction")
print(x-2)
print("scalar multiplication")
print(x*2)
print("scalar division")
print(x/2)

print("dot product")
print(np.dot(x,y))

y=np.array([[1,2],[3,4]])
print("Transpose of Matrix")
print(y)
print(y.T)
