# INHERITANCE is used when you have various CLASSES that do much that is similar

class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print (f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat (Pet):

# Call super Class (Pet) initialization to add ATTRIBUTE to OBJECT

    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    def speak(self):
        print ("Meow")

    def show(self):
        print (f"I am {self.name} and I am {self.age} years old and I am {self.colour}")

class Dog (Pet):

    def speak (self):
        print ("Bark")

class Fish(Pet):
    pass

# Dog and Cat class INHERIT the Pet METHODS.
# When METHODS that are the same in both CLASSES, the child class have priority.

p = Dog("Tim", 19)
p.show()
p.speak()

c = Cat("Bill", 34, "brown")
c.show()
c.speak()

f = Fish("Bubbles", 10)
f.speak()
