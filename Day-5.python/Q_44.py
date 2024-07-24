#REMOVE ALL THE BRAKECTS FROM THE GIVEN ALGEBRIC EXPERESSION
#{==123,}==125
#(==40,)==41
#[==91,]==93


str=input()
for i in str:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end=" ")  

