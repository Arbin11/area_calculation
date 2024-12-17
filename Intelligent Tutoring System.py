import tkinter as tk
from math import pi
from tkinter import messagebox

# Create the main window
root = tk.Tk()
# root.iconbitmap("shapes.ico")  //
root.title("Math Intelligent Tutoring System - Area Calculations")
root.geometry("600x400")  # Set a fixed window size
root.resizable(True, True)  # Disable window resizing for consistency

# Centering function for all widgets
def center_widget(widget, frame, row, column, columnspan=1, padx=0, pady=0):
    widget.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky="nsew")
    frame.grid_columnconfigure(column, weight=2)

# Define functions for each shape's area calculation
def calculate_area():
    shape = shape_var.get()
    try:
        if shape == "Triangle":
            base = float(entry_base.get())
            height = float(entry_height.get())
            formula = f"Using Formula : 0.5 * base * height\n\nCalculating : 0.5 * {base} * {height}"
            area = 0.5 * base * height
        elif shape == "Square":
            side = float(entry_side.get())
            formula = f"Using Formula : (side_length)\u00b2\n\nCalculating : ({side})\u00b2"
            area = side ** 2
        elif shape == "Circle":
            radius = float(entry_radius.get())
            formula = f"Using Formula : \u03c0 * (radius)\u00b2\n\nCalculating : {pi:.6f} * ({radius})\u00b2"
            area = pi * radius ** 2
        else:
            area = None
        if area is not None:
            formula_label.config(text = formula)
            result_label.config(text=f"Calculated Area: {area:.2f}")
        else:
            messagebox.showerror("Error", "Please select a valid shape.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create frames for better organization and centering
top_frame = tk.Frame(root)
top_frame.pack(expand=True)
input_frame = tk.Frame(root)
input_frame.pack(expand=True)
result_frame = tk.Frame(root)
result_frame.pack(expand=True)

# Title label
title_label = tk.Label(top_frame, text="Area Calculation", font=("Times New Roman", 24, "bold"))
center_widget(title_label, top_frame, 0, 0, columnspan=2, pady=10)

# Create dropdown for shape selection
shape_var = tk.StringVar(value="Select Shape")
shape_label = tk.Label(input_frame, text="Shape:", font=("Times New Roman", 18, "bold"))
center_widget(shape_label, input_frame, 0, 0, padx=15,pady=5)
shape_dropdown = tk.OptionMenu(input_frame, shape_var, "Triangle", "Square", "Circle")
center_widget(shape_dropdown, input_frame, 0, 1, padx=15,pady=5)

# Input fields for dimensions
entry_base = tk.Entry(input_frame, width=10, text="12")
entry_height = tk.Entry(input_frame, width=10, text="5")
entry_side = tk.Entry(input_frame, width=10)
entry_radius = tk.Entry(input_frame, width=10)

# Display input fields based on selected shape
def update_fields(*args):
    for widget in input_frame.grid_slaves():
        if int(widget.grid_info()["row"]) > 0:
            widget.grid_forget()
    shape = shape_var.get()
    if shape == "Triangle":
        tk.Label(input_frame, text="Base:").grid(row=1, column=0, padx=5)
        entry_base.grid(row=1, column=1, padx=5)
        tk.Label(input_frame, text="Height:").grid(row=2, column=0, padx=5)
        entry_height.grid(row=2, column=1, padx=5)
    elif shape == "Square":
        tk.Label(input_frame, text="Side Length:").grid(row=1, column=0, padx=5)
        entry_side.grid(row=1, column=1, padx=5)
    elif shape == "Circle":
        tk.Label(input_frame, text="Radius:").grid(row=1, column=0, padx=5)
        entry_radius.grid(row=1, column=1, padx=5)

shape_var.trace("w", update_fields)

# Button to calculate area
calc_button = tk.Button(result_frame, text="Calculate Area", command=calculate_area, font=("Times New Roman", 12))
center_widget(calc_button, result_frame, 0, 0, pady=10)

# Label to display the result
formula_label = tk.Label(result_frame, text="", font=("Times New Roman", 12))
center_widget(formula_label, result_frame, 1, 0, pady=5)

# Label to display the result
result_label = tk.Label(result_frame, text="", font=("Times New Roman", 12))
center_widget(result_label, result_frame, 2, 0, pady=5)

# Run the application
root.mainloop()


# In[ ]:




