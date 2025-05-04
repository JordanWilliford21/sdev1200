#
# Name
# Date
# Relational Database Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.
import sqlite3

# Initialize and connect to the database
def connect_db():
    conn = sqlite3.connect('student_info.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

# Create tables
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Majors (
            MajorID INTEGER PRIMARY KEY,
            Name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Departments (
            DeptID INTEGER PRIMARY KEY,
            Name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY,
            Name TEXT,
            MajorID INTEGER,
            DeptID INTEGER,
            FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
            FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
        )
    ''')

    conn.commit()
    conn.close()
    print("Tables created successfully.")

# ---------------- Majors CRUD ----------------
def add_major(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Majors (Name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    print("Major added successfully.")

def search_major(major_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Majors WHERE MajorID=?", (major_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def update_major(major_id, new_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Majors SET Name=? WHERE MajorID=?", (new_name, major_id))
    conn.commit()
    conn.close()
    print("Major updated successfully.")

def delete_major(major_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Majors WHERE MajorID=?", (major_id,))
    conn.commit()
    conn.close()
    print("Major deleted successfully.")

def list_majors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Majors")
    results = cursor.fetchall()
    conn.close()
    return results

# ---------------- Departments CRUD ----------------
def add_department(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Departments (Name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    print("Department added successfully.")

def search_department(dept_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Departments WHERE DeptID=?", (dept_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def update_department(dept_id, new_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Departments SET Name=? WHERE DeptID=?", (new_name, dept_id))
    conn.commit()
    conn.close()
    print("Department updated successfully.")

def delete_department(dept_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Departments WHERE DeptID=?", (dept_id,))
    conn.commit()
    conn.close()
    print("Department deleted successfully.")

def list_departments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Departments")
    results = cursor.fetchall()
    conn.close()
    return results

# ---------------- Students CRUD ----------------
def add_student(name, major_id, dept_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Students (Name, MajorID, DeptID) VALUES (?, ?, ?)",
        (name, major_id, dept_id)
    )
    conn.commit()
    conn.close()
    print("Student added successfully.")

def search_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE StudentID=?", (student_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def update_student(student_id, new_name, new_major_id, new_dept_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Students SET Name=?, MajorID=?, DeptID=? WHERE StudentID=?",
        (new_name, new_major_id, new_dept_id, student_id)
    )
    conn.commit()
    conn.close()
    print("Student updated successfully.")

def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE StudentID=?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully.")

def list_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.StudentID, s.Name, m.Name AS Major, d.Name AS Department
        FROM Students s
        JOIN Majors m ON s.MajorID = m.MajorID
        JOIN Departments d ON s.DeptID = d.DeptID
    ''')
    results = cursor.fetchall()
    conn.close()
    return results

# ---------------- Menu ----------------
def main():
    create_tables()
    while True:
        print("\nChoose an option:")
        print("1. Manage Majors")
        print("2. Manage Departments")
        print("3. Manage Students")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            manage_majors()
        elif choice == '2':
            manage_departments()
        elif choice == '3':
            manage_students()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def manage_majors():
    while True:
        print("\nMajors Menu:")
        print("1. Add Major")
        print("2. Search Major")
        print("3. Update Major")
        print("4. Delete Major")
        print("5. List Majors")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter major name: ")
            add_major(name)
        elif choice == '2':
            major_id = int(input("Enter major ID: "))
            print(search_major(major_id))
        elif choice == '3':
            major_id = int(input("Enter major ID: "))
            new_name = input("Enter new name: ")
            update_major(major_id, new_name)
        elif choice == '4':
            major_id = int(input("Enter major ID: "))
            delete_major(major_id)
        elif choice == '5':
            majors = list_majors()
            for m in majors:
                print(m)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def manage_departments():
    while True:
        print("\nDepartments Menu:")
        print("1. Add Department")
        print("2. Search Department")
        print("3. Update Department")
        print("4. Delete Department")
        print("5. List Departments")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter department name: ")
            add_department(name)
        elif choice == '2':
            dept_id = int(input("Enter department ID: "))
            print(search_department(dept_id))
        elif choice == '3':
            dept_id = int(input("Enter department ID: "))
            new_name = input("Enter new name: ")
            update_department(dept_id, new_name)
        elif choice == '4':
            dept_id = int(input("Enter department ID: "))
            delete_department(dept_id)
        elif choice == '5':
            departments = list_departments()
            for d in departments:
                print(d)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def manage_students():
    while True:
        print("\nStudents Menu:")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. List Students")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            print("Available Majors:")
            majors = list_majors()
            for m in majors:
                print(m)
            major_id = int(input("Enter major ID: "))

            print("Available Departments:")
            departments = list_departments()
            for d in departments:
                print(d)
            dept_id = int(input("Enter department ID: "))

            add_student(name, major_id, dept_id)
        elif choice == '2':
            student_id = int(input("Enter student ID: "))
            print(search_student(student_id))
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            new_name = input("Enter new name: ")

            print("Available Majors:")
            majors = list_majors()
            for m in majors:
                print(m)
            new_major_id = int(input("Enter new major ID: "))

            print("Available Departments:")
            departments = list_departments()
            for d in departments:
                print(d)
            new_dept_id = int(input("Enter new department ID: "))

            update_student(student_id, new_name, new_major_id, new_dept_id)
        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            delete_student(student_id)
        elif choice == '5':
            students = list_students()
            for s in students:
                print(s)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
