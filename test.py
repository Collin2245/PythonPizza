import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames  
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
       

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        fNameLabel = tk.Label(self, text="First name: ", font=controller.title_font)
        fNameLabel.pack(side="left",  padx = 10, pady = 10,anchor = "nw")

        fName = tk.Entry(self, font=controller.title_font)
        fName.pack(side="right",  padx = 10, pady = 10,anchor = "w")

        lNameLabel = tk.Label(self, text="last name: ", font=controller.title_font)
        lNameLabel.pack(side="left",  padx = 10, pady = 10,anchor = "w")

        lName = tk.Entry(self,  font=controller.title_font)
        lName.pack(side="right", padx = 10, pady = 10 ,anchor = "w")


        # Label(text ="ENTER INFO ").pack()
        # Label(text ="First name: ").pack()
        # Label(text ="Last name: ").pack()
        # Label(text ="Email address: ").pack()
        # Label(text ="Phone number: ").pack()

        # lName = Entry()
        # emailAddress = Entry()
        # phoneNum = Entry()
        # nextButton = Button( text="next")
                        
        # fName.pack()
        # lName.pack()
        # emailAddress.pack()
        # phoneNum.pack()
        # nextButton.pack()
    
 
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side="bottom", fill="x", pady=10)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()