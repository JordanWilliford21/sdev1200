#
# Name
# Date
# Name and Address Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program.  
# The code below was auto-generated. 
# Delete unnecessary code.

import tkinter as tk

class MyGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tk.Tk()

        # Create StringVar objects to display name,
        # street, and city-state-zip
        self.name_value = tk.StringVar()
        self.street_value = tk.StringVar()
        self.csz_value = tk.StringVar()

        # Create two frames
        self.info_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)

        # Create the label widgets, associated with the StringVar objects
        self.name_label = tk.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tk.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tk.Label(self.info_frame, textvariable=self.csz_value)

        # Pack the labels
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        # Create the button widgets
        self.show_info_button = tk.Button(self.button_frame, text='Show Info', command=self.show)
        self.quit_button = tk.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # Pack the buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        # Pack the frames
        self.info_frame.pack()
        self.button_frame.pack()

        # Enter the tkinter main loop
        self.main_window.mainloop()

    # Callback function for the show info button
    def show(self):
        self.name_value.set('Jordan Williford')
        self.street_value.set('1650 Stella CT')
        self.csz_value.set('Cody, Wyoming 82414')


# Creating instance of MyGUI class
my_gui = MyGUI()
