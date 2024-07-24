#check how many vowels are tere in a given string
vowels=['a','e','i','o','u']
str="hello world"
count=0
for i in str:
    if(i in vowels):
        count+=1
print(count)

