from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import os
from Connect_Brisco_DB import Connect_DB
from extractCSV import ExtractCSV
from datetime import datetime, date, time
from PIL import Image, ImageTk

def Create_CSV():
    dirPrint =Dir_entry.get()
    t_month = root.var1.get()
    Fname_entry.delete(0,'end')
    s = "_"
    t_year = Year_entry.get()
    seq = ("Gov","Barkies",t_month,t_year,"CSV")
    t_fname1 = s.join(seq)
    t_fname2 = ".csv"
    t_fname = t_fname1 + t_fname2
    Fname_entry.insert(0,t_fname)
    full_file = os.path.join(dirPrint,t_fname)
    print(full_file)

def Browse_dir():
    directory = tkFileDialog.askdirectory()
    Dir_entry.delete(0,'end')
    Dir_entry.insert(0,directory)

def Create_DropDown(root,DD_list):
    root.var1 = StringVar(root)
    root.var1.set(DD_list[0])
    root.DD_menu = OptionMenu(root, root.var1, *DD_list)
    root.DD_menu.config(width=8)
    return root.DD_menu

# Main code Start

A = Connect_DB('postgres','postgres','localhost','Boom_boom1')
root = Tk()
root.geometry("500x500")
cwd = os.getcwd()

img = Image.open("Brisco_logo.png")
tk_img = ImageTk.PhotoImage(img)

# Label Widgets
label_image = Label(root,image=tk_img,borderwidth=2,relief='groove')
label_year = Label(root,text ="Year")
label_month = Label(root,text ="Month")
label_day = Label(root,text ="Day")
label_folder = Label(root,text ="Folder")
label_Fname = Label(root, text="Filename")

# Button widgets
button_printName = Button(root, text="Create CSV",command=Create_CSV,bg='green')
Dir_to_Save = Button(root, text = "Browse", command=Browse_dir)

# text entry Widgets
Dir_entry = Entry(root)
Year_entry = Entry(root)
Fname_entry = Entry(root)

#Drop down menu Widgets
DD_L_month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
                        'Sep','Oct','Nov','Dec']
DD_month = Create_DropDown(root,DD_L_month)

#initial values in entry boxes
Dir_entry.insert(0,cwd)
Year_entry.insert(0,"2017")

Dir_entry_row = 1
Fname_entry_row = 2


#Layout Widgets
label_image.grid(row=0,column=0,sticky=E)
label_folder.grid(row=1,column=0,sticky=W)
Dir_entry.grid(row=1,column=0,sticky=E)
Dir_to_Save.grid(row=1,column=1)
label_Fname.grid(row=2, column=0,sticky=W)
Fname_entry.grid(row=2, column=0,sticky=E)
label_month.grid(row=3,column=0,pady=(20,0))
label_year.grid(row=3,column=1,pady=(20,0))
Year_entry.grid(row=4,column=1)
DD_month.grid(row=4, column= 0)
button_printName.grid(row=5,column=0,sticky=W,pady=100)

root.mainloop()
