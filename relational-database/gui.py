import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

DB_NAME = 'student_info.db'

# ---------- Database Setup ----------
def connect_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

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

# ---------- GUI ----------
class StudentDBApp:
    def __init__(self, root):
        self.root = root
        self.root.title("College Student Information System")
        self.root.geometry("700x500")
        
        tab_control = ttk.Notebook(root)
        
        self.majors_tab = ttk.Frame(tab_control)
        self.departments_tab = ttk.Frame(tab_control)
        self.students_tab = ttk.Frame(tab_control)
        
        tab_control.add(self.majors_tab, text="Majors")
        tab_control.add(self.departments_tab, text="Departments")
        tab_control.add(self.students_tab, text="Students")
        
        tab_control.pack(expand=1, fill="both")

        self.build_majors_tab()
        self.build_departments_tab()
        self.build_students_tab()

    # ----- Majors Tab -----
    def build_majors_tab(self):
        frame = self.majors_tab

        tk.Label(frame, text="Major Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.major_name_entry = tk.Entry(frame)
        self.major_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(frame, text="Add Major", command=self.add_major).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(frame, text="Delete Selected", command=self.delete_major).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(frame, text="Refresh", command=self.refresh_majors).grid(row=2, column=2, padx=5, pady=5)

        self.majors_tree = ttk.Treeview(frame, columns=("ID", "Name"), show="headings")
        self.majors_tree.heading("ID", text="ID")
        self.majors_tree.heading("Name", text="Name")
        self.majors_tree.grid(row=1, column=0, columnspan=2, rowspan=5, padx=5, pady=5, sticky="nsew")

        frame.rowconfigure(5, weight=1)
        frame.columnconfigure(1, weight=1)

        self.refresh_majors()

    def add_major(self):
        name = self.major_name_entry.get()
        if not name:
            messagebox.showwarning("Input Error", "Please enter a major name.")
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Majors (Name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
        self.refresh_majors()
        self.major_name_entry.delete(0, tk.END)

    def delete_major(self):
        selected = self.majors_tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a major to delete.")
            return
        item = self.majors_tree.item(selected)
        major_id = item['values'][0]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Majors WHERE MajorID=?", (major_id,))
        conn.commit()
        conn.close()
        self.refresh_majors()

    def refresh_majors(self):
        for row in self.majors_tree.get_children():
            self.majors_tree.delete(row)
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Majors")
        for row in cursor.fetchall():
            self.majors_tree.insert('', tk.END, values=row)
        conn.close()

    # ----- Departments Tab -----
    def build_departments_tab(self):
        frame = self.departments_tab

        tk.Label(frame, text="Department Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.department_name_entry = tk.Entry(frame)
        self.department_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(frame, text="Add Department", command=self.add_department).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(frame, text="Delete Selected", command=self.delete_department).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(frame, text="Refresh", command=self.refresh_departments).grid(row=2, column=2, padx=5, pady=5)

        self.departments_tree = ttk.Treeview(frame, columns=("ID", "Name"), show="headings")
        self.departments_tree.heading("ID", text="ID")
        self.departments_tree.heading("Name", text="Name")
        self.departments_tree.grid(row=1, column=0, columnspan=2, rowspan=5, padx=5, pady=5, sticky="nsew")

        frame.rowconfigure(5, weight=1)
        frame.columnconfigure(1, weight=1)

        self.refresh_departments()

    def add_department(self):
        name = self.department_name_entry.get()
        if not name:
            messagebox.showwarning("Input Error", "Please enter a department name.")
            return
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Departments (Name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
        self.refresh_departments()
        self.department_name_entry.delete(0, tk.END)

    def delete_department(self):
        selected = self.departments_tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a department to delete.")
            return
        item = self.departments_tree.item(selected)
        dept_id = item['values'][0]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Departments WHERE DeptID=?", (dept_id,))
        conn.commit()
        conn.close()
        self.refresh_departments()

    def refresh_departments(self):
        for row in self.departments_tree.get_children():
            self.departments_tree.delete(row)
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Departments")
        for row in cursor.fetchall():
            self.departments_tree.insert('', tk.END, values=row)
        conn.close()

    # ----- Students Tab -----
    def build_students_tab(self):
        frame = self.students_tab

        tk.Label(frame, text="Student Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.student_name_entry = tk.Entry(frame)
        self.student_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Select Major:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.major_combo = ttk.Combobox(frame, state="readonly")
        self.major_combo.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Select Department:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.department_combo = ttk.Combobox(frame, state="readonly")
        self.department_combo.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(frame, text="Add Student", command=self.add_student).grid(row=3, column=2, padx=5, pady=5)
        tk.Button(frame, text="Delete Selected", command=self.delete_student).grid(row=4, column=2, padx=5, pady=5)
        tk.Button(frame, text="Refresh", command=self.refresh_students).grid(row=5, column=2, padx=5, pady=5)

        self.students_tree = ttk.Treeview(frame, columns=("ID", "Name", "Major", "Department"), show="headings")
        self.students_tree.heading("ID", text="ID")
        self.students_tree.heading("Name", text="Name")
        self.students_tree.heading("Major", text="Major")
        self.students_tree.heading("Department", text="Department")
        self.students_tree.grid(row=3, column=0, columnspan=2, rowspan=5, padx=5, pady=5, sticky="nsew")

        frame.rowconfigure(8, weight=1)
        frame.columnconfigure(1, weight=1)

        self.refresh_students()

    def add_student(self):
        name = self.student_name_entry.get()
        major = self.major_combo.get()
        department = self.department_combo.get()
        if not name or not major or not department:
            messagebox.showwarning("Input Error", "Please fill out all fields.")
            return

        major_id = self.major_ids.get(major)
        dept_id = self.department_ids.get(department)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Students (Name, MajorID, DeptID) VALUES (?, ?, ?)",
            (name, major_id, dept_id)
        )
        conn.commit()
        conn.close()
        self.refresh_students()
        self.student_name_entry.delete(0, tk.END)

    def delete_student(self):
        selected = self.students_tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a student to delete.")
            return
        item = self.students_tree.item(selected)
        student_id = item['values'][0]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Students WHERE StudentID=?", (student_id,))
        conn.commit()
        conn.close()
        self.refresh_students()

    def refresh_students(self):
        # Refresh table
        for row in self.students_tree.get_children():
            self.students_tree.delete(row)
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT s.StudentID, s.Name, m.Name, d.Name
            FROM Students s
            JOIN Majors m ON s.MajorID = m.MajorID
            JOIN Departments d ON s.DeptID = d.DeptID
        ''')
        for row in cursor.fetchall():
            self.students_tree.insert('', tk.END, values=row)

        # Refresh dropdowns
        cursor.execute("SELECT MajorID, Name FROM Majors")
        majors = cursor.fetchall()
        self.major_ids = {name: mid for mid, name in majors}
        self.major_combo['values'] = list(self.major_ids.keys())

        cursor.execute("SELECT DeptID, Name FROM Departments")
        departments = cursor.fetchall()
        self.department_ids = {name: did for did, name in departments}
        self.department_combo['values'] = list(self.department_ids.keys())

        conn.close()

# ---------- Main ----------
if __name__ == "__main__":
    create_tables()
    root = tk.Tk()
    app = StudentDBApp(root)
    root.mainloop()
