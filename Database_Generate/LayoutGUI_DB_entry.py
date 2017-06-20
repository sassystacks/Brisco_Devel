from Tkinter import *
import ttk
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

# combobox initial val
TM9_combo_val = StringVar()
wCircle_combo_val = StringVar()
block_combo_val = StringVar()
logCircle_combo_val = StringVar()
haulBy_combo_val = StringVar()
truckLicense_combo_val = StringVar()
truckNum_combo_val = StringVar()
axle_combo_val = StringVar()

# 1st row combobox inisialize
TM9_combo = ttk.Combobox(root,textvariable = TM9_combo_val)
wCircle_combo = ttk.Combobox(root,textvariable = wCircle_combo_val)
block_combo = ttk.Combobox(root,textvariable = block_combo_val)
logCircle_combo = ttk.Combobox(root,textvariable = logCircle_combo_val)
haulBy_combo = ttk.Combobox(root,textvariable = haulBy_combo_val)
truckLicense_combo = ttk.Combobox(root,textvariable = truckLicense_combo_val)
truckNum_combo = ttk.Combobox(root,textvariable = truckNum_combo_val)
axle_combo = ttk.Combobox(root,textvariable = axle_combo_val)

#Drop down menu Widgets
pady_val = 100
columnum = 0
TM9_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
wCircle_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
block_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
logCircle_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
haulBy_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
truckLicense_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
truckNum_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
axle_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1

#initial values in entry boxes

#enlarge Text boxes


#Brisco Label
label_image.grid(row=0,column=0,pady=(0,30),sticky=E)

#1st Row Layout Widgets
label_date.grid(row=1,column=0)
label_popNum.grid(row=1,column=1)
label_popNumCount.grid(row=1,column=2)
label_SampleLoad.grid(row=1,column=3)
label_TM9.grid(row=1,column=4)
label_owner.grid(row=1,column=5)
label_FMA.grid(row=1,column=6)
label_workingCircle.grid(row=1,column=7)

#1st row Emtry and Combobox


#2nd row layout Widgets
label_BlockNum.grid(row=3,column=0)
label_loggingCo.grid(row=3,column=1)
label_TruckPlate.grid(row=3,column=2)
label_TruckNum.grid(row=3,column=3)
label_TruckAxle.grid(row=3,column=4)
label_gross.grid(row=3,column=5)
label_tare.grid(row=3,column=6)
label_net.grid(row=3,column=7)


root.mainloop()
