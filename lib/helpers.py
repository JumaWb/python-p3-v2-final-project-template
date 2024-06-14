# lib/helpers.py
from models.Student import Student
from models.course import Course
from models.enrolment import Enrollment
def Create_students():
    Student.create_table()
    print("Table student created succcessfully!")

def Add_student():
    name = input("Enter the student's name: ")
    age = input("Enter student's age: ")
    year = input("Enter the year of study: ")
    Student.create(name, age, year)
def Update_student():
    student_id = int(input("Enter the student's ID"))
    student = Student.find_by_id(student_id)
    if student:
         name = input("Enter the student's name: ")
         age = int (input("Enter student's age: "))
         year = int (input("Enter the year of study: "))
         student.name = name
         student.age = age
         student.year = year
         student.update()
         print("Student updated successfuly!")
    else: 
        print("Failed to update!")
def Delete_student():
    student_id = int(input("Enter the Student's ID"))
    student = Student.find_by_id(student_id)
    if student:
        student.delete()
        print("Student deleted successfully!")
    else:
        print("Student not found!")
def Find_student_by_name():
    name = input("Enter the student name")
    student = Student.find_by_name(name)
    if student:
        print(f"student: {student}")
    else:
        print("student not found!")
def List_students():
     students = Student.view_students()
     for student in students:
          print(student)
    


def Create_course():
    Course.create_table()
    print("Course table created successfully!")

def Add_course():
    course_title = input("Enter the course: ")
    course_duration = input("Enter the course duration: ")
    Course.create(course_title, course_duration)
    
def Update_course():
        course_id = int(input("Enter the course ID: "))
        course = Course.find_by_id(course_id)
        if course:
            course_title = input("Enter the course title: ")
            course_duration = int(input("Enter the course duration: "))
            course.course_title = course_title
            course.course_duration = course_duration
            course.update()
            print("Course updated successfully!")
        else: 
            print("Failed to update! Course not found!")

    
def Delete_course():
        course_id = int(input("Enter the course ID: "))
        course = Course.find_by_id(course_id)
        if course:
            course.delete()
            print("Course deleted successfully!")
        else:
            print("Course not found!")

    
def Find_course_by_title():
        course_title = input("Enter the course title: ")
        course = Course.find_by_title(course_title)
        if course:
            print(f"Course: {course.course_title}, Duration: {course.course_duration}")
        else:
            print("Course not found!")
def List_course():
     courses = Course.get_all()
     for course in courses:
          print(course) 
     
def Create_enrolment():
    Enrollment.create_table()
    print("Course enrollment created successfully!")

def Add_enrolment():
    student_id = input("Enter the student id: ")
    course_id = input("Enter the course id: ")
    Enrollment.create(student_id, course_id)
 
def Update_enrollment():
        enrollment_id = int(input("Enter the enrollment ID: "))
        enrollment = Enrollment.find_by_id(enrollment_id)
        if enrollment:
            student_id = int(input("Enter the new student ID: "))
            course_id = int(input("Enter the new course ID: "))
            
            enrollment.student_id = student_id
            enrollment.course_id = course_id
            enrollment.save()
            print("Enrollment updated successfully!")
         
        else:
            print("Enrollment not found!")


def Delete_enrollment():
        enrollment_id = int(input("Enter the enrollment ID: "))
        
        enrollment = Enrollment.find_by_id(enrollment_id)
        if enrollment:
            enrollment.delete()
            print("enrollment deleted successfully!")
        else:
            print("Enrollment not found!")

    
def Find_enrollment_by_id():
        enrollment_id = int(input("Enter the enrollment ID: "))
        enrollment = Enrollment.find_by_id(enrollment_id)
        if enrollment:
             print(f"enrollment: {enrollment}")
        else:
             print("enrollment not found!")
       