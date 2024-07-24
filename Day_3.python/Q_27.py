#find the peak element--------printing 1peak element then break

#my_list=list(map(int,input().split(" ")))
#count=0
#for i in range(1,len(my_list)-1):
 #if((my_list[i]>my_list[i+1] and my_list[i]>my_list[i-1])):
  # count=i
 #  break
#print(my_list[count])




#printing every peak element
my_list=list(map(int,input().split(" ")))
for i in range(1,len(my_list)-1):
 if((my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1])): 
    print(my_list[i],end=" ")





      