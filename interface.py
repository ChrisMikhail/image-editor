import tkinter as tk
from tkinter import *
import functions
import MouseTracker


# Window
window = tk.Tk()
window.geometry("900x500")
window.title("Image Editor")
window.configure(bg='#252525')


# Canvas
canvas = tk.Canvas(window, width=725, height=425)
canvas.pack(fill="both", expand=True)

# Title
title = Label(window, text="Image Editor", bg="#252525", font=("bold", 30), fg="white")
title.pack()


# Buttons
selectImg = Button(window, text= "Select an Image", bg="#252525", fg="white", command=functions.open_file)
selectImg.pack()

draw = Button(window, text= "Erase All", bg="#252525", fg="white", command="")
draw.pack()

tracker = MouseTracker.MouseTracker(canvas)
window.bind("<Configure>", functions.resize_canvas)
window.mainloop()


