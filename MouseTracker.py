import interface

class MouseTracker:
    def __init__(self, parent):
        self.mouse_x, self.mouse_y = 0, 0
        self.mouse_pressed = False
        self.draw_enabled = False
        self.erase_enabled = False
        self.fill_colour = 'black'
        self.startxy = (0, 0)
        interface.canvas.bind("<Motion>", self.update_mouse_position)
        interface.canvas.bind("<ButtonPress-1>", self.mouse_down)
        interface.canvas.bind("<ButtonRelease-1>", self.mouse_up)
        interface.window.bind("<Control-p>", self.toggle_draw)
        interface.window.bind("<Control-e>", self.toggle_erase)
        interface.window.bind("<Control-R>", lambda event: self.change_colour(event, 'red'))
        interface.window.bind("<Control-G>", lambda event: self.change_colour(event, 'green'))
        interface.window.bind("<Control-B>", lambda event: self.change_colour(event, 'blue'))
        interface.window.bind("<Control-b>", lambda event: self.change_colour(event, 'black'))




    def update_mouse_position(self, event):

        self.mouse_x, self.mouse_y = event.x, event.y
        if self.mouse_pressed and self.draw_enabled:
            interface.canvas.create_oval(self.mouse_x - 7, self.mouse_y - 7, self.mouse_x + 7, self.mouse_y + 7, fill=self.fill_colour, outline=self.fill_colour)

        if self.mouse_pressed and self.erase_enabled:
            selected_oval = interface.canvas.find_enclosed(self.mouse_x - 18, self.mouse_y - 18, self.mouse_x + 18, self.mouse_y + 18)
            if len(selected_oval) > 0:
                if interface.canvas.type(selected_oval[0]) == 'oval':
                    interface.canvas.delete(selected_oval[0])

        if self.mouse_pressed and (self.erase_enabled == False) and (self.draw_enabled == False):
            selected_img = interface.canvas.find_overlapping(self.mouse_x, self.mouse_y, self.mouse_x, self.mouse_y)
            if interface.canvas.type(selected_img) == 'image':
                dx, dy = event.x - self.startxy[0], event.y - self.startxy[1]
                interface.canvas.move(selected_img, dx, dy)
                self.startxy = (event.x, event.y)

        


    def mouse_down(self, event):
        self.mouse_pressed = True
        self.startxy = (event.x, event.y)

    def mouse_up(self, event):
        self.mouse_pressed = False

    def toggle_draw(self, event):
        self.draw_enabled = not self.draw_enabled
        if self.draw_enabled != False:
            interface.canvas.config(cursor="target")
            self.erase_enabled = False
        else:
            interface.canvas.config(cursor="arrow")


    def toggle_erase(self, event):
        self.erase_enabled = not self.erase_enabled
        if self.erase_enabled != False:
            interface.canvas.config(cursor="star")
            self.draw_enabled = False
        else:
            interface.canvas.config(cursor="arrow")


    def change_colour(self, event, colour):
        self.fill_colour = colour
        self.draw_enabled = True
        self.erase_enabled = False
        interface.canvas.config(cursor="target")

