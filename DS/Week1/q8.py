l1=[]
ch=int(input("Enter number of elements: "))
for i in range(ch):
    ele=int(input("Enter elements: "))
    l1.append(ele)
for i in range(ch):
    if(l1[i]<0):
        print(l1[i])

