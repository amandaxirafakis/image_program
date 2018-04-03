#import GUI library
from tkinter import *

#for Python V3 you must explicitely load the messagebox
import tkinter.messagebox

#create the book class incorporating instance variables and methods
class Book:
    def __init__(self, id_i, filename_i, title_i, owner_i, licence_i, size_i):
        self.id = id_i
        self.filename = filename_i
        self.title = title_i
        self.owner = owner_i
        self.licenec = licence_i
        self.size = size_i

    def get_id(self):
        return self.id

    def get_filename(self):
        return self.filename

    def get_title(self):
        return self.title

    def get_owner(self):
        return self.owner

    def get_licence(self):
        return self.licence

    def get_size(self):
        return self.size

class GUI:

    def __init__(self):

        window = Tk()
        window.title("Image metadata")
        window.minsize(width=400, height=270)

        self.recordlist = []

        id_label = Label(window, text='Enter ID of image:')
        id_label.pack() 
        self.id_field = Entry(window)
        self.id_field.pack()

        filename_label = Label(window, text='Enter the name of the file: (e.g flowers.jpg)')
        filename_label.pack()
        self.filename_field = Entry(window)
        self.filename_field.pack()

        title_label = Label(window, text='Enter the title of the file: (e.g flowers)')
        title_label.pack()
        self.title_field = Entry(window)
        self.title_field.pack()

        owner_label = Label(window, text='Enter the owner of the file:')
        owner_label.pack()
        self.owner_field = Entry(window)
        self.owner_field.pack()

        licence_label = Label(window, text='Enter the image licence type:')
        licence_label.pack()
        self.licence_field = Entry(window)
        self.licence_field.pack()

        size_label = Label(window, text='Enter the size of the image:')
        size_label.pack()
        self.size_field = Entry(window)
        self.size_field.pack()

        window.mainloop()

GUI()
