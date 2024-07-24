#print all the vowels followed by consonants 
vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
ans=""
i=input()
inp=i.lower()
for i in inp:
    if(i in vowels):
        ans+=i  
for i in inp:
    if(i in consonents):
        ans+=i
print(ans)