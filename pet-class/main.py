#
# Jordan Williford
# 2/7/2025
# Pet Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

import pet
#Get the pet's name, type, and age.
name = input("What is your pet's name?")
animal_type = input("What type of animal is that?")
age = input("How old is your pet?")

#Create and instance of the Pet class.
my_pet = pet.Pet(name, animal_type, age)

print("Here is the information you entered:")
print("Pet name:", my_pet.get_name())
print("Animal type:", my_pet.get_animal_type())
print("Age:",my_pet.get_age())

#Assign the values to the objects attributes.
my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)

#Display the pet data.
print("Here is the information you entered:")
print("Pet name:", my_pet.get_name())
print("Animal type:", my_pet.get_animal_type())
print("Age:", my_pet.get_age())