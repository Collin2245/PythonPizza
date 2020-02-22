from tkinter import *
# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   
        #reference to the master widget, which is the tk window                 
        self.master = master
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()
    #Creation of init_window
    def init_window(self):
        def pull_code():
            CCODE = couponCode.get()
            print(CCODE)

   
        
        Label(self.master, text ="coupon:  ").grid(row=0)
        couponCode = Entry(self.master)
        couponCode.grid(row=0, column=1)

        
        
   
        Button(self.master, text = "submit coupon ", command= pull_code).grid(row=2, column=1)

       # canvas1.create_window(200, 140, window=entry1)

   # ccode = int(couponCode.get())
# root window created. Here, that would be the only window,
# you can later have windows within windows.
root = Tk()
root.geometry("400x300")
#creation of an instance
app = Window(root)
#mainloop 
root.mainloop() 
