#
# Jordan Williford
# 4/6/2025
# Tree Age Programming Project
# SDEV 1200
#Tree age Project

# Use comments liberally throughout the program. 
import tkinter as tk

root = tk.Tk()
root.title("Tree Rings")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

center = 200
spacing = 20

for year in range(1, 6):
    r = year * spacing
    canvas.create_oval(center - r, center - r, center + r, center + r, outline="brown")
    canvas.create_text(center, center - r + 10, text=str(year), fill="green", font=("Arial", 10, "bold"))

root.mainloop()
