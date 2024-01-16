print("1.) enter upto N elements in the list \n 2.) delete specified using del \n 3.) insert specified \n 4.) delete specified using remove \n 5.) check element in list \n 6.) reverse")
l1=[]
while(True):
    a=int(input("Enter for choice"))
    if(a==1):
        ch=int(input("Enter number of elements :"))
        for i in range(0,ch):
            ip=int(input("Enter elements"))
            l1.append(ip)
        print(l1)
    elif(a==2):
        dd=int(input("Enter index: "))
        del l1[dd]
        print(l1)
    elif(a==3):
        l1.insert(4,"maths")
        print(l1)
    elif(a==5):
        check=int(input())
        if(check in l1):
            print("True")
        else:
            print("False")
    elif(a==4):
        cj=input()
        l1.remove(cj)
        print(l1)
    elif(a==6):
        print(l1)
        l1.reverse()
        print(l1)
    else:
        break


