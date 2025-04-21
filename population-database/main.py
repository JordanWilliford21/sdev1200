import sqlite3

def display_menu():
    print("\nChoose an option:")
    print("1. Display cities sorted by population (ascending)")
    print("2. Display cities sorted by population (descending)")
    print("3. Display cities sorted by name")
    print("4. Display total population")
    print("5. Display average population")
    print("6. Display city with highest population")
    print("7. Display city with lowest population")
    print("8. Exit")

def display_results(results):
    for row in results:
        print(f"CityID: {row[0]}, CityName: {row[1]}, Population: {row[2]}")

def main():
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            cursor.execute("SELECT * FROM Cities ORDER BY Population ASC")
            display_results(cursor.fetchall())

        elif choice == '2':
            cursor.execute("SELECT * FROM Cities ORDER BY Population DESC")
            display_results(cursor.fetchall())

        elif choice == '3':
            cursor.execute("SELECT * FROM Cities ORDER BY CityName ASC")
            display_results(cursor.fetchall())

        elif choice == '4':
            cursor.execute("SELECT SUM(Population) FROM Cities")
            total = cursor.fetchone()[0]
            print(f"Total Population: {total}")

        elif choice == '5':
            cursor.execute("SELECT AVG(Population) FROM Cities")
            avg = cursor.fetchone()[0]
            print(f"Average Population: {avg:.2f}")

        elif choice == '6':
            cursor.execute("SELECT * FROM Cities ORDER BY Population DESC LIMIT 1")
            result = cursor.fetchone()
            print(f"City with Highest Population: CityName: {result[1]}, Population: {result[2]}")

        elif choice == '7':
            cursor.execute("SELECT * FROM Cities ORDER BY Population ASC LIMIT 1")
            result = cursor.fetchone()
            print(f"City with Lowest Population: CityName: {result[1]}, Population: {result[2]}")

        elif choice == '8':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

    conn.close()

if __name__ == "__main__":
    main()
