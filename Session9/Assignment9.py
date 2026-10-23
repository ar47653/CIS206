#GIVEN DATA
courses = {
"Python": {"Alice", "Bob", "Charlie", "David"},
"Database": {"Bob", "Eve", "Frank", "Alice"},
"Networking": {"Charlie", "George", "Alice"},
"Cybersecurity": {"David", "Eve", "Henry", "Charlie"}
}

#PRINT EACH COURSE NAME
def print_course_name(courses_dict):
    print("\nCOURSES:")
    for course in courses_dict:
        print(course)
    print()

#PRINT STUDENTS IN EACH COURSE
def print_students(courses_dict):
    print("\nSTUDENTS")
    for course, student in courses_dict.items():
        print(course + ":")
        for name in student:
            print(name)
        print()

#PRINT NUMBER OF STUDENTS IN EACH COURSE 
def print_number_of_students(courses_dict):
    print("\nNUMBER OF STUDENTS")
    for course, student in courses_dict.items():
        print(course + ":")
        print(len(student))
    print()

#FIND STUDENTS ENROLLED IN MULTIPLE COURSES
def find_students(courses_dict):
    print("\nSTUDENTS ENROLLED IN PYTHON AND DATABASE:")
    temp = []
    for course, student in courses_dict.items():
        if course == "Python" or course == "Database":
            for name in student:
                if name in temp:
                    print(name)
                temp.append(name)
    print()
    print("\nSTUDENTS ENROLLED IN PYTHON AND CYBERSECURITY:")
    temp = []
    for course, student in courses_dict.items():
        if course == "Python" or course == "Cybersecurity":
            for name in student:
                if name in temp:
                    print(name)
                temp.append(name)
    print()

#PRINT ALL STUDENTS 
def print_all_students(courses_dict):
    print("\nALL STUDENTS:")
    all_students = []
    for course, student in courses_dict.items():
        names = []
        for name in student:
            names.append(name)
        all_students = set(all_students).union(names)
    for students in all_students:
        print(students)
    print()

#FIND STUDENTS THAT ARE TAKING ONLY ONE COURSE 
def find_student_one_course(courses_dict):
    print("\nSTUDENTS TAKING ONLY ONE COURSE")
    students = []
    removed = []
    for course, student in courses_dict.items():
        for name in student:
            if name not in students and name not in removed:
                students.append(name)
            elif name in students:
                students.remove(name)
                removed.append(name)
            elif name in removed:
                continue
    for one_course_student in students:
        print(one_course_student)
    print()

#USER SEARCH STUDENT 
def user_search(courses_dict):
    print("\nSEARCH A STUDENT: ")
    user_input = input("Enter a student name: ")
    courses = []
    for course, student in courses_dict.items():
        if user_input in student:
            courses.append(course)
    if not courses:
        print("Student not found.")
    else:
        print(user_input + " is enrolled in: ")
        for course_name in courses:
            print(course_name)
    print()




def main():
    print_course_name(courses)
    print_students(courses)
    print_number_of_students(courses)
    find_students(courses)
    print_all_students(courses)
    find_student_one_course(courses)
    user_search(courses)


main()
