import numpy as np
l1=np.arange(9)**2
l1=l1.reshape(3,3)
print(l1)
rowsum=np.sum(l1,axis=0)
print(" Row sum : ",rowsum)
colsum=np.sum(l1,axis=1)
print("Col sum : ",colsum)

