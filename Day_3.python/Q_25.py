#using whileloop take the input and sum of the digits
#123
#123%10=3----r
#sum=sum+r---0+3=3
#n//2---123//2=12----extract
#....

n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)