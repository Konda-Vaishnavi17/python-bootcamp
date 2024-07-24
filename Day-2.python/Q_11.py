#take list from given user and use append,pop,sort
my_list=list(map(int,input().split(" ")))
print("enter 1 for append")
print("enter 2 for pop")
print("enter 3 for sort")
print("enter 4 for lengths")
choice=int(input())
if (choice==1):
    my_list.append(9999)
    print(*my_list)
elif (choice==2):
       my_list.pop(2)
       print(*my_list)
elif (choice==3):
     my_list.sort()
     print(*my_list)
else:
    print(f"good morning length of the list{len(my_list)}")