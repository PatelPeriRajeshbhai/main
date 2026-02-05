import json
import os

FILE_NAME = "students.json"

def load_data():
    
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
   
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_student(name, roll_num, marks, grade):
   
    data = load_data()

    for student in data:
        if student["roll_number"] == roll_num:
            print("Student with this roll number already exists!")
            return

    student = {
        "name": name,
        "roll_number": roll_num,
        "marks": marks,
        "grade": grade
    }

    data.append(student)
    save_data(data)
    print("Student added successfully!")


def search_student(roll_num):
    
    data = load_data()
    for student in data:
        if student["roll_number"] == roll_num:
            return student
    return None


def update_marks(roll_num, new_marks):
    
    data = load_data()
    for student in data:
        if student["roll_number"] == roll_num:
            student["marks"] = new_marks
            save_data(data)
            print("Marks updated successfully!")
            return
    print("Student not found!")


def delete_student(roll_num):
    
    data = load_data()
    new_data = [s for s in data if s["roll_number"] != roll_num]

    if len(new_data) == len(data):
        print("Student not found!")
    else:
        save_data(new_data)
        print("Student deleted successfully!")


def display_all():
    
    data = load_data()
    if not data:
        print("No student records found.")
        return

    print("\n---- All Students ----")
    for student in data:
        print(f"Name: {student['name']}, Roll: {student['roll_number']}, Marks: {student['marks']}, Grade: {student['grade']}")
    print("----------------------\n")


def calculate_average():
    
    data = load_data()
    if not data:
        print("No student data available to calculate average.")
        return

    avg = sum(student["marks"] for student in data) / len(data)
    print(f"Class Average Marks: {avg:.2f}")

add_student("Alice", 1, 85, "A")
add_student("Bob", 2, 76, "B")
print(search_student(1))
update_marks(1, 90)
delete_student(2)
display_all()
calculate_average()
