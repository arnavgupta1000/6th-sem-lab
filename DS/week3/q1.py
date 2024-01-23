import numpy as np
x=int(input("Enter a number :"))
l1=np.array([1])
for i in range(2,x+1):
    if(x%i==0):
        l1=np.append(l1,i)
print(l1)
