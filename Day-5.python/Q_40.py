#print the non repeating or unique chracters in a given string
vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
ans=""
i=input()
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i  
print(ans)
