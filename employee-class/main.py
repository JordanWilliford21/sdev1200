#
# Jordan Williford
# 2/9/2025
# Employee Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.
class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

# Employee Objects
luke = Employee("Luke Skywalker",47899,"Traning", "Jedi Master")
hulk = Employee("The Hulk", 39119, "Contruction", "Demolition Worker")
bullwinkle = Employee("Bullwinkle Moose", 81774, "Animation", "Cartoon Character")

#Display the Info
print("Employee: ", luke.name)
print("ID Number:", luke.id_number)
print("Department:", luke.department)
print("Job Title:", luke.job_title, "\n")

print("Employee: ", hulk.name)
print("ID Number:", hulk.id_number)
print("Department:", hulk.department)
print("Job Title:", hulk.job_title, "\n")

print("Employee: ", bullwinkle.name)
print("ID Number:", bullwinkle.id_number)
print("Department:", bullwinkle.department)
print("Job Title:", bullwinkle.job_title)