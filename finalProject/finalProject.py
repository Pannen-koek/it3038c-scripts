import random
import string
import tkinter as tk
from tkinter import messagebox

#Creating GUI Window
root = tk.Tk()

#Set Title and Size of Window
root.title('Final Project Cooper')
root.geometry("400x200")

#Setting global passwd variable
passwd = ""

#Function to Generate Passwords
def generate_password():
    
    char = string.digits + string.ascii_letters + string.punctuation
    passwdLeng = int(entry_length.get())
    passwd_entry.delete(0, passwdLeng)
    passwd = ""
    for i in range(passwdLeng):
        passwd = passwd + random.choice(char)
    passwd_entry.insert(0, passwd)

#Creating the password length label and entry box
label_length = tk.Label(root, text = "Password Length:")
label_length.pack()
entry_length = tk.Entry(root)
entry_length.pack()

#Creating the generate password button
button_generate = tk.Button(root, text = "Generate Password", command = generate_password)
button_generate.pack()

#Creating the generated password text box
label_length = tk.Label(root, text = "Generated Password:")
label_length.pack(pady=10)
passwd_entry = tk.Entry(root)
passwd_entry.pack()



root.mainloop()
