#i/p:hello123world then o/p:6

vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
check="0123456789"
ans=0
i="hello123wOrld"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)
print(ans)


