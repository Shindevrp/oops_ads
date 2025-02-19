def grade_Tracker(d,name ,roolNumber,marks):
    d[name]=[int(roolNumber),int(marks)]
    return d
def display(d):
    for k,v in d.items():
        print(f"Name: {k}, Roll Number: {v[0]}, Marks: {v[1]}, Grade: {grade(v[1])}")

# Name: Xavier, Roll Number: 801, Marks: 64, Grade: D
# Name: Yolanda, Roll Number: 802, Marks: 92, Grade: A

def grade(marks):
    if marks >= 90:
        return "A"
    elif 80 <= marks < 90:
        return "B"
    elif 70 <= marks < 80:
        return "C"
    else:
        return "D"

def calculate_average(d):
    if len(d) == 0:
        return 0
    total_marks = 0
    for k in d:
        total_marks += d[k][1]
    avg_m = total_marks / len(d)

    return avg_m
# d = {}
# s = input().split( )
# print(s)
# while s != "end ":
    
#     if "Add Student:" in s:
#         parts = s.split(":")[1].strip().split(", ")
#         name = parts[0]
#         roll_number = parts[1]
#         marks = parts[2]
#         d = grade_Tracker(d, name, roll_number, marks)

#     elif s == "DisplayStudents":
#         display(d)
#     elif s == "CalculateAverageMarks":
#         avg = calculate_average(d)
#         print("hello")
#         print("Average Marks:", round(avg, 2))
#     # s = input().split()
# while True:
#     s = input().strip()  

#     if s == " ":  
#         break
    
#     if s.startswith("Add Student:"):
#         parts = s[len("Add Student:"):].strip().split(", ")
#         name = parts[0]
#         roll_number = parts[1]
#         marks = parts[2]
#         d = grade_Tracker(d, name, roll_number, marks)
    
#     elif s == "DisplayStudents":
#         display(d)
    
#     elif s == "CalculateAverageMarks":
#         avg = calculate_average(d)
#         print("Average Marks:", round(avg, 2))
    

d = {}

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
            d = grade_Tracker(d, name, roll_number, marks)
        
        elif s == "DisplayStudents":
            display(d)
        
        elif s == "CalculateAverageMarks":
            avg = calculate_average(d)
            print("Average Marks:", format(avg, ".2f")) 
except EOFError:
    print()