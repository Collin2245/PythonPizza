from tkinter import *
from pizzapi import *


class Window(Frame):



    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    



    def init_window(self):
        self.master.title("PIZZA TIME")



        #Labels for user info
        Label(self.master, text = "First name: ").grid(row = 0)
        Label(self.master, text = "Last name: ").grid(row = 1)
        Label(self.master, text = "Email: ").grid(row = 2)
        Label(self.master, text = "Phone number: ").grid(row = 3)

        #Text boxes for user info
        fName = Entry(self.master)
        lName = Entry(self.master)
        email = Entry(self.master)
        phoneNum = Entry(self.master)

        #placing user info
        fName.grid(row = 0, column = 1)
        lName.grid(row = 1, column = 1)
        email.grid(row = 2, column = 1)
        phoneNum.grid(row = 3, column = 1)


        #labels for address
        Label(self.master, text = "Address: ").grid(row = 4)
        Label(self.master, text = "City: ").grid(row = 5)
        Label(self.master, text = "State: ").grid(row = 6)
        Label(self.master, text = "Zip Code: ").grid(row = 7)

        #text boxes for address
        address = Entry(self.master)
        city = Entry(self.master)
        state = Entry(self.master)
        zipCodeHome = Entry(self.master)

        #placements for address
        address.grid(row = 4, column = 1)
        city.grid(row = 5, column = 1)
        state.grid(row = 6, column = 1)
        zipCodeHome.grid(row = 7, column = 1)

        #Labels for card
        Label(self.master, text = "Card Number: ").grid(row = 8)
        Label(self.master, text = "Expiration Date: ").grid(row = 9)
        Label(self.master, text = "CVV: ").grid(row = 10)
        Label(self.master, text = "Zip Code on card: ").grid(row = 11)

        #textboxes for card
        cardNum = Entry(self.master)
        expDate = Entry(self.master)
        cvv = Entry(self.master)
        zipCode = Entry(self.master)

        #placing card
        cardNum.grid(row = 8, column = 1)
        expDate.grid(row = 9, column = 1)
        cvv.grid(row = 10, column = 1)
        zipCode.grid(row = 11, column = 1)

        Label(self.master, text = "Order seperated by comma ").grid(row = 12)
        orderCombo = Entry(self.master)
        orderCombo.grid(row = 12, column = 1)



        #all in one button ordering 2 liter soda
        def saveUser():

            #info as strings

            #user
            fNameText = fName.get()
            lNameText = lName.get()
            emailText = email.get()
            phoneNumText = phoneNum.get()
            #card
            cardNumText = cardNum.get()
            expDateText = expDate.get()
            cvvText = cvv.get()
            zipCodeText = zipCode.get()
            #address
            addressText = address.get()
            cityText = city.get()
            stateText = state.get()
            zipCodeHomeText = zipCodeHome.get()

            #






            #setting up api
            customer = Customer(fNameText,lNameText,emailText,phoneNumText)
            print (fNameText)
            card = PaymentObject(cardNumText,expDateText,cvvText,zipCodeText)            
            print(cardNumText)
            destination = Address(addressText,cityText,stateText,zipCodeHomeText)
            print(customer)

            #api functions
            store = destination.closest_store()
            order = Order(store,customer,destination)

            orderComboText = orderCombo.get()
            result = [x.strip() for x in orderComboText.split(',')]


            for i in  result:
                order.add_item(i)

            print(result)
            #adding orders


            #mock paying for order
            order.pay_with(card)




        #button attached to function
        saveUserButton = Button(self.master, text = "Order" ,command = saveUser)

        saveUserButton.grid(row = 13, column = 1)










root = Tk()
root.geometry("400x800")
app = Window(root)
root.mainloop()