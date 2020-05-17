import numpy as np
import sys

a=np.array([1,2,3,4,5,6,7])
print(a)
print(type(a))
print(a.dtype)#type of array content

a[2]=3.0#change an element
print(a)
print(a.dtype)

b=a[0:2]#store a subset to b
print(b)

a[4:6]=6,7
print(a)

c=np.array([9,1,4,6])
select=[1,2]#get elements at positions 1 n 2
d=c[select]
print(d)

c[select]=100#replace elements at selected locations
print(c)

print(a.size)
print(a.ndim)#dimension of array
print()
print(a.shape)

x=np.array([1,-1,1,-1])
print(x.mean())
print(x.std())#standard deviation


print(a.max())
print(a.min())

#ARITHMETIC OPERATIONS ON NUMPY ARRAYS

u=np.array([1,0])
v=np.array([0,1])
print(u)
print(v)
print("u+v")
print(u+v)
print("u-v")
print(u-v)
print("u*v")
print(u*v)
print("u+scalar")
print(u+2)
print("u-scalar")
print(u-1)
print("u*scalar")
print(u*3)
print("u/scalar")
print(u/2)
print("Dot prodduct of u and v")
print(np.dot(u,v))

y=([np.pi,np.pi/2,0])
print(np.sin(y))

z=np.linspace(0,1,num=5)#get 5 values in between the numbers 0 and 1
print(z)

g=np.linspace(0,np.pi*2,num=4)
print(np.sin(g))