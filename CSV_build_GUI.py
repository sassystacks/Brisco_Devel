from Tkinter import *

class Application(Frame):
    def Build_CSV(self):
        dt_selected = self.var1.get()
        print(dt_selected)
        try:
            indx_date = self.lst1.index(dt_selected)+1
            print(indx_date)
        except:
            print"Please Select a date"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.CSV_build = Button(self)
        self.CSV_build ["text"] = "Create CSV",
        self.CSV_build ["command"] = self.Build_CSV
        self.CSV_build .pack({"side": "left"})

        self.lst1 = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
                    'Sep','Oct','Nov','Dec']
        self.var1 = StringVar()
        self.drop = OptionMenu(root,self.var1,*self.lst1)
        self.drop.grid()
        self.drop.pack({"side": "left"})




    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
