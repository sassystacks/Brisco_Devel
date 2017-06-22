from Tkinter import *
import ttk
import Tkinter, Tkconstants, tkFileDialog
import datetime
from Connect_Brisco_DB import Connect_DB

from PIL import Image, ImageTk


# Function Defs

# B = ExtractCSV(A,'test.csv',11,2016)
root = Tk()
root.geometry("1200x800")

connect_trucker = Connect_DB('postgres','postgres','192.168.0.200','coffeegood')


img = Image.open("Brisco_logo.png")
tk_img = ImageTk.PhotoImage(img)

# Label Widgets
label_image = Label(root,image=tk_img,borderwidth=2,relief='groove')
label_timeIn_tag = Label(root, text = "Time in: ")
label_timeOut_tag = Label(root, text = "Time out: ")
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
label_pcs = Label(root, text="Pieces")
label_hauledBy = Label(root, text = "Hauled by")

# labels that change with weight entered
textVarGross = "[]kg"
textVarTare = "[]kg"
textVarNet = "[]kgr"

label_scaleGross = Label(root,text=textVarGross)
label_scaleTare = Label(root,text=textVarTare )
label_scaleNet = Label(root,text=textVarNet)

# Buttons
button_weighIn = Button(root, text="Weigh In",bg='green')
button_weighOut = Button(root, text="Weigh Out",bg='green')
button_weighIn.config(width='20',height='8',activebackground='red')
button_weighOut.config(width='20',height='8',activebackground='red')

# Drop Down Menus
# Generate Time and Date
date_now = str(datetime.datetime.now().date())
time_now = str(datetime.datetime.now().strftime("%H:%M:%S"))

gen_date = Label(root, text = date_now)
gen_timeIn = Label(root, text = time_now)
gen_timeOut = Label(root, text = time_now)

#population load slip
DD_lst_popLoad = ['720','726','730','740','750','760','780','785']
popLoad_DD_val = StringVar()
popLoad_DD_val.set(DD_lst_popLoad[0])
popLoad_DD_menu = OptionMenu(root, popLoad_DD_val, *DD_lst_popLoad)

# Sample Load drop down menu
DD_lst_sample = ['No','Yes']
sample_DD_Val = StringVar()
sample_DD_Val.set(DD_lst_sample[0])
sample_DD_menu = OptionMenu(root, sample_DD_Val, *DD_lst_sample)

# textEntry
popCount_entry = Entry(root)
TM9_entry =Entry(root)
gross_entry = Entry(root)
tare_entry = Entry(root)
net_entry = Entry(root)
timeIn_entry = Entry(root)
timeOut_entry = Entry(root)
pcs_entry = Entry(root)

# combobox initial val
owner_combo_val = StringVar()
FMA_combo_val = StringVar()
wCircle_combo_val = StringVar()
block_combo_val = StringVar()
logCo_combo_val = StringVar()
truckLicense_combo_val = StringVar()
truckNum_combo_val = StringVar()
axle_combo_val = StringVar()
hauledBy_combo_val = StringVar()

# 1st row combobox inisialize
owner_combo = ttk.Combobox(root,textvariable = owner_combo_val)
FMA_combo = ttk.Combobox(root,textvariable = FMA_combo_val)
hauledBy_combo = ttk.Combobox(root,textvariable = hauledBy_combo_val)
# 2nd Row combobox initialize
wCircle_combo = ttk.Combobox(root,textvariable = wCircle_combo_val)
block_combo = ttk.Combobox(root,textvariable = block_combo_val)
logCo_combo = ttk.Combobox(root,textvariable = logCo_combo_val)
truckLicense_combo = ttk.Combobox(root,textvariable = truckLicense_combo_val)
truckNum_combo = ttk.Combobox(root,textvariable = truckNum_combo_val)
axle_combo = ttk.Combobox(root,textvariable = axle_combo_val)

#Drop down menu Widgets
# row 2 of GUI
pady_val = 100
columnum = 0
popLoad_DD_menu.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
popCount_entry.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
sample_DD_menu.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
TM9_entry.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
owner_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
FMA_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
hauledBy_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1

# 4th Row
columnum = 0
wCircle_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
block_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
logCo_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
truckLicense_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
truckNum_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
axle_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1
pcs_entry.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
columnum = columnum+1

#enlarge Text boxes

#1st row labels
label_image.grid(row=0,column=0,pady=(0,30),sticky=E)
label_date.grid(row=0, column = 6,pady = (10,0),sticky='nw')
label_timeIn_tag.grid(row=0, column = 6,sticky=W)
label_timeOut_tag.grid(row=0, column = 6, pady = (60,0),sticky=W)

#insert date and times
gen_date.grid(row=0, column = 7,pady = (10,0),sticky=N)
gen_timeIn.grid(row=0, column = 7)
gen_timeOut.grid(row=0, column = 7, pady = (60,0))

#2nd Row Layout Widgets
columnum = 0
label_popNum.grid(row=1,column=columnum )
columnum = columnum+1
label_popNumCount.grid(row=1,column=columnum )
columnum = columnum+1
label_SampleLoad.grid(row=1,column=columnum )
columnum = columnum+1
label_TM9.grid(row=1,column=columnum )
columnum = columnum+1
label_owner.grid(row=1,column=columnum )
columnum = columnum+1
label_FMA.grid(row=1,column=columnum )
columnum = columnum+1
label_hauledBy.grid(row=1,column=columnum )
columnum = columnum+1
#1st row Emtry and Combobox


#2nd row layout Widgets
columnum = 0
label_workingCircle.grid(row=3,column=columnum)
columnum = columnum+1
label_BlockNum.grid(row=3,column=columnum)
columnum = columnum+1
label_loggingCo.grid(row=3,column=columnum)
columnum = columnum+1
label_TruckPlate.grid(row=3,column=columnum)
columnum = columnum+1
label_TruckNum.grid(row=3,column=columnum)
columnum = columnum+1
label_TruckAxle.grid(row=3,column=columnum)
columnum = columnum+1
label_pcs.grid(row=3,column=columnum)
columnum = columnum+1

#3rd row labels
label_gross.grid(row=5,column=0)
label_tare.grid(row=5,column=1)
label_net.grid(row=5,column=2)


#3rd row values
columnum = 0
label_scaleGross.grid(row=6,column=columnum)
columnum = columnum+1
label_scaleTare.grid(row=6,column=columnum)
columnum = columnum+1
label_scaleNet.grid(row=6,column=columnum)
columnum = columnum+1


# Buttons
columnum = 0
button_weighIn.grid(row=7,column=columnum,pady=100)
columnum = columnum+1
button_weighOut.grid(row=7,column=columnum,pady=100)

# Main loop keep at bottom
root.mainloop()
