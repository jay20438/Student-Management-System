import json
import datetime

student_data = {
    "1001": ["Rajesh Sharma", 16, "2008-01-15", "10", ["Maths", "Science", "English","History"], {"Maths": 70, "Science": 70, "English": 70,"SST":70},70,"B"],
    "1002": ["Suresh Gupta", 15, "2009-05-20", "9", ["Maths", "Science", "English","History"], {"Maths": 90, "Science": 88, "English": 95,"SST":91},91,"A+"],
    "1003": ["Rani Singh", 17, "2007-03-30", "11", ["Maths", "Physics", "Chemistry","Computer Science"], {"Maths": 75, "Physics": 80, "Chemistry": 85,"Computer Science":80},80,"A"],
    "1004": ["Vansh Jain", 17, "2007-10-21", "11", ["Maths", "Economics", "Accounts","Business Studies"], {"Maths":60, "Economics":80, "Accounts":45,"Business Studies":55},60,"C"]
}

class Student:
    def __init__(self, student_id, full_name, age, dob, student_class, subjects, marks,percentage,grade):
        self.student_id = student_id
        self.full_name = full_name
        self.age = age
        self.dob = dob
        self.student_class = student_class
        self.subjects = subjects
        self.marks = marks
        self.percentage = percentage
        self.grade = grade

    def __str__(self):
        return f'Student ID: {self.student_id}\nName: {self.full_name}\nAge: {self.age}\nDOB: {self.dob}\nClass: {self.student_class}\nSubjects: {", ".join(self.subjects)}\nMarks: {self.marks}\nPercentage: {self.percentage:.2f}%\nGrade: {self.grade}'

def load_students(data):
    students = []
    for student_id, student_info in data.items():
        student = Student(student_id, *student_info)
        students.append(student)
    return students

def show_all_students(students):
    for student in students:
        print(student)
        print()

def calculate_percentage(marks):
    return sum(marks.values()) / len(marks)

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def check_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def valid_date(day,month,year):
    if month == 1 and day <= 31:
        return True
    elif month == 2:
        if check_leap_year(year) == True and day <= 29:
            return True
        elif check_leap_year(year) == False and day <= 28:
            return True
        
    elif month == 3 and day <= 31:
        return True
    elif month == 4 and day <= 30:
        return True
    elif month == 5 and day <= 31:
        return True
    elif month == 6 and day <= 30:
        return True 
    elif month == 7 and day <= 31:
        return True
    elif month == 8 and day <= 31:
        return True
    elif month == 9 and day <= 30:
        return True
    elif month == 10 and day <= 31:
        return True
    elif month == 11 and day <= 30:
        return True
    elif month == 12 and day <= 31:
        return True
    else:
        return False
    
    
def add_student():
    student_id = input("Enter Student ID: ")
    full_name = input("Enter Full Name: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    parts = dob.split("-")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    present_date = datetime.datetime.now()
    present_year = present_date.year
    present_month = present_date.month
    present_day = present_date.day

    if valid_date(day,month,year) == False:
            print("Enter a valid date!")

            while True:
                dob = input("Enter Date of Birth (YYYY-MM-DD): ")
                parts = dob.split("-")
                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2])
                print(month)
                print(day)
                
                if valid_date(day,month,year) == False:
                    print("Enter a valid date!")
                    continue
                else:
                    break
        
    
    if present_year > year:
        age = present_year - year
        if present_month < month:
            age -= 1
        elif  present_month == month:
            if present_day < day:
                age -= 1

    student_class = input("Enter Class: ")
    subjects = input("Enter Subjects (comma-separated): ").split(",")
    subjects = [subject.strip() for subject in subjects if subject.strip()]
    marks = {}
    for subject in subjects:
        marks[subject] = int(input(f"Enter marks for {subject}: "))

    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)
    
    new_student = Student(student_id, full_name, age, dob, student_class, subjects, marks,percentage,grade)
    student_data[student_id] = [full_name, age, dob, student_class, subjects, marks,percentage,grade]
    print(f"Student {full_name} added successfully.")
    return new_student

