import tkinter as tk
from tkinter import messagebox

# FUNCTION TO WORK
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Set up the GUI window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x200")

# Create Entry widgets for numbers
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Create Label for result
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=5)

# Create Buttons for operations
button_add = tk.Button(root, text="+", command=lambda: calculate('+'))
button_add.pack(pady=5)
button_subtract = tk.Button(root, text="-", command=lambda: calculate('-'))
button_subtract.pack(pady=5)
button_multiply = tk.Button(root, text="*", command=lambda: calculate('*'))
button_multiply.pack(pady=5)
button_divide = tk.Button(root, text="/", command=lambda: calculate('/'))
button_divide.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
 
