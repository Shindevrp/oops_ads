class GradeTracker:
    def __init__(self):
        self.students = {}

    def grade_Tracker(self, name, rollNumber, marks):
        rollNumber = rollNumber.strip(',')
        marks = marks.strip(',')
        self.students[name] = [int(rollNumber), int(marks)]
    
    def display(self):
        for name, info in self.students.items():
            print(f"Name: {name}, Roll Number: {info[0]}, Marks: {info[1]}, Grade: {self.grade(info[1])}")
    
    def grade(self, marks):
        if marks >= 90:
            return "A"
        elif 80 <= marks < 90:
            return "B"
        elif 70 <= marks < 80:
            return "C"
        else:
            return "D"
    
    def calculate_average(self):
        if len(self.students) == 0:
            return 0
        total_marks = sum([info[1] for info in self.students.values()])
        return total_marks / len(self.students)


def main():
    tracker = GradeTracker()
    
    try:
        while True:
            s = input().strip()
            
            if s == "":
                break
            
            if s.startswith("Add Student:"):
                parts = s[len("Add Student:"):].strip().split()
                name = parts[0][:-1]
                roll_number = parts[1]
                marks = parts[2]
                tracker.grade_Tracker(name, roll_number, marks)
            
            elif s == "DisplayStudents":
                tracker.display()
            
            elif s == "CalculateAverageMarks":
                avg = tracker.calculate_average()
                print(f"Average Marks: {avg:.2f}")
    except EOFError:
        print()

main()