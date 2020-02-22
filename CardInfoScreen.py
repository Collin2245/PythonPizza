from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def init_window(self):

        

        #title
        self.master.title("Payment Information")
        
        #setting up labels and button
        Label(self.master, text = "Card Number: ").grid(row = 0)
        Label(self.master, text = "Expiration Date (mmyy): ").grid(row = 1)
        Label(self.master, text = "CVV: ").grid(row = 2)
        Label(self.master, text = "Zip Code: ").grid(row = 3)
        

        #defining entry variables
        cardNumInput = Entry(self.master)
        expDateInput = Entry(self.master)
        cvvInput = Entry(self.master)
        zipCodeInput = Entry(self.master)

        def test():
            print(cardNumInput.get())
            print(expDateInput.get())
            print(cvvInput.get())
            print(zipCodeInput.get())
            

        #populating the grid
        cardNumInput.grid(row = 0, column = 1)
        expDateInput.grid(row = 1, column = 1)
        cvvInput.grid(row = 2, column = 1)
        zipCodeInput.grid(row = 3, column = 1)
        enter = Button(root, text = "Enter", command = test)
        enter.grid(row = 4, column = 1)

root = Tk(screenName = "Card Info")
root.geometry("800x600")
app = Window(root)
root.mainloop()

#hiiiii 