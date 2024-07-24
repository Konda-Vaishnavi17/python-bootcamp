#find the elements present in K+N index
#k=3
#n=2
#3 6 8  4 6 2
#o/p:2
#--------
#k=3
#n=4
#80 70 54 36 72
#o/p:error

my_list=list(map(int,input().split()))
k=int(input())
n=int(input())
if (len(my_list)<k+n):
    print("error")
for i in range (len(my_list)):
    print(my_list[k+n],end=" ")
    break
    
 