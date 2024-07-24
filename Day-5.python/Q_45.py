#ABC,4---input----->A after 4 means E,B AFTER 4 MEANS F
# o/p:EFG 

str=input()
ans=0
for i in str:
    print(chr(ord(i)+4),end=" ")
print()
