#print a leap year in a given range

year=int(input())
for i in range(2000,2025):
    if((i%4)==0 and (i%100)!=0):
        print(i,end=" ")
