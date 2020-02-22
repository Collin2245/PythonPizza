import tkinter as tk
import CustomerInfo
from tkinter import font as tkfont

class PizzaOrderer3000(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family="Calibri",size=18, weight="bold")

        container = tk.Frame(self)
        container.pack(side="top", fill= "both", expand="true")
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}
        for F in (CustomerInfo,2): #add pages here
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame("CustomerInfo")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



        