 #Q:7 your are given with a comma separated natural numbers 1-10 print even numbers
#my_list=list(map(int,input().split(",")))
#for i in range(1,len(my_list),2):
   #print(my_list[i])


#Q_7.1 how many even numbers are there in above question
#my_list=list(map(int,input().split(",")))
#count=0
#for i in range(1,len(my_list),2):
 #  count+=1
  # print(count)


#Q:7.2 your are given with a spce seperated integer list find the number of even elements and number of odd elements in a given list
my_list=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(my_list)):
   if (my_list[i]%2==0):
          even+=1   
   else:
          odd+=1
print(even)
print(odd)


#Q:8 given an space separated integer list find the average of elements present in the even index


