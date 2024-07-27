#multiple inheritence

class Father:
    def father_speak():
        return "father class"
class mother:
    def mother_speak():
        return "mother class"
class kid(Father,mother):
    def kid_speak():
        return "Iam kid Im having properties of mother and father"
obj1=kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())
