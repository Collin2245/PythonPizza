import tkinter as tk
from tkinter import *

import PizzaOrderer3000
import globals


class CustomerInfo(PizzaOrderer3000.tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Label(self.master, text ="ENTER INFO ").grid(row=0)
        Label(self.master, text ="First name: ").grid(row=1)
        Label(self.master, text ="Last name: ").grid(row=2)
        Label(self.master, text ="Email address: ").grid(row=3)
        Label(self.master, text ="Phone number: ").grid(row=4)
        fName = Entry(self.master)
        lName = Entry(self.master)
        emailAddress = Entry(self.master)
        phoneNum = Entry(self.master)
        nextButton = Button(self.master, text="next")
        fName.grid(row=1, column=1)
        lName.grid(row=2, column=1)
        emailAddress.grid(row=3, column=1)
        phoneNum.grid(row=4, column=1)
        nextButton.grid(row=5,column =1)






    
       

  
        

    

