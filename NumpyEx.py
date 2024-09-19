import numpy as np
a= np.zeros(5,int)
print(a)
b= np.ones(5,int)
print(b)
c= np.arange(2,20,2)
print(c)


from numpy import *
a=arange(1,6)
b = a.view()
print("original arrays: ",a)
print("new array ",b)
b[0]=99
print("original array: ",a)
print("new array ",b)