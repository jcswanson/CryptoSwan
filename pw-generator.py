import random
import string
import pyperclip
import tkinter as tk

# create the main window
root = tk.Tk()
root.title("CryptoSwan Password Generator")
root.geometry("400x400")
root.resizable(0, 0)



# start definition of functions
# function randomizes and generates password
def generate_password():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(password_characters)
                       for i in range(password_length))
    password_output.delete(0, tk.END)
    password_output.insert(0, password)


# copy password to clipboard
def copy_password():
    password = password_output.get()
    pyperclip.copy(password)


# quits program
def exit_generator():
    root.destroy()

# add widgets to the root window
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root, width=20)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_output = tk.Entry(root, width=40)
password_output.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_password)
copy_button.pack()

author_label = tk.Label(root, text="John Swanson | CYBER 100 | 4/27/23", font='arial 18 bold')
author_label.pack(side='bottom')

# run the main loop
root.mainloop()
