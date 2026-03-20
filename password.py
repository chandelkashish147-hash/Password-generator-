import random
import string
import tkinter as tk
from tkinter import messagebox


# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())

        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4")
            return

        letters = string.ascii_letters
        digits = string.digits
        special = string.punctuation

        all_characters = letters + digits + special

        password = ''.join(random.choice(all_characters) for i in range(length))

        result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


# Create main window
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Password Generator Tool", font=("Arial", 16, "bold"))
title.pack(pady=15)

# Length input
label_length = tk.Label(root, text="Enter Password Length:")
label_length.pack()

entry_length = tk.Entry(root, width=20)
entry_length.pack(pady=5)

# Generate button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=15)

# Result
result_var = tk.StringVar()

result_label = tk.Label(root, text="Generated Password:", font=("Arial", 12))
result_label.pack()

result_entry = tk.Entry(root, textvariable=result_var, width=30, font=("Arial", 12), justify="center")
result_entry.pack(pady=10)

# Run GUI
root.mainloop()