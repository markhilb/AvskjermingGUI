import tkinter
from tkinter import messagebox
from tkinter.simpledialog import askstring
from decimal import Decimal
from items import Wallmount, Post, Glass, LengthBar
from config import CANVAS_LEFT_START, POST_WIDTH, POST_LAST_WIDTH, WALLMOUNT_WIDTH

class Canvas(tkinter.Canvas):
    def __init__(self, parent):
        super().__init__(parent, bg="red", highlightthickness=0)
        self.items = []
        self.current_width = Decimal("0")
        self.current_xpos = CANVAS_LEFT_START
        self.length_bar = LengthBar(self)

    def auto_calculate(self, total_width, left, width, height, right):
        self.clear()
        if left is Post:
            if not self.add_post(total_width, height):
                return
        else:
            if not self.add_wallmount(total_width, height):
                return
        
        total_width_minus_edges = (total_width - self.current_width - (POST_WIDTH if right is Post else WALLMOUNT_WIDTH))
        num =  total_width_minus_edges / (Decimal(width) + POST_WIDTH)
        
        for _ in range(int(num)):
            self.add_glass(total_width, width, height)
            self.add_post(total_width, height)
        self.add_glass(total_width, width, height)

        if right is Post:
            if not self.add_post(total_width, height):
                self.clear()
                return
        else:
            if not self.add_wallmount(total_width, height):
                self.clear()
                return
            
    def add_wallmount(self, total_width, height):
        if len(self.items) is not 0:
            if not isinstance(self.items[len(self.items) - 1], Glass):
                return False
        if self.current_width + WALLMOUNT_WIDTH >= total_width:
            if not self.cut_glass((self.current_width + WALLMOUNT_WIDTH) - total_width):
                return False
        wallmount = Wallmount(self, self.current_xpos, height)
        self.items.append(wallmount)
        self.update()
        return True

    def add_post(self, total_width, height):
        if len(self.items) is not 0:
            if not isinstance(self.items[len(self.items) - 1], Glass):
                return False
        if self.current_width + POST_LAST_WIDTH >= total_width:
            if not self.cut_glass((self.current_width + POST_LAST_WIDTH) - total_width):
                return False
        post = Post(self, self.current_xpos, height, True)
        self.items.append(post)
        self.update()
        return True

    def add_glass(self, total_width, width, height):
        if len(self.items) is 0 or self.current_width >= total_width:
            return False
        if isinstance(self.items[len(self.items) - 1], Post):
            if len(self.items) is not 1:
                self.items[len(self.items) - 1].is_last = False
                self.update()
        elif isinstance(self.items[len(self.items) - 1], Glass):
            return False
        if self.current_width + width > total_width:
            width = total_width - self.current_width 
        glass = Glass(self, self.current_xpos, width, height)
        self.items.append(glass)
        self.update()
        return True


    def cut_glass(self, width):
        if len(self.items) is 0:
            return False
        glass = self.items.pop()
        if glass.width <= width:
            self.items.append(glass)
            return False
        self.update()
        new_glass = Glass(self, self.current_xpos, glass.width - width, glass.height)
        self.items.append(new_glass)
        glass.delete()
        self.update()
        return True

    def update(self):
        self.current_width = Decimal("0")
        self.current_xpos = CANVAS_LEFT_START
        for item in self.items:
            self.current_width += item.width
            self.current_xpos += item.display_width
        self.length_bar.update(self.current_width, self.current_xpos)

    def clear(self):
        for item in self.items:
            item.delete()
        self.items.clear()
        self.current_width = Decimal("0")
        self.current_xpos = CANVAS_LEFT_START
        self.length_bar.update(self.current_width, self.current_xpos)

    def undo(self):
        if len(self.items) is not 0:
            item = self.items.pop()
            item.delete()
        if len(self.items) is not 0 and isinstance(self.items[len(self.items) - 1], Post):
            self.items[len(self.items) - 1].is_last = True
        self.update()

    def edit_glass(self, id, width):
        print(id)
        print(width)

    def delete_glass(self, id):
        print(id)