def filter_students_by_class(students, student_class):
    return [student for student in students if student.student_class == student_class]

def filter_students_by_subject(students,subject):
    student_names = []
    for student in students:
        if subject in student.subjects:
            student_names.append(student.full_name)
    return ", ".join(student_names)

def filter_students_by_percentage(students,min_percentage):
    student_names = []
    for student in students:
        if min_percentage < student.percentage:
            student_names.append(student.full_name)
    return ", ".join(student_names)

def search_student_by_id(students, student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None

def update_student_record(student):
    print("Current Record: ")
    print(student)
    print("Enter new details (leave blank to keep current value):")
    student.age = int(input(f"Age ({student.age}): ") or student.age)
    student.dob = input(f"DOB ({student.dob}): ") or student.dob
    student.student_class = input(f"Class ({student.student_class}): ") or student.student_class
    subjects = input(f"Subjects ({', '.join(student.subjects)}): ")
    if subjects:
        student.subjects = [subject.strip() for subject in subjects.split(",")]
        marks = {}
        for subject in student.subjects:
            marks[subject] = int(input(f"Enter marks for {subject}: "))
        student.marks = marks
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)
    student_data[student.student_id] = [student.full_name, student.age, student.dob, student.student_class, student.subjects, student.marks,percentage,grade]
    print(f"Student {student.full_name}'s record updated successfully.")

def delete_student_record(student_id):
    if student_id in student_data:
        del student_data[student_id]
        print(f"Student with ID {student_id} deleted successfully.")
    else:
        print(f"Student with ID {student_id} not found.")

def calculate_class_average_percentage(students, student_class):
    filtered_students = filter_students_by_class(students, student_class)
    if not filtered_students:
        print(f"No students found in class {student_class}.")
        return
    total_percentage = sum(student.percentage for student in filtered_students)
    average_percentage = total_percentage / len(filtered_students)
    print(f"Average percentage for class {student_class}: {average_percentage:.2f}%")

def calculate_student_average_marks(student):
    average_marks = student.percentage
    print(f"Average marks for student {student.full_name} ({student.student_id}): {average_marks:.2f}")

def main():
    students = load_students(student_data)
    while True:
        print("1. Show all students")
        print("2. Add a student")
        print("3. Filter students by class")
        print("4. Filter students by subject")
        print("5. Filter students by percentage")
        print("6. Search for a student by ID")
        print("7. Update a student's record")
        print("8. Delete a student")
        print("9. Get average percentage of a class")
        print("10. Calculate average marks of a student")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_all_students(students)
        elif choice == '2':
            new_student = add_student()
        elif choice == '3':
            student_class = input("Enter Class to filter: ")
            filtered_students = filter_students_by_class(students, student_class)
            show_all_students(filtered_students)
        elif choice == '4':
            subject_name = input("Enter subject:")
            subject_name = subject_name.capitalize()
            print(filter_students_by_subject(students,subject_name))
        elif choice == '5':
            min_percentage = input("Enter the minimum percentage:")
            print(filter_students_by_percentage(students,min_percentage))
        elif choice == '6':
            student_id = input("Enter Student ID to search: ")
            student = search_student_by_id(students, student_id)
            if student:
                print(student)
            else:
                print(f"Student with ID {student_id} not found.")
        elif choice == '7':
            student_id = input("Enter Student ID to update: ")
            student = search_student_by_id(students, student_id)
            if student:
                update_student_record(student)
            else:
                print(f"Student with ID {student_id} not found.")
        elif choice == '8':
            student_id = input("Enter Student ID to delete: ")
            delete_student_record(student_id)
        elif choice == '9':
            student_class = input("Enter Class to calculate average percentage: ")
            calculate_class_average_percentage(students, student_class)
        elif choice == '10':
            student_id = input("Enter Student ID to calculate average marks: ")
            student = search_student_by_id(students, student_id)
            if student:
                calculate_student_average_marks(student)
            else:
                print(f"Student with ID {student_id} not found.")
        elif choice == '11':
            with open("updated_student_data.json", "w") as outfile:
                json.dump(student_data, outfile)
            print("Exiting the portal!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
