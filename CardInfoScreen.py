from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def init_window(self):

        #title
        self.master.title("GUI")
        
        #setting up labels and button
        Label(self.master, text = "Card Number: ").grid(row = 0)
        Label(self.master, text = "Expiration Date (mmyy): ").grid(row = 1)
        Label(self.master, text = "CVV: ").grid(row = 2)
        Label(self.master, text = "Zip Code: ").grid(row = 3)
        enter = Button(root, text = "Enter")
        enter.grid(row = 4, column = 1)

        #defining entry variables
        cardNum = Entry(self.master)
        expDate = Entry(self.master)
        cvv = Entry(self.master)
        zipCode = Entry(self.master)

        #putting those entry variables into the grid
        cardNum.grid(row = 0, column = 1)
        expDate.grid(row = 1, column = 1)
        cvv.grid(row = 2, column = 1)
        zipCode.grid(row = 3, column = 1)

    def nextAndEnter():
        




root = Tk(screenName = "Card Info")
root.geometry("800x600")
app = Window(root)
root.mainloop()
