import numpy as np
l1=np.arange(9).reshape(3,3)
print(l1)
l2=np.arange(9)**2
l3=l2.reshape(3,3)
print(l3)
sum=np.add(l1,l3)
print(sum)
