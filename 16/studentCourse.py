class Student:
    def __init__(self,studentId,name,enrolledCourses) -> None:
        self.studentId = studentId
        self.name = name
        self.enrolledCourses = enrolledCourses

    def enroll(self,courseCode):
        self.enrolledCourses.append(courseCode)
    def getCourses(self):
        return self.enrolledCourses

class Course:
    def __init__(self,courseCode,courseName,maxEnrollment,currentEnrollment) -> None:
        self.courseCode = courseCode
        self.courseName = courseName
        self.maxEnrollment = maxEnrollment
        self.currentEnrollment = 0
    
    def canEnroll(self):
        if self.currentEnrollment< self.maxEnrollment:
            return True
        return False


class EnrollmentManager:
    def __init__(self,student,courses) -> None:
        self.students=student
        self.courses=courses

    def enrollStudent(self,studentId,courseCode):
        for student in self.students:
            if student.studentId==studentId:
                for i in  self.courses:
                    if i.canEnroll():
                        student.enroll(courseCode)
                        i.currentEnrollment+= 1
                        return True
        return False

        
    
    def listStudentsInCourse(self,courseCode):
        new = []
        for student in self.students:
            if courseCode in student.enrolledCourses:
                new.append(student)
        return new
        