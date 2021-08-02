# CREATE CLASS

class Person:

# CREATE METHODS (FUNCTIONS)

    def name(self):
        print("This person's name is David")

    def age(self):
        print("This person's age is 37")

    def add_one(self, x):
        return x + 1

# CREATE OBJECTS (INSTANTIATES INSTANCES OF THE CLASS Person)

dbr1 = Person()
dbr2 = Person()

# EXECUTE METHODS

dbr1.name()
dbr2.age()
print(dbr1.add_one(5))

