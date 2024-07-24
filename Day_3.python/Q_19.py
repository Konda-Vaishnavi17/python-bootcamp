#print the element in a particular index but the condition is cyclic print
#k=3
#3 6 8 4 61 2
#o/p:4
#-------
#k=8
#80 70 54 36 72
#o/p:36

my_list=list(map(int,input().split()))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])