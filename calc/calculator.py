import tkinter as tk

def click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def clear():
    display.delete(0, tk.END)

def operation(op):
    first_number = display.get()
    global first_num
    global math_op
    first_num = int(first_number)
    math_op = op
    display.delete(0, tk.END)

def equals():
    second_number = display.get()
    display.delete(0, tk.END)
    if math_op == "+":
        display.insert(0, first_num + int(second_number))
    elif math_op == "-":
        display.insert(0, first_num - int(second_number))
    elif math_op == "*":
        display.insert(0, first_num * int(second_number))
    elif math_op == "/":
        display.insert(0, first_num / int(second_number))

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Number buttons
buttons = [
    (i, tk.Button(root, text=str(i), padx=40, pady=20, command=lambda i=i: click(i)))
    for i in range(1, 10)
]
buttons.append((0, tk.Button(root, text="0", padx=40, pady=20, command=lambda: click(0))))

# Arrange buttons like a telephone keypad
for i, btn in buttons:
    row = (9 - i) // 3 + 1
    col = (i - 1) % 3
    btn.grid(row=row, column=col)

# Operation buttons
btn_add = tk.Button(root, text="+", padx=39, pady=20, command=lambda: operation("+"))
btn_subtract = tk.Button(root, text="-", padx=41, pady=20, command=lambda: operation("-"))
btn_multiply = tk.Button(root, text="*", padx=40, pady=20, command=lambda: operation("*"))
btn_divide = tk.Button(root, text="/", padx=41, pady=20, command=lambda: operation("/"))
btn_equals = tk.Button(root, text="=", padx=91, pady=20, command=equals)
btn_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=clear)

# Place operation buttons
btn_add.grid(row=5, column=0)
btn_subtract.grid(row=6, column=0)
btn_multiply.grid(row=6, column=1)
btn_divide.grid(row=6, column=2)
btn_equals.grid(row=5, column=1, columnspan=2)
btn_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()
