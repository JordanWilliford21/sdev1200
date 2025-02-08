#
# Jordan Williford
# 2/7/2025
# Pet Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

class Pet:
    def __init__(self,name,animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
#The set_name method sets the pet's name.
    def set_name(self,name):
        self.__name = name
#The set_animal_type method sets the pet's type.
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
#The set_age method sets the pet's age.
    def set_age(self, age):
        self.__age = age
#The get_name method returns the pet's name. 
    def get_name(self):
        return self.__name
#The get_animal_type method returns the pet's type
    def get_animal_type(self):
        return self.__animal_type
#The get_age method returns the pet's age.
    def get_age(self):
        return self.__age