class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] # list of students

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()     
        return value / len(self.students)

programming = Course("programming", 2)

bill = Student("bill", 19, 85)
jill = Student("jill", 19, 65)
danny = Student("danny", 18, 80)

print(programming.add_student(bill))
print(programming.add_student(jill))
print(programming.get_average_grade())
print(programming.add_student(danny))

