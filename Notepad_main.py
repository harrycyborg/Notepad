from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

# Create a Tkinter window
root = Tk()
root.title("Notepad")

# Set default filename
filename = None

# Define functions for file operations
def save_file():
    global filename
    if filename is None:
        filename = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        with open(filename, "w") as f:
            f.write(text_area.get("1.0", END))

def open_file():
    global filename
    filename = askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        with open(filename, "r") as f:
            text_area.delete("1.0", END)
            text_area.insert("1.0", f.read())

# Create a Text widget for text entry
text_area = Text(root, undo=True)
text_area.pack(expand=True, fill=BOTH)

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create an "Edit" menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=text_area.edit_undo)
edit_menu.add_command(label="Redo", command=text_area.edit_redo)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Start the Tkinter event loop
root.mainloop()
