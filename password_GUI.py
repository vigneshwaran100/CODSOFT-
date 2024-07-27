import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    """Generate a strong password of the given length."""
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def generate_and_display_password():
    """Generate a password and display it in the GUI."""
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        if password is not None:
            password_label.config(text=f"Generated Strong Password:")
            password_text.delete(1.0, tk.END)
            password_text.insert(tk.END, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create the length label and entry
length_label = tk.Label(root, text="Enter length of the password:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Create the generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

# Create the password label and text box
password_label = tk.Label(root, text="")
password_label.pack()
password_text = tk.Text(root, height=1, width=40)
password_text.pack()

# Start the GUI event loop
root.mainloop()