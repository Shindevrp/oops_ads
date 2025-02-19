from studentCourse import Student,Course,EnrollmentManager
def main():
    # Create students
    student1 = Student(1, "Alice", [])
    student2 = Student(2, "Bob", [])
    
    # Create a course with maximum enrollment 1 to test capacity limits
    course = Course("CS101", "Intro to CS", 1, 0)
    
    # Create EnrollmentManager with students and the course
    em = EnrollmentManager([student1, student2], [course])
    
    # Test enrolling first student (should succeed)
    enroll1 = em.enrollStudent(1, "CS101")
    print("Alice enrolled in CS101:", enroll1)
    
    # Test enrolling second student (should fail due to capacity)
    enroll2 = em.enrollStudent(2, "CS101")
    print("Bob enrolled in CS101 (should fail):", enroll2)
    
    # List students in CS101
    print("Students in CS101:")
    for s in em.listStudentsInCourse("CS101"):
        print(s.name)
    
    # Additional: Check student's enrolled courses
    print("Alice's courses:", student1.getCourses())
    print("Bob's courses:", student2.getCourses())

if __name__ == '__main__':
    main()
