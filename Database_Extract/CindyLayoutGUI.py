from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import os
from Connect_Brisco_DB import Connect_DB
from extractCSV import ExtractCSV
from datetime import datetime, date, time
from PIL import Image, ImageTk

class CindyProgram:
    def __init__(self,master):

        cwd = os.getcwd()
        self.master = master

        self.img = Image.open("Brisco_logo.png")
        self.tk_img = ImageTk.PhotoImage(self.img)

        #initialize rames
        self.frame1 = Frame(self.master,borderwidth =5,relief='raised',padx=50,pady=50)
        self.frame1.grid(column=0, row=1)
        self.frame2 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame2.grid(column=0, row=0,padx=50,pady=50)
        self.frame3 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame3.grid(row=1,column=0,rowspan=2)
        # self.label_frame3 = Label(self.frame3,text='frame3')
        # self.label_frame3.pack()

        # Label Widgets
        self.label_image = Label(self.frame2,image=self.tk_img,borderwidth=2,relief='groove')
        self.label_year = Label(self.frame1,text ="Year")
        self.label_month = Label(self.frame1,text ="Month")
        self.label_day = Label(self.frame1,text ="Day")
        self.label_folder = Label(self.frame1,text ="Folder")
        self.label_Fname = Label(self.frame1, text="Filename")

        # Button widgets
        # self.button_printName = Button(self.frame3, text="Create CSV",command=self.Create_CSV,bg='green')
        self.Dir_to_Save = Button(self.frame1, text = "Browse", command=self.Browse_dir)

        # text entry Widgets
        self.Dir_entry = Entry(self.frame1)
        self.Year_entry = Entry(self.frame1)
        self.Fname_entry = Entry(self.frame1)

        #Drop down menu Widgets
        self.DD_L_month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
                                'Sep','Oct','Nov','Dec']
        self.DD_month = self.Create_DropDown()

        #initial values in entry boxes
        self.Dir_entry.insert(0,cwd)
        self.Year_entry.insert(0,"2017")

        self.Dir_entry_row = 1
        self.Fname_entry_row = 2

        #Layout Widgets
        self.label_image.grid(row=0,column=0,sticky=E,pady=70,padx=70)
        self.label_folder.grid(row=0,column=0,sticky=W)
        self.Dir_entry.grid(row=0,column=1)
        self.Dir_to_Save.grid(row=0,column=3,sticky=E,padx=(20,0))
        self.label_Fname.grid(row=1, column=0,sticky=W)
        self.Fname_entry.grid(row=1, column=1,sticky=E)
        self.label_month.grid(row=2,column=0,pady=(20,0))
        self.label_year.grid(row=2,column=1,pady=(20,0))
        self.Year_entry.grid(row=3,column=1)
        self.DD_month.grid(row=3, column= 0)

        self.label_CSV = Label(self.master,text='Export SpreadSheets',relief='sunken')
        self.label_CSV.grid(row=0,column=0,pady=(320,0))


    def Create_CSV(self):
        dirPrint =self.Dir_entry.get()
        t_month = self.var1.get()
        month_num =self.DD_L_month.index(t_month)+1
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
        # A=ExtractCSV(master.instance_db,t_fname,month_num,year_num)
        # A.WriteCSV()

    def Browse_dir(self):
        directory = tkFileDialog.askdirectory()
        self.Dir_entry.delete(0,'end')
        self.Dir_entry.insert(0,directory)

    def Create_DropDown(self):
        self.var1 = StringVar()
        self.var1.set(self.DD_L_month[0])
        self.DD_menu = OptionMenu(self.frame1, self.var1, *self.DD_L_month)
        self.DD_menu.config(width=8)
        return self.DD_menu



def main():
    root = Tk()
    app = CindyProgram(root)
    root.geometry("1000x700")
    root.mainloop()

if __name__ == '__main__':
    main()