class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name} says woof!")
        

my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.age)
my_dog.bark()
        
class Cat:
    def __init__(self):
        self.color = "black"
    
    def meow(self):
        print("Meow!")

my_cat = Cat()
print(my_cat.color)
my_cat.meow()

class Dog:
    def __init__(self, name, age):
       self.name = name
       self.age = age
       
    def bark(self):
        print(f"{self.name} says woof!")
        
