from tkinter import filedialog
from PIL import ImageTk, Image
import interface


images = []


def open_file(event):
    filename = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    if len(filename) > 1:
        my_image = ImageTk.PhotoImage(Image.open(filename))
        images.append(my_image)
        chosen_img = interface.canvas.create_image(0, 0, image=my_image, anchor="nw")
        interface.canvas.image = chosen_img

def resize_canvas(event):
    interface.canvas.config(width=event.width, height=event.height-50)


def erase_all(event):
    interface.canvas.delete("all")


# Simulate keyboard events
def sim_open():
    interface.window.event_generate("<Control-o>")
def sim_eraseAll():
    interface.window.event_generate("<Control-D>")
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

def update_brush_size(val):
    interface.brushSizeValue.set(int(val))
    interface.max_label.config(text=f"Brush Size: {interface.brushSizeValue.get()}")