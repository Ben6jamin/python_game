# Import necessary modules
import tkinter as tk
from tkinter import ttk

# Create a window
root = tk.Tk()
root.geometry("400x300")
root.title("Welcome to My Application")

# Create a label for the title
title_label = ttk.Label(root, text="Welcome to My Application!", font=("Helvetica", 18))
title_label.pack(pady=20)

# Create a label for the description
description_label = ttk.Label(root, text="This is a simple Python application created to showcase a welcoming page.", font=("Helvetica", 12))
description_label.pack(pady=10)



def login():
    username = username_entry.get()
    password = password_entry.get()
    # Add code to check if username and password are correct
    # If correct, proceed to main program
    # If incorrect, display error message



# Create labels and entry widgets
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)
password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*")
login_button = tk.Button(root, text="Login", command=login)

# Add labels and entry widgets to window
username_label.pack()
username_entry.pack()


password_label.pack()
password_entry.pack()
login_button.pack()



# Create a button to close the window
close_button = ttk.Button(root, text="Close", command=root.destroy)
close_button.pack(pady=200)

# set the background color
root.configure(background='blue')

# Run the window
root.mainloop()
