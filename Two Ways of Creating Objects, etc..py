# TWO WAYS OF CREATING OBJECTS, FUNCTIONS (METHODS) AND ATTRIBUTES

class Class_name1:
    def __init__(self, name_of_string_attribute1):
        self.value_of_attribute1 = name_of_string_attribute1
First_object = Class_name1("actual_string_attribute_of_object1")
print(First_object.value_of_attribute1)

# RESULT: actual_string_attribute_of_object1

class DBR:
    def __init__(self, my_name):
        self.actual_name = my_name
Me = DBR("David")
print(Me.actual_name)

# RESULT: David

class Class_name2:
    def Function(self, name_of_string_attribute2):
        self.value_of_attribute2 = name_of_string_attribute2

First_object.value_of_attribute2 = "actual_string_attribute_of_object2"
print(First_object.value_of_attribute2)

# RESULT: actual_string_attribute_of_object2

class Pamela:
    def Function(self, my_name):
        self.actual_name = my_name
Me.Function = "Pam"
print(Me.Function)

# RESULT: Pam