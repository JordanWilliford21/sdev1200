#
# Jordan Williford
# 4/6/2025
# Property Tax Programming Project
# SDEV 1200
#Property Tax Project 

# Use comments liberally throughout the program. 
import tkinter as tk

def calculate():
    try:
        value = float(entry.get())
        assessment = value * 0.6
        tax = (assessment / 100) * 0.75
        result_label.config(text=f"Assessment: ${assessment:.2f}\nTax: ${tax:.2f}")
    except ValueError:
        result_label.config(text="Enter a valid number.")

# GUI Setup
window = tk.Tk()
window.title("Property Tax Calculator")
window.geometry("300x200")

tk.Label(window, text="Actual Property Value:").pack(pady=5)
entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="Calculate", command=calculate).pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
