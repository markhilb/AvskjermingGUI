import tkinter
from popups import EditGlassPopup
from config import CANVAS_BASELINE, CANVAS_LEFT_START, GLASS_BASELINE, WALLMOUNT_WIDTH, POST_WIDTH, POST_LAST_WIDTH, POST_BASE_WIDTH, POST_BASE_HEIGHT, \
                   LENGTH_BAR_SIDES_TOP, LENGTH_BAR_THICKNESS, LENGTH_BAR_SIDES_BOTTOM, LENGTH_BAR_TOP, LENGTH_BAR_BOTTOM, LENGT_BAR_LABEL_TOP, \
                   WALLMOUNT_DISPLAY_WIDTH, POST_DISPLAY_WIDTH, POST_BASE_DISPLAY_WIDTH, POST_BASE_DISPLAY_HEIGHT


class Wallmount:
    def __init__(self, canvas, xpos, height):
        self.canvas = canvas
        self.xpos = xpos
        self.width = WALLMOUNT_WIDTH
        self.display_width = WALLMOUNT_DISPLAY_WIDTH
        self.height = height + 1
        self.display_height = height + 5
        self.color = "gray"

        self.id = canvas.create_rectangle(self.xpos, CANVAS_BASELINE - self.display_height, self.xpos + self.display_width, CANVAS_BASELINE, fill=self.color)

    def delete(self):
        self.canvas.delete(self.id)


class Post:
    def __init__(self, canvas, xpos, height, is_last):
        self.canvas = canvas
        self.xpos = xpos
        self.display_width = POST_DISPLAY_WIDTH
        self.height = height + 1
        self.display_height = height + 5
        self.is_last = is_last
        self.color = "black"

        self.id = canvas.create_rectangle(self.xpos, CANVAS_BASELINE - self.display_height, self.xpos + self.display_width, CANVAS_BASELINE, fill=self.color)

        self.base = canvas.create_rectangle(self.xpos - POST_BASE_DISPLAY_WIDTH, CANVAS_BASELINE - POST_BASE_DISPLAY_HEIGHT, self.xpos + self.display_width + POST_BASE_DISPLAY_WIDTH, CANVAS_BASELINE, fill=self.color)

    @property
    def width(self):
        return (POST_LAST_WIDTH if self.is_last else POST_WIDTH) 

    def delete(self):
        self.canvas.delete(self.id)
        self.canvas.delete(self.base)


class Glass:
    def __init__(self, canvas, total_width, xpos, width, height):
        self.canvas = canvas
        self.xpos = xpos
        self.display_width = width
        self.width = width
        self.display_height = height
        self.height = height
        self.color = "blue"

        self.id = canvas.create_rectangle(self.xpos, GLASS_BASELINE - self.display_height, self.xpos + self.display_width, GLASS_BASELINE, fill=self.color)
        canvas.tag_bind(self.id, "<Button-1>", lambda *args: EditGlassPopup(canvas, self.id, total_width))

        self.label = self.canvas.create_text(self.xpos + (self.display_width / 2), GLASS_BASELINE - self.display_height - 30, text=self.width)

    def delete(self):
        self.canvas.delete(self.id)
        self.canvas.delete(self.label)
    

class LengthBar:
    def __init__(self, canvas):
        self.canvas = canvas
        self.left = self.canvas.create_rectangle(0, 0, 0, 0, fill="black")
        self.right = self.canvas.create_rectangle(0, 0, 0, 0, fill="black")
        self.bar = self.canvas.create_rectangle(0, 0, 0, 0, fill="black")
        self.label = self.canvas.create_text(0, 0, text="")
    

    def update(self, current_width, xpos):
        self.canvas.delete(self.bar)
        self.canvas.delete(self.left)
        self.canvas.delete(self.right)
        self.canvas.delete(self.label)
        if current_width > 0:
            self.left = self.canvas.create_rectangle(CANVAS_LEFT_START, LENGTH_BAR_SIDES_TOP, CANVAS_LEFT_START + LENGTH_BAR_THICKNESS, LENGTH_BAR_SIDES_BOTTOM, fill="black")
            self.bar = self.canvas.create_rectangle(CANVAS_LEFT_START, LENGTH_BAR_TOP, xpos, LENGTH_BAR_BOTTOM, fill="black")
            self.right = self.canvas.create_rectangle(xpos - LENGTH_BAR_THICKNESS, LENGTH_BAR_SIDES_TOP, xpos, LENGTH_BAR_SIDES_BOTTOM, fill="black")
            self.label = self.canvas.create_text(xpos / 2, LENGT_BAR_LABEL_TOP, text=current_width)