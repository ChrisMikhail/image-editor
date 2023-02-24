from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import interface


def open_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    my_image = ImageTk.PhotoImage(Image.open(filename))
    my_image_label = Label(interface.canvas, image=my_image, anchor="nw")
    my_image_label.photo = my_image
    my_image_label.pack()

def resize_canvas(event):
    interface.canvas.config(width=event.width, height=event.height-50)

def erase_all():
    interface.canvas.delete("all")

def sim_enter():
    interface.window.event_generate('<Return>')

