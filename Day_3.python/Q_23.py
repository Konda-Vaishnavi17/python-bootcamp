#find the missing number in an array
#
my_list=list(map(int,input().split(" ")))
sum=0
sum1=0
missing_num=0
for i in range(1,11):
    sum=sum+i
for i in range(0,len(my_list)):
     sum1=sum1+my_list[i]
missing_num=sum-sum1
print(missing_num)
