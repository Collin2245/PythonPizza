from tkinter import *

#main function
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master
        self.init_window()
    def init_window(self):

        #title of master widget
        self.master.title("Information Page")
        

        Label(self.master, text = "Enter Location").grid(row=0)
        Label(self.master, text = "Address: ").grid(row=1)
        Label(self.master, text = "City: ").grid(row=2)
        Label(self.master, text = "State: ").grid(row=3)
        Label(self.master, text = "ZIP: ").grid(row=4)

        address = Entry(self.master)
        city = Entry(self.master)
        state = Entry(self.master)
        zipcode = Entry(self.master)

        
        address.grid(row = 1, column = 1)
        city.grid(row = 2, column = 1)
        state.grid(row = 3, column = 1)
        zipcode.grid(row = 4, column = 1)
        
        def callBack():
            storedAddress = (address.get())
            print(storedAddress)
            storedCity = (city.get())
            print(storedCity)
            storedState = (state.get())
            print(storedState)
            storedZip = (zipcode.get())
            print(storedZip)
         
       
        nextEnter= Entry(root)
        nextEnter = Button(root, text = "Next", command = callBack)
        nextEnter.grid(row = 5, column = 2)
        
        
         
       

root = Tk()


app = Window(root)
root.mainloop()