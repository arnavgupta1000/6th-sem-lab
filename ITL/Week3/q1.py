print("Enter for choice: \n 1) ADD\n 2) Subtract \n 3.) Multiply\n 4.) Divide \n 5.) exit")
a1=int(input("enter 1st number: "))
a2=int(input("Enter 2nd number: "))
while(True):
    choice=int(input())
    if(choice==1):
        print("The sum is :",a1+a2)
    elif(choice==2):
        print("the diff is : ",a1-a2)
    elif(choice==3):
        print("the product is :",a1*a2)
    elif(choice==4):
        print("The quotient is : ",a1/a2)
    else:
        break

 
