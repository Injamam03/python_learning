class Animal:
    def sound(self):
        print("some sound")

class Dog(Animal):
    def sound(self):










        
        print("woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Ambah, Ambah")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()
























"""class Animal:
    def __init__(self, name):
        self.name = name
        print(self.name + " was adopted.")
    def run(self):
        print("running!")
 
class Turtle(Animal):
    def run(self):
        super().run() 
        print("running slowly!")
 
# we get back an interesting response
tim = Turtle("Injamam")  
tim.run()

a = Animal( "injamam")
a.run()
"""








"""
class Animal:
    def __init__(self, name):
        self.name = name
        print(self.name + " was adopted.")

    def run(self):
        print("running!")

    def sound(self):
        print("some sound!")


class Turtle(Animal):
    def run(self):
        print(self.name + " is running slowly!")

    def sound(self):
        print(self.name + " says: ssss!")


class Dog(Animal):
    def run(self):
        print(self.name + " is running fast!")

    def sound(self):
        print(self.name + " says: woof!")


class Cat(Animal):
    def run(self):
        print(self.name + " is running!")

    def sound(self):
        print(self.name + " says: meow!")


# Object তৈরি করো
tim = Turtle("Tim")
dog = Dog("Bruno")
cat = Cat("Mimi")

print("-------------------")

# সবার run() call করো
tim.run()
dog.run()
cat.run()

print("-------------------")

# সবার sound() call করো
tim.sound()
dog.sound()
cat.sound()
"""

