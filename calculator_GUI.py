import tkinter as tk

def calculate():
    try:
        num1 = int(num1_entry.get())
        num2 = int(num2_entry.get())
    except ValueError:
        result_label.config(text="Invalid input, please enter valid numbers")
        return

    operation = operation_var.get()
    if operation == "1":
        result = num1 + num2
    elif operation == "2":
        result = num1 - num2
    elif operation == "3":
        result = num1 * num2
    elif operation == "4":
        if num2!= 0:
            result = num1 / num2
        else:
            result_label.config(text="Error: Division by zero is not allowed")
            return

    result_label.config(text=f"The result is: {result}")

def clear():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Calculator")

operation_var = tk.StringVar()
operation_var.set("1")

operation_label = tk.Label(root, text="Select an operation:")
operation_label.pack()

operation_frame = tk.Frame(root)
operation_frame.pack()

addition_radio = tk.Radiobutton(operation_frame, text="Addition", variable=operation_var, value="1")
addition_radio.pack(side=tk.LEFT)

subtraction_radio = tk.Radiobutton(operation_frame, text="Subtraction", variable=operation_var, value="2")
subtraction_radio.pack(side=tk.LEFT)

multiplication_radio = tk.Radiobutton(operation_frame, text="Multiplication", variable=operation_var, value="3")
multiplication_radio.pack(side=tk.LEFT)

division_radio = tk.Radiobutton(operation_frame, text="Division", variable=operation_var, value="4")
division_radio.pack(side=tk.LEFT)

num1_label = tk.Label(root, text="Enter Num1:")
num1_label.pack()
num1_entry = tk.Entry(root)
num1_entry.pack()

num2_label = tk.Label(root, text="Enter Num2:")
num2_label.pack()
num2_entry = tk.Entry(root)
num2_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()