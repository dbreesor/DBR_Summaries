class Person:

# CLASS ATTRIBUTE - not specific to any object - Global Variable

    number_of_people = 0
    gravity = -9.8

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person ("tim")
print(Person.number_of_people)
p2 = Person ("jill")
print(Person.number_of_people)

# CLASS METHODS

class Person:
    number_of_people = 0
    gravity = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("tim")
p2 = Person("jill")

print (Person.number_of_people_())

#STATIC METHODS

class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def pr():
        print("run")

print (Math.add5(5))

Math.pr()