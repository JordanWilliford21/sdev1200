#
# Jordan Williford
# 3/8/2025
# Plant Information Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 
class Plant:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def print_info(self):
        print(f"Plant Information:")
        print(f"   Plant name: {self.name}")
        print(f"   Cost: {self.cost}")

class Flower(Plant):
    def __init__(self, name, cost, has_fragrance, color):
        super().__init__(name, cost)
        self.has_fragrance = has_fragrance
        self.color = color

    def print_info(self):
        print(f"Flower Information:")
        print(f"   Flower name: {self.name}")
        print(f"   Cost: {self.cost}")
        print(f"   Has fragrance: {'Yes' if self.has_fragrance else 'No'}")
        print(f"   Color: {self.color}")

def print_list(garden):
    for index, item in enumerate(garden, 1):
        print(f"\nPlant {index} Information:")
        item.print_info()

def main():
    my_garden = []

    while True:
        print("\nEnter a plant or flower (or -1 to stop):")
        plant_type = input("Is it a plant or a flower? (plant/flower): ").strip().lower()

        if plant_type == '-1':
            break
        
        if plant_type == 'plant':
            name = input("Enter the name of the plant: ").strip()
            cost = float(input("Enter the cost of the plant: ").strip())
            print(f"You entered: Plant name = {name}, Cost = {cost}")
            new_plant = Plant(name, cost)
            my_garden.append(new_plant)

        elif plant_type == 'flower':
            name = input("Enter the name of the flower: ").strip()
            cost = float(input("Enter the cost of the flower: ").strip())
            has_fragrance = input("Does the flower have fragrance? (true/false): ").strip().lower() == 'true'
            color = input("Enter the color of the flower: ").strip()
            print(f"You entered: Flower name = {name}, Cost = {cost}, Has fragrance = {has_fragrance}, Color = {color}")
            new_flower = Flower(name, cost, has_fragrance, color)
            my_garden.append(new_flower)

        else:
            print("Invalid input. Please enter 'plant' or 'flower'.")

    print("\nHere is the list of plants and flowers in your garden:")
    print_list(my_garden)

if __name__ == "__main__":
    main()
