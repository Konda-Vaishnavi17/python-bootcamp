#write a program to print all the vowels and consonants
vowels="aeiou"
abc="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="hello wOrld"  #---if any capital is there then it does not count therefore first we need to take lower() function 
inp=i.lower()
for i in inp:
    if(i in vowels):
        count+=1
for i in inp:
    if(i in abc):
        c+=1
print(count)
print(c)