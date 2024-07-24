#WAP t0 print all the prime numbers in a given range
a=int(input())
b=int(input())
r=a**0.5+1
for i in range(a,b+1): #2-11 should run
    for j in range(2,i):
        if(i%j==0):
           break
    else:
         print(i,end=" ")



