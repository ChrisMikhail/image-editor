import tkinter as tk
from tkinter import *
import functions
import MouseTracker


# Window
window = tk.Tk()
window.geometry("900x500")
window.title("Image Editor")
window.configure(bg='#252525')
window.update_idletasks() 


# Canvas
canvas = tk.Canvas(window, width=725, height=425)
canvas.pack(fill="both", expand=True)
tracker = MouseTracker.MouseTracker(canvas)


# Buttons
selectImg = Button(window, text= "Select an Image", bg="#252525", fg="white", command=functions.open_file)
selectImg.pack(padx=3, pady=5, side=tk.LEFT)

draw = Button(window, text= "Draw", bg="#252525", fg="white", command=functions.sim_enter)
draw.pack(padx=3, pady=5, side=tk.LEFT)

# eraser = Button(window, text= "Erase", bg="#252525", fg="white", command="")
# eraser.pack(padx=3, side=tk.LEFT)

eraseAll = Button(window, text= "Erase All", bg="#252525", fg="white", command=functions.erase_all)
eraseAll.pack(padx=3, pady=5, side=tk.LEFT)

# addText = Button(window, text= "Add Text", bg="#252525", fg="white", command=functions.type_words)
# addText.pack(padx=3, side=tk.LEFT)

# downloadImg = Button(window, text= "Download", bg="#252525", fg="white", command="")
# downloadImg.pack(padx=3, side=tk.LEFT)


window.bind("<Configure>", functions.resize_canvas)
window.mainloop()


