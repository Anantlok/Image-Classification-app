import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
label = tk.Label(root, text="enter image address")
label.pack()
entry = tk.Entry(root)
entry.pack()

def get_input():
    user_input = entry.get()
    print("User input:", user_input)
    window = tk.Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()
    messagebox.showinfo('question', f'the subject of the image is {user_input}')

    window.deiconify()
    window.destroy()
    window.quit()

button = tk.Button(root, text="get input", command=get_input)
button.pack()
root.mainloop()




