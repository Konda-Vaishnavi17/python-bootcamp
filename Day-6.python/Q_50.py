#oops instances
class Myclass:
    def add(a,b):
       ins_var=" im instance var"
       print("ins_var_add")
       return a+b
    def sub(a,b):
       return a-b
    def mul(a,b):
       return a*b
    def mod(a,b):
       return a%b
obj1=Myclass
print(obj1.add(2,5))


