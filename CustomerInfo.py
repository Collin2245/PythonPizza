import tkinter as tk
from tkinter import *

import Page

class CustomerInfoClass(Page.PageClass):
    def __init__(self,*args,**kwargs):
        Page.PageClass.__init__(self,*args, **kwargs)





        Label(text ="ENTER INFO ").pack()
        Label(text ="First name: ").pack()
        Label(text ="Last name: ").pack()
        Label(text ="Email address: ").pack()
        Label(text ="Phone number: ").pack()
        fName = Entry()
        lName = Entry()
        emailAddress = Entry()
        phoneNum = Entry()
        nextButton = Button( text="next")
                        
        fName.pack()
        lName.pack()
        emailAddress.pack()
        phoneNum.pack()
        nextButton.pack()






    
       

  
        

    

