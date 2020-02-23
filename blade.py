from tkinter import *
#from pizzapi import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Pizza Orderer")
        
        def blade():
            count = 1
            for i in range(0, 1000):

                
                Label(self.master, text = "I LOVE BLADE ").grid(row = count, column = count + 1)
                count = count + 1
        
        enter = Button(root, text = "Press Me hehe" ,command = blade)
        enter.grid(row = 0)
        





root = Tk()
root.geometry("1920x1080")
app = Window(root)
root.mainloop()