import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window size and position
root.geometry("500x500+100+100")

# Load the image file
image = tk.PhotoImage(file="desktop/python game/python_game/page1/Ben.jpg")

# Create a label with the image as the background
background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add other widgets to the window as needed

# Start the main event loop
root.mainloop()
