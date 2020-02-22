from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Review Order and Submit")

        #labels for Customer info
        Label(self.master, text = "First Name: ").grid(row = 0)
        Label(self.master, text = "Last Name: ").grid(row = 1)
        Label(self.master, text = "Email: ").grid(row = 2)
        Label(self.master, text = "Phone Number: ").grid(row = 3)
        
        #labels for location
        Label(self.master, text = " ").grid(row = 4)
        Label(self.master, text = " Location Information").grid(row = 5)
        Label(self.master, text = " ").grid(row = 6)
        Label(self.master, text = "Address: ").grid(row = 7)
        Label(self.master, text = "City: ").grid(row = 8)
        Label(self.master, text = "State: ").grid(row = 9)
        Label(self.master, text = "Zip Code: ").grid(row = 10)

        #labels for card info
        Label(self.master, text = " ").grid(row = 11)
        Label(self.master, text = "Card Info").grid(row = 12)
        Label(self.master, text = " ").grid(row = 13)
        Label(self.master, text = "Card Number: ").grid(row = 14)
        Label(self.master, text = "Expiration Date (mmyy): ").grid(row = 15)
        Label(self.master, text = "CVV: ").grid(row = 16)
        Label(self.master, text = "Zip Code: ").grid(row = 17)





finalPage = Tk()
finalPage.geometry("800x600")
app = Window(finalPage)
finalPage.mainloop()