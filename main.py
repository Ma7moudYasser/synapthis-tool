from tkinter import *
from image_filtering import ImageFiltering
from edge_detection import EdgeDetection

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x500+100+100')
        self.root.config(background='#F9440B')
        self.root.resizable(False, False)
        self.root.title("Synapthsis")

        ## --------- Buttons ----------------------------- #
        btn_image_filtering = Button(master=root, text='Image Filtering', font=('Arial', 12, 'bold'), bg='#ED251F', command=self.open_image_filtering_window)
        btn_image_filtering.place(x=100, y=100)


        btn_image_detection = Button(master=root, text = 'Edge detection', font=('Arial', 12, 'bold' ), bg = '#ED251F', command=self.open_image_detection_window)
        btn_image_detection.place(x= 250, y = 100)

        # ------------ Labels -----------------------------#
        label_of_application = Label(master=root, text='Welcome to Synapthis', font=('Arial', 20, 'bold'), bg='#F9440B')
        label_of_application.place(x=450, y=30)

    def open_image_filtering_window(self):
        self.root.withdraw()  # Hide the main window
        ImageFiltering(self.root)
    def open_image_detection_window(self):
        self.root.withdraw()
        EdgeDetection(self.root)



if __name__ == "__main__":
    root = Tk()
    ob = MainMenu(root)
    root.mainloop()
