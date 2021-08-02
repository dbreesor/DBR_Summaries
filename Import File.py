from Export import Person
from Export_1 import Another_Class

# CREATE OBJECTS (INSTANTIATES INSTANCES OF THE CLASS Person)

dbr1 = Person()
dbr2 = Person()

# EXECUTE METHODS

dbr1.name()
dbr2.age()
print(dbr1.add_one(5))

# INHERITANCE

Example = Another_Class
Example.Another_Method(Person)



