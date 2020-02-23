from tkinter import *
#from pizzapi import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def init_window(self):

        Label(self.master, text = "First name: ").grid(row = 0)
        Label(self.master, text = "Last name: ").grid(row = 1)
        Label(self.master, text = "Email: ").grid(row = 2)
        Label(self.master, text = "Phone number: ").grid(row = 3)
        
        fName = Entry(self.master)
        lName = Entry(self.master)
        email = Entry(self.master)
        phoneNum = Entry(self.master)
        fName.grid(row = 0, column = 1)
        lName.grid(row = 1, column = 1)
        email.grid(row = 2, column = 1)
        phoneNum.grid(row = 3, column = 1)
        
        
        Label(self.master, text = "Address: ").grid(row = 4)
        Label(self.master, text = "City: ").grid(row = 5)
        Label(self.master, text = "State: ").grid(row = 6)
        Label(self.master, text = "Zip Code: ").grid(row = 7)
        
        
        address = Entry(self.master)
        city = Entry(self.master)
        state = Entry(self.master)
        zipCode = Entry(self.master)
        address.grid(row = 4, column = 1)
        city.grid(row = 5, column = 1)
        state.grid(row = 6, column = 1)
        zipCode.grid(row = 7, column = 1)


        Label(self.master, text = "Card Number: ").grid(row = 8)
        Label(self.master, text = "Expiration Date: ").grid(row = 9)
        Label(self.master, text = "CVV: ").grid(row = 10)
        Label(self.master, text = "Zip Code on card: ").grid(row = 11)
        
        cardNum = Entry(self.master)
        expDate = Entry(self.master)
        cvv = Entry(self.master)
        zipCodeCard = Entry(self.master)
        cardNum.grid(row = 8, column = 1)
        expDate.grid(row = 9, column = 1)
        cvv.grid(row = 10, column = 1)
        zipCodeCard.grid(row = 11, column = 1)
        
        def saveUser():
            #customer = Customer(fName.get(), lastName.get(), email.get(), phoneNum.get() )
            hi = fName.get()
            print(hi)
            bye = cardNum.get()
            #card = PaymentObject(cardNum.get(), expDate.get(), cvv.get(), zipCode.get())            
            print(bye)

        enter = Button(root, text = "Save user" ,command = saveUser)
        enter.grid(row = 12, column = 2)



root = Tk()
root.geometry("300x800")
app = Window(root)
root.mainloop()