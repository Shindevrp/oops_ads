class Student:
    def __init__(self, name, rn, m):
        self.name = name
        self.rollNumber = rn
        self.marks = m

    def getGrade(self):
        if (self.marks>=90):
            return 'A'
        elif (self.marks >= 80 and self.marks < 90):
            return 'B'
        elif (self.marks >= 70 and self.marks < 80):
            return 'C'
        else:
            return 'D'
    # Name: Ian, Roll Number: 401, Marks: 90, Grade: A   
    def __str__(self):
        return "Name: "+self.name + ", Roll Number: "+str(self.rollNumber) + ", Marks: "+ str(self.marks) + ", Grade: "+self.getGrade()

class GradeBook:
    def __init__(self):
        self.GB = []

    def add_student(self, name, rn, marks):
        s = Student(name, rn, marks)
        self.GB.append(s)

    def display_student(self):
        for student in self.GB:
            print(student)
    
    def calculate_average(self):
        total = 0
        for student in self.GB:
            total += student.marks
        return total/len(self.GB)


try:
    gradebook = GradeBook()
    while(True):
        i = input().split(" ")
        if len(i) == 5:
            name = i[2][:-1]
            rn = int(i[3][:-1])
            marks = int(i[4])
            gradebook.add_student(name, rn, marks)
        elif i[0] == "DisplayStudents":
            gradebook.display_student()
        elif i[0] == "CalculateAverageMarks":
            print(f"Average Marks: {gradebook.calculate_average():.2f}")
except EOFError:
    pass


