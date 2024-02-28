from tkinter import *

class EdgeDetection:
    def __init__(self, root):
        self.root = root
        self.image_filtering_window = Toplevel(self.root)
        self.image_filtering_window.geometry('1200x500+100+100')
        self.image_filtering_window.config(background='#F9440B')
        self.image_filtering_window.resizable(False, False)
        self.image_filtering_window.title("Edge Detection")

        self.create_widgets()

    def create_widgets(self):
        # Add your widgets for image filtering window here
        pass
