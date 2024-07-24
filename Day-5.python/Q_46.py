#I/P=hello-----wor----ld
#o/p=---------helloworld      hint:print("-",*30)-->it prints "-"(30 times)

inp=input()
count=0
ans=""
for i in inp:
     if (i=="-"):
      count+=1
     else:
        ans=ans+i
print("-"*count+ans)



