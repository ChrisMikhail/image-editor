from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
import interface


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


# Simulate keyboard events
def sim_draw():
    interface.window.event_generate('<Control-p>')
def sim_erase():
    interface.window.event_generate('<Control-e>')
def sim_red():
    interface.window.event_generate('<Control-R>')
def sim_green():
    interface.window.event_generate('<Control-G>')
def sim_blue():
    interface.window.event_generate('<Control-B>')
def sim_black():
    interface.window.event_generate('<Control-b>')
