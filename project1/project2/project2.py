import random
import string
#Importing for displaying password later.
from tkinter import messagebox

#Using the "String" module to generate the acceptable characters
char = string.digits + string.ascii_letters + string.punctuation

#User Input for Length of Desired Password
passwdLeng = int(input("Length of Password: "))

#Declaring passwd variable for later 
passwd = ""

#Forloop to generate the password
for i in range(passwdLeng):
    passwd = passwd + random.choice(char)

messagebox.showinfo("Not A Password", passwd)