#  multilevel inheritence code

class Animal:
    def speak():
        return "Animal is speaking"
class dog(Animal):
    def bark():
        return "Bow"
class puppy(dog):
    def puppy_speak():
        return "iam puppy"
obj3=puppy
print(obj3.speak())
print(obj3.bark())
print(obj3.puppy_speak())
