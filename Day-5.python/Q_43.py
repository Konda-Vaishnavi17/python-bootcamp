#write a code to print all the capital letters in a string

str=input()
for i in str:
    if(ord(i)>=65 and ord(i)<=91):  
        print(i)
