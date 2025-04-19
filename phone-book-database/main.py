#
# Name
# Date
# Phone Book Database Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.
import sqlite3

def connect_db():
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Entries (
            Name TEXT PRIMARY KEY,
            Phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn

def add_entry(conn):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    try:
        conn.execute("INSERT INTO Entries (Name, Phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("Entry added.")
    except sqlite3.IntegrityError:
        print("Entry already exists. Try updating instead.")

def lookup_entry(conn):
    name = input("Enter name to look up: ")
    cursor = conn.execute("SELECT Phone FROM Entries WHERE Name = ?", (name,))
    result = cursor.fetchone()
    if result:
        print(f"{name}'s phone number is {result[0]}")
    else:
        print("Entry not found.")

def update_entry(conn):
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")
    cursor = conn.execute("UPDATE Entries SET Phone = ? WHERE Name = ?", (new_phone, name))
    if cursor.rowcount == 0:
        print("Entry not found.")
    else:
        conn.commit()
        print("Entry updated.")

def delete_entry(conn):
    name = input("Enter name to delete: ")
    cursor = conn.execute("DELETE FROM Entries WHERE Name = ?", (name,))
    if cursor.rowcount == 0:
        print("Entry not found.")
    else:
        conn.commit()
        print("Entry deleted.")

def display_menu():
    print("\n--- Phonebook Menu ---")
    print("1. Add new entry")
    print("2. Look up a number")
    print("3. Update a number")
    print("4. Delete an entry")
    print("0. Exit")

def main():
    conn = connect_db()
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            add_entry(conn)
        elif choice == "2":
            lookup_entry(conn)
        elif choice == "3":
            update_entry(conn)
        elif choice == "4":
            delete_entry(conn)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
