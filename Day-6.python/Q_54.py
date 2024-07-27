# method overiding
class Animal:
    def speak():
        return "Animal is speaking"
class dog(Animal):
    def speak():
        return "Dog is speaking"
class puppy(dog):
    def speak():
        return "puppy is speaking"
obj3=puppy
print(obj3.speak())