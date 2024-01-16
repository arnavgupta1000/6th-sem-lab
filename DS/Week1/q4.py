a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
if(a>b and a>c):
    print("1st is greatest")
elif(b>c and b>a):
    print("2nd is greatest")
else:
    print("3rd is greatest")
