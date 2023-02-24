import interface

class MouseTracker:
    def __init__(self, parent):
        self.mouse_x, self.mouse_y = 0, 0
        self.mouse_pressed = False
        self.draw_enabled = False
        interface.canvas.bind("<Motion>", self.update_mouse_position)
        interface.canvas.bind("<ButtonPress-1>", self.mouse_down)
        interface.canvas.bind("<ButtonRelease-1>", self.mouse_up)
        interface.window.bind("<Return>", self.enable_draw)


    def update_mouse_position(self, event):
        if self.mouse_pressed and self.draw_enabled:
            self.mouse_x, self.mouse_y = event.x, event.y
            # Drawing feature will be here temporarily
            interface.canvas.create_oval(self.mouse_x, self.mouse_y, self.mouse_x+15, self.mouse_y+15, fill='black')

    def mouse_down(self, event):
        self.mouse_pressed = True

    def mouse_up(self, event):
        self.mouse_pressed = False

    def enable_draw(self, event):
        self.draw_enabled = True