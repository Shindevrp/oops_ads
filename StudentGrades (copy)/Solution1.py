class GradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_number, marks):
        self.students[name] = [int(roll_number), int(marks)]

    def display(self):
        for name, data in self.students.items():
            print(f"Name: {name}, Roll Number: {data[0]}, Marks: {data[1]}, Grade: {self.grade(data[1])}")

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
        total_marks = sum(data[1] for data in self.students.values())
        avg_m = total_marks / len(self.students)
        return avg_m


if __name__ == "__main__":
    tracker = GradeTracker()

    try:
        while True:
            s = input().strip()

            if s == " ":
                break

            if s.startswith("Add Student:"):
                parts = s[len("Add Student:"):].strip().split(", ")
                name = parts[0]
                roll_number = parts[1]
                marks = parts[2]
                tracker.add_student(name, roll_number, marks)

            elif s == "DisplayStudents":
                tracker.display()

            elif s == "CalculateAverageMarks":
                avg = tracker.calculate_average()
                print("Average Marks:", format(avg, ".2f"))
    except EOFError:
        print()
