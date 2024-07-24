#a=input() check +or- and odd or even

a=int(input())
if(a%2==0 and a>0):
    print("a is positive and even")
elif(a%2==0 and a<0):
    print("a is negative and even")
elif(a%2==1 and a>0):
     print("a is positive and odd")
     
    