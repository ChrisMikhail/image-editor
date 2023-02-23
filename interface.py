import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import functions

window = tk.Tk()
window.geometry("900x500")
window.title("Image Editor")
window.configure(bg='#252525')
canvas = Canvas(window, width=725, height=425).place(x=85, y=60)

title = Label(window, text="Image Editor", bg="#252525", font=("bold", 30), fg="white")
title.pack()
Button(window, text= "Select an Image", bg="#252525", fg="white", command=functions.open_file).place(x=405, y=242.5)

window.mainloop()

