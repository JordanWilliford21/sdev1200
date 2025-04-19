#
# Name
# Date
# Population Database Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.
import sqlite3

def connect_db():
    return sqlite3.connect("cities.db")

def display_menu():
    print("\n--- City Population Database ---")
    print("1. Display cities sorted by population (ascending)")
    print("2. Display cities sorted by population (descending)")
    print("3. Display cities sorted by name")
    print("4. Display total population")
    print("5. Display average population")
    print("6. Display city with highest population")
    print("7. Display city with lowest population")
    print("0. Exit")

def fetch_and_display(query, description):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print(f"\n{description}")
        for row in rows:
            print(row)

def display_total_population():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(Population) FROM Cities")
        total = cursor.fetchone()[0]
        print(f"\nTotal Population: {total}")

def display_average_population():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT AVG(Population) FROM Cities")
        average = cursor.fetchone()[0]
        print(f"\nAverage Population: {average:.2f}")

def display_extreme_population(highest=True):
    with connect_db() as conn:
        cursor = conn.cursor()
        if highest:
            cursor.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1")
            label = "Highest"
        else:
            cursor.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1")
            label = "Lowest"
        city = cursor.fetchone()
        print(f"\n{label} Population City: {city[0]} ({city[1]})")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            fetch_and_display("SELECT CityName, Population FROM Cities ORDER BY Population ASC", "Cities by
