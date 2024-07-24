#Q:8 given an space separated integer list find the average of elements present in the even index
my_list=list(map(int,input().split(" ")))
sum=0
avg=0
i=0
for i in range(0,len(my_list)):
    if (i%2==0):
        sum=sum+1
        avg=sum/len(my_list)

print(avg)


