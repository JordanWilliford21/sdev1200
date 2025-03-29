#
# Jordan Williford
# 3/28/2025
# Joe's Automotive Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program.  
# The code below was auto-generated. 
# Delete/adjust unnecessary code.

import tkinter as tk
from tkinter import messagebox

# Prices of the services
services = {
    "Oil change": 30.00,
    "Lube job": 20.00,
    "Radiator flush": 40.00,
    "Transmission flush": 100.00,
    "Inspection": 35.00,
    "Muffler replacement": 200.00,
    "Tire rotation": 20.00
}

def calculate_total():
    total = 0.0
    # Loop through each checkbutton and add its corresponding price if it's selected
    for service, var in check_vars.items():
        if var.get() == 1:
            total += services[service]
    
    total_label.config(text=f"Total Charges: ${total:.2f}")

# Create the main window
root = tk.Tk()
root.title("Joe's Automotive Maintenance Services")

# Create a dictionary to store the checkbutton variables
check_vars = {}

# Create checkbuttons for each service
for service in services:
    var = tk.IntVar()
    check_vars[service] = var
    tk.Checkbutton(root, text=f"{service} - ${services[service]:.2f}", variable=var, command=calculate_total).pack()

# Label to display the total charges
total_label = tk.Label(root, text="Total Charges: $0.00")
total_label.pack()

# Run the GUI event loop
root.mainloop()
