t1=(12, 7, 38, 56, 78)
t2=()
t2=list(t2)
t1=list(t1)
for i in t1:
    if(i%2==0):
        t2.append(i)
t2=tuple(t2)
print(t2)

