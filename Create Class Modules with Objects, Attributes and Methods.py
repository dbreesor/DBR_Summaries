class Person:

    # CREATE METHODS (FUNCTIONS)

    def __init__(self, name, sex):
        self.the_name = name
        self.the_sex = sex

    def one_function(self):
        return ("Hello, my name is " + self.the_name + " and I am " + str(self.set_age) + " years old")

    def a_function(self, x):
        return x + 1

    def that_sex(self):
        if self.the_sex == "male":
            return True
        else:
            return False

# ENABLES ATTRIBUTES TO BE SET ON THE FLY

    def set_age(self, age):
        self.the_age = age

# CREATE OBJECTS AND ATTRIBUTES

dbr1 = Person("David", "male")
dbr2 = Person("Pam", "female")

dbr1.set_age = 91
dbr2.set_age = 45
print (dbr1.set_age)

# PRINT ATTRIBUTES AND CALL METHODS

print(dbr1.the_name)
print(dbr2.the_sex)
print(dbr1.a_function(4))
print(dbr2.a_function(16))

print(dbr1.one_function())
# OR in Methods creation section "Print" and simply call it here: dbr1.one_funtion()

# ENABLES ATTRIBUTES TO BE CHANGED ON THE FLY

dbr1.the_age = 73
print(dbr1.the_age)

# CALL THE IF / ELSE METHOD (FUNCTION)

print(dbr1.that_sex())
print(dbr2.that_sex())

