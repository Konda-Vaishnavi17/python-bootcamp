#replace the elements in an array with average of max and min element
#13 2 67 20 68
#68+2=70==35
#35 35 35 35 35

my_list=list(map(int,input().split()))
maxi=my_list[0]
for i in range(0,len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
print(maxi)
mini=my_list[0]
for i in range(0,len(my_list)):
    if(my_list[i]<mini):
        mini=my_list[i]
print(mini)
avg=0
avg=(maxi+mini)//2
for i in range(len(my_list)):
    my_list[i]=avg   #assigning avg value to every element in my_list
print(my_list)




