import random
import string
import tkinter as tk
from tkinter import messagebox

# Creating the main window
root = tk.Tk()
root.title("Password Generator")

# Function to generate a random password
def generate_password():
    char = string.digits + string.ascii_letters + string.punctuation
    passwdLeng = int(entry_length.get())
    passwd = ""
    for i in range(passwdLeng):
        passwd = passwd + random.choice(char)
    messagebox.showinfo("Generated Password", passwd)

# Creating the password length label and entry widget
label_length = tk.Label(root, text="Password Length:")
label_length.pack()
entry_length = tk.Entry(root)
entry_length.pack()

# Creating the generate password button
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack()

# Running the main loop
root.mainloop()
