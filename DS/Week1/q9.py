l1=[]
countneg=0
countpos=0
ch=int(input("Enter number of elements: "))
for i in range(ch):
    ele=int(input("Enter elements: "))
    l1.append(ele)
for i in range(ch):
    if(l1[i]<0):
        countneg+=1
    else:
        countpos+=1
print("Number of negative ",countneg)
print("Number of positive ",countpos)

