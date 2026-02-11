# Students Result based on tenth grade subjects
import csv

FILE_NAME = "students.csv"

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "Fail"

# Function to add student
def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")

    maths = int(input("Enter Maths Marks: "))
    science = int(input("Enter Science Marks: "))
    socialscience = int(input("Enter Social Science Marks: "))
    english = int(input("Enter English Marks: "))
    hindi = int(input("Enter Hindi Marks: "))

    total = maths + science + socialscience + english + hindi
    avg = total / 5
    grade = calculate_grade(avg)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, maths, science, socialscience, english, hindi, total, avg, grade])

    print("Student Added Successfully!")

# Function to view students
def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        print("\n----- Student Records -----")
        for row in reader:
            print(row)

# Main menu
def main():
    while True:
        print("\n===== Student Result System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice!")


main()