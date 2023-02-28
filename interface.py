import tkinter as tk
from tkinter import *
import functions
from MouseTracker import MouseTracker


# Window
window = tk.Tk()
window.geometry("900x500")
window.title("Image Editor")
window.configure(bg='#252525')
window.update_idletasks() 


# Canvas
canvas = tk.Canvas(window, width=725, height=425)
canvas.pack(fill="both", expand=True)
tracker = MouseTracker(canvas)


# Buttons
selectImg = Button(window, text= "Select an Image", bg="#252525", fg="white", command=functions.open_file)
selectImg.pack(padx=3, pady=5, side=tk.LEFT)

draw = Button(window, text= "Draw", bg="#252525", fg="white", command=functions.sim_draw)
draw.pack(padx=3, pady=5, side=tk.LEFT)

eraser = Button(window, text= "Erase", bg="#252525", fg="white", command=functions.sim_erase)
eraser.pack(padx=3, side=tk.LEFT)

clearScreen = Button(window, text= "Clear Canvas", bg="#252525", fg="white", command=functions.erase_all)
clearScreen.pack(padx=3, pady=5, side=tk.LEFT)

black = Button(window, bg="black",  width=2, command=functions.sim_black)
black.pack(padx=3, pady=5, side=tk.LEFT)

red = Button(window, bg="red", width=2, command=functions.sim_red)
red.pack(padx=3, pady=5, side=tk.LEFT)

green = Button(window, bg="green",  width=2, command=functions.sim_green)
green.pack(padx=3, pady=5, side=tk.LEFT)

blue = Button(window, bg="blue",  width=2, command=functions.sim_blue)
blue.pack(padx=3, pady=5, side=tk.LEFT)

# downloadImg = Button(window, text= "Download", bg="#252525", fg="white", command=functions.download_img)
# downloadImg.pack(padx=3, side=tk.LEFT)


window.bind("<Configure>", functions.resize_canvas)
window.mainloop()


