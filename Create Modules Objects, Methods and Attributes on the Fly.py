class Student:

# A METHOD to add OBJECTS and ATTRIBUTES on the fly

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# A METHOD to return grades that were made on the fly, for use in a Course CLASS METHOD

    def get_grade(self):
        return self.grade

class Course:

# A METHOD to add additional OBJECTS and ATTRIBUTES on the fly

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

# A METHOD to add additional OBJECTS

    def add_student(self, student):
        if (len(self.students) < self.max_students):
            self.students.append(student)

# A METHOD which uses OBJECTS made on the fly and the return from a Student CLASS METHOd

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

# Creates OBJECTS and their ATTRIBUTES in the Student CLASS

s1 = Student("A", 19, 95)
s2 = Student("B", 19, 95)
s3 = Student("C", 19, 95)

# Creates OBJECTS and their ATTRIBUTES in the Course CLASS

course = Course("Science", 3)

# Uses a METHOD in the Course CLASS to add student OBJECTS to the Course CLASS

course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

# Prints the name of a particular Student OBJECT in the Course CLASS

print(course.students[0].name)

# returns result of Course CLASS METHOD that uses other OBJECTS, ATTRIBUTES and Student CLASS METHOD

print(course.get_average_grade())