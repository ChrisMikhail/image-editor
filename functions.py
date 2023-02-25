from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import interface
import tkinter as tk



def open_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    my_image = ImageTk.PhotoImage(Image.open(filename))
    image_id = interface.canvas.create_image(0, 0, image=my_image, anchor="nw")
    interface.canvas.lower(image_id)
    interface.canvas.image = my_image


def resize_canvas(event):
    interface.canvas.config(width=event.width, height=event.height-50)


def erase_all():
    interface.canvas.delete("all")


def sim_enter():
    interface.window.event_generate('<Return>')


# def type_words():
#     box = tk.Entry(interface.canvas)
    
