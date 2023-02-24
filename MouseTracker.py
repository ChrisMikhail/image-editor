import interface

class MouseTracker:
    def __init__(self, parent):
        self.canvas = interface.canvas
        self.canvas.pack()
        self.mouse_x, self.mouse_y = 0, 0
        self.mouse_pressed = False
        self.canvas.bind("<Motion>", self.update_mouse_position)
        self.canvas.bind("<ButtonPress-1>", self.mouse_down)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_up)

    def update_mouse_position(self, event):
        if self.mouse_pressed:
            self.mouse_x, self.mouse_y = event.x, event.y
            self.canvas.create_oval(self.mouse_x, self.mouse_y, self.mouse_x+20, self.mouse_y+20, fill='black')

    def mouse_down(self, event):
        self.mouse_pressed = True

    def mouse_up(self, event):
        self.mouse_pressed = False