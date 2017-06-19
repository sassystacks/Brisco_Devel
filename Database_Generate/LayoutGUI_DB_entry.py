from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

from PIL import Image, ImageTk



def Browse_dir():
    directory = tkFileDialog.askdirectory()
    Dir_entry.delete(0,'end')
    Dir_entry.insert(0,directory)

def Create_DropDown():
    root.var1 = StringVar(root)
    root.var1.set(root.DD_L_month[0])
    root.DD_menu = OptionMenu(root, root.var1, *root.DD_L_month)
    root.DD_menu.config(width=8)
    return root.DD_menu

# Main code Start


# B = ExtractCSV(A,'test.csv',11,2016)
root = Tk()
root.geometry("500x500")
cwd = os.getcwd()

img = Image.open("Brisco_logo.png")
tk_img = ImageTk.PhotoImage(img)

# Label Widgets
label_image = Label(root,image=tk_img,borderwidth=2,relief='groove')
label_date = Label(root,text ="Date")
label_popNum = Label(root,text ="Pop. Load Slip#")
label_popNumCount = Label(root,text ="Pop. Count")
label_SampleLoad = Label(root,text ="Sample Loads")
label_TM9 = Label(root, text="TM9/Ticket #")
label_owner = Label(root, text="Owner")
label_FMA = Label(root, text="Disposition/FMA #")
label_workingCircle= Label(root, text="Working Circle")
label_BlockNum = Label(root, text="Block #")
label_loggingCo = Label(root, text="Logging Co.")
label_TruckPlate = Label(root, text="Truck License Plate #")
label_TruckNum= Label(root, text="Truck #")
label_TruckAxle = Label(root, text="Truck Axle")
label_gross = Label(root, text="Gross Weight")
label_tare = Label(root, text="Tare Weight")
label_net = Label(root, text="Net Weight")


# Button widgets
button_printName = Button(root, text="Create CSV",command=Create_CSV,bg='green')
Dir_to_Save = Button(root, text = "Browse", command=Browse_dir)

# text entry Widgets
Dir_entry = Entry(root)
root.Year_entry = Entry(root)
Fname_entry = Entry(root)

#Drop down menu Widgets
root.DD_L_month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
                        'Sep','Oct','Nov','Dec']
DD_month = Create_DropDown()

#initial values in entry boxes
Dir_entry.insert(0,cwd)
root.Year_entry.insert(0,"2017")

Dir_entry_row = 1
Fname_entry_row = 2

#enlarge Text boxes


#Layout Widgets
label_image.grid(row=0,column=0,pady=(0,30),sticky=E)
label_folder.grid(row=1,column=0,sticky=W)
Dir_entry.grid(row=1,column=0,sticky=E)
Dir_to_Save.grid(row=1,column=3)
label_Fname.grid(row=2, column=0,sticky=W)
Fname_entry.grid(row=2, column=0,sticky=E)
label_month.grid(row=3,column=0,pady=(20,0))
label_year.grid(row=3,column=1,pady=(20,0))
root.Year_entry.grid(row=4,column=1)
DD_month.grid(row=4, column= 0)
button_printName.grid(row=5,column=0,sticky=W,pady=100)

root.mainloop()
