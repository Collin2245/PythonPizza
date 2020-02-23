
import tkinter as tk
from tkinter import *

import Page

class CardInfoScreenClass(Page.PageClass):
    def __init__(self,*args,**kwargs):
        Page.PageClass.__init__(self,*args, **kwargs)



        # Label(text ="ENTER INFO ").grid(row=0)
        # Label(text ="First name: ").grid(row=1)
        # Label(text ="Last name: ").grid(row=2)
        # Label(text ="Email address: ").grid(row=3)
        # Label(text ="Phone number: ").grid(row=4)
        # fName = Entry()
        # lName = Entry()
        # emailAddress = Entry()
        # phoneNum = Entry()
        # nextButton = Button( text="next")
                        
        # fName.grid(row=1, column=1)
        # lName.grid(row=2, column=1)
        # emailAddress.grid(row=3, column=1)
        # phoneNum.grid(row=4, column=1)
        # nextButton.grid(row=5,column =1)



        Label( text = "Card Number: ").pack()
        Label( text = "Expiration Date: ").pack()
        Label( text = "CVV: ").pack()
        Label( text = "Zip Code: ").pack()
        cardNum = Entry()
        expDate = Entry()
        cvv = Entry()
        zipCode = Entry()
        cardNum.pack()
        expDate.pack()
        cvv.pack()
        zipCode.pack()

        




