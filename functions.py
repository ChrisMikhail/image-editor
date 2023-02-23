from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import interface

def open_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    my_image = ImageTk.PhotoImage(Image.open(filename))
    my_image_label = Label(interface.canvas, image=my_image)
    my_image_label.photo = my_image
    my_image_label.pack()   

