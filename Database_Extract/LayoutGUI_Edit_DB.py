from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import os
from Connect_Brisco_DB import Connect_DB
from extractCSV import ExtractCSV
from datetime import datetime, date, time
from PIL import Image, ImageTk


class GUIforDBedit:


    def __init__(self,master):
        self.master = master
        self.instance_db = Connect_DB('postgres','postgres','localhost','Boom_boom1')

        self.cwd = os.getcwd()

        self.img = Image.open("Brisco_logo.png")
        self.tk_img = ImageTk.PhotoImage(self.img)

        # Label Widgets
        self.label_image = Label(self.master,image=self.tk_img,borderwidth=2,relief='groove')
        self.label_year = Label(self.master,text ="Year")
        self.label_month = Label(self.master,text ="Month")
        self.label_day = Label(self.master,text ="Day")
        self.label_folder = Label(self.master,text ="Folder")
        self.label_Fname = Label(self.master, text="Filename")

        # Button widgets
        self.button_printName = Button(self.master, text="Create CSV",command=self.Create_CSV,bg='green')
        self.button_browse = Button(self.master, text = "Browse", command=self.Browse_dir)

        # text entry Widgets
        self.Dir_entry = Entry(self.master)
        self.Year_entry = Entry(self.master)
        self.Fname_entry = Entry(self.master)

        #Drop down menu Widgets
        self.DD_L_month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
                                'Sep','Oct','Nov','Dec']
        self.DD_month = self.Create_DropDown()

        #initial values in entry boxes
        self.Dir_entry.insert(0,self.cwd)
        self.Year_entry.insert(0,"2017")

        self.Dir_entry_row = 1
        self.Fname_entry_row = 2

        #enlarge Text boxes


        #Layout Widgets
        self.label_image.grid(row=0,column=0,pady=(0,30),sticky=E)
        self.label_folder.grid(row=1,column=0,sticky=W)
        self.Dir_entry.grid(row=1,column=0,sticky=E)
        self.button_browse.grid(row=1,column=3)
        self.label_Fname.grid(row=2, column=0,sticky=W)
        self.Fname_entry.grid(row=2, column=0,sticky=E)
        self.label_month.grid(row=3,column=0,pady=(20,0))
        self.label_year.grid(row=3,column=1,pady=(20,0))
        self.button_printName.grid(row=5,column=3,sticky=W,pady=100)
        #Example of a second window opening up

        self.frame = Frame(self.master)
        self.button1 = Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

    def Create_CSV(self):
        dirPrint = self.Dir_entry.get()
        t_month = self.var1.get()
        month_num = self.DD_L_month.index(t_month)+1
        year_num = int(self.Year_entry.get())
        self.Fname_entry.delete(0,'end')
        s = "_"
        t_year = self.Year_entry.get()
        seq = (t_month,t_year,"Load","Summary")
        t_fname1 = s.join(seq)
        t_fname2 = ".csv"
        t_fname = t_fname1 + t_fname2
        self.Fname_entry.insert(0,t_fname)
        full_file = os.path.join(dirPrint,t_fname)
        A=ExtractCSV(self.instance_db,t_fname,month_num,year_num)
        A.WriteCSV()

    def Create_DropDown(self):
        self.var1 = StringVar(self.master)
        self.var1.set(self.DD_L_month[0])
        self.DD_menu = OptionMenu(self.master, self.var1, *self.DD_L_month)
        self.DD_menu.config(width=8)


    def Browse_dir(self):

        self.directory = tkFileDialog.askdirectory()
        self.Dir_entry.delete(0,'end')
        self.Dir_entry.insert(0,self.directory)

        if self.Dir_entry.get() == '':
            self.directory = self.cwd
            self.Dir_entry.delete(0,'end')
            self.Dir_entry.insert(0,self.directory)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main loop keep at bottom~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
def main():
    root = Tk()
    root.geometry("500x500")
    A = GUIforDBedit(root)
    root.mainloop()

if __name__ == '__main__':
    main()
