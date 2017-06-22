from Tkinter import *
import ttk
import Tkinter, Tkconstants, tkFileDialog
import datetime
from Connect_Brisco_DB import Connect_DB

from PIL import Image, ImageTk


# Function Defs

# B = ExtractCSV(A,'test.csv',11,2016)

class GUIatFrontDesk:

    def __init__(self,master,imageFname):

    # connect_trucker = Connect_DB('postgres','postgres','192.168.0.200','coffeegood')
    # connect_trucker = Connect_DB('postgres','postgres','192.168.20.200','coffeegood')


    self.img = Image.open()
    self.tk_img = ImageTk.PhotoImage(img)

    # Label Widgets
    self.label_image = Label(master,image=tk_img,borderwidth=2,relief='groove')
    self.label_timeIn_tag = Label(master, text = "Time in: ")
    self.label_timeOut_tag = Label(master, text = "Time out: ")
    self.label_date = Label(master,text ="Date")
    self.label_popNum = Label(master,text ="Pop. Load Slip#")
    self.label_popNumCount = Label(master,text ="Pop. Count")
    self.label_SampleLoad = Label(master,text ="Sample Loads")
    self.label_TM9 = Label(master, text="TM9/Ticket #")
    self.label_owner = Label(master, text="Owner")
    self.label_FMA = Label(master, text="Disposition/FMA #")
    self.label_workingCircle= Label(master, text="Working Circle")
    self.label_BlockNum = Label(master, text="Block #")
    self.label_loggingCo = Label(master, text="Logging Co.")
    self.label_TruckPlate = Label(master, text="Truck License Plate #")
    self.label_TruckNum= Label(master, text="Truck #")
    self.label_TruckAxle = Label(master, text="Truck Axle")
    self.label_gross = Label(master, text="Gross Weight")
    self.label_tare = Label(master, text="Tare Weight")
    self.label_net = Label(master, text="Net Weight")
    self.label_pcs = Label(master, text="Pieces")
    self.label_hauledBy = Label(master, text = "Hauled by")

    # labels that change with weight entered
    self.textVarGross = "[]kg"
    self.textVarTare = "[]kg"
    self.textVarNet = "[]kgr"

    self.label_scaleGross = Label(master,text=textVarGross)
    self.abel_scaleTare = Label(master,text=textVarTare )
    self.label_scaleNet = Label(master,text=textVarNet)

    # Buttons
    self.button_weighIn = Button(master, text="Weigh In",bg='green')
    self.button_weighOut = Button(master, text="Weigh Out",bg='green')
    self.button_weighIn.config(width='20',height='8',activebackground='red')
    self.button_weighOut.config(width='20',height='8',activebackground='red')
    # Drop Down Menus
    # Generate Time and Date
    self.date_now = str(datetime.datetime.now().date())
    self.time_now = str(datetime.datetime.now().strftime("%H:%M:%S"))

    self.gen_date = Label(master, text = date_now)
    self.gen_timeIn = Label(master, text = time_now)
    self.gen_timeOut = Label(master, text = time_now)

    #population load slip
    self.DD_lst_popLoad = ['720','726','730','740','750','760','780','785']
    self.popLoad_DD_val = StringVar()
    self.popLoad_DD_val.set(DD_lst_popLoad[0])
    self.popLoad_DD_menu = OptionMenu(master, popLoad_DD_val, *DD_lst_popLoad)

    # Sample Load drop down menu
    self.DD_lst_sample = ['No','Yes']
    self.sample_DD_Val = StringVar()
    self.sample_DD_Val.set(DD_lst_sample[0])
    self.sample_DD_menu = OptionMenu(master, sample_DD_Val, *DD_lst_sample)

    # textEntry
    self.popCount_entry = Entry(master)
    self.TM9_entry =Entry(master)
    self.gross_entry = Entry(master)
    self.tare_entry = Entry(master)
    self.net_entry = Entry(master)
    self.timeIn_entry = Entry(master)
    self.timeOut_entry = Entry(master)
    self.pcs_entry = Entry(master)

    # combobox initial val
    self.owner_combo_val = StringVar()
    self.FMA_combo_val = StringVar()
    self.wCircle_combo_val = StringVar()
    self.block_combo_val = StringVar()
    self.logCo_combo_val = StringVar()
    self.truckLicense_combo_val = StringVar()
    self.truckNum_combo_val = StringVar()
    self.axle_combo_val = StringVar()
    self.hauledBy_combo_val = StringVar()

    # 1st row combobox inisialize
    self.owner_combo = ttk.Combobox(master,textvariable = owner_combo_val)
    self.FMA_combo = ttk.Combobox(master,textvariable = FMA_combo_val)
    self.hauledBy_combo = ttk.Combobox(master,textvariable = hauledBy_combo_val)
    # 2nd Row combobox initialize
    self.wCircle_combo = ttk.Combobox(master,textvariable = wCircle_combo_val)
    self.block_combo = ttk.Combobox(master,textvariable = block_combo_val)
    self.logCo_combo = ttk.Combobox(master,textvariable = logCo_combo_val)
    self.truckLicense_combo = ttk.Combobox(master,textvariable = truckLicense_combo_val)
    self.truckNum_combo = ttk.Combobox(master,textvariable = truckNum_combo_val)
    self.axle_combo = ttk.Combobox(master,textvariable = axle_combo_val)

    #Drop down menu Widgets
    self.pady_val = 100
    columnum = 0
    self.popLoad_DD_menu.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1
    self.popCount_entry.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1
    self.sample_DD_menu.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1
    self.TM9_entry.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1
    self.hauledBy_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1

    # 4th Row
    columnum = 0
    self.wCircle_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1
    self.block_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1
    self.logCo_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1
    self.truckLicense_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1
    self.truckNum_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1
    self.axle_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1
    self.pcs_entry.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
    columnum = columnum+1

    #enlarge Text boxes

    #1st row labels
    self.label_image.grid(row=0,column=0,pady=(0,30),sticky=E)
    self.label_date.grid(row=0, column = 6,pady = (10,0),sticky='nw')
    self.label_timeIn_tag.grid(row=0, column = 6,sticky=W)
    self.label_timeOut_tag.grid(row=0, column = 6, pady = (60,0),sticky=W)

    #insert date and times
    self.gen_date.grid(row=0, column = 7,pady = (10,0),sticky=N)
    self.gen_timeIn.grid(row=0, column = 7)
    self.gen_timeOut.grid(row=0, column = 7, pady = (60,0))

    #2nd Row Layout Widgets
    columnum = 0
    self.label_popNum.grid(row=1,column=columnum )
    columnum = columnum+1
    self.label_popNumCount.grid(row=1,column=columnum )
    columnum = columnum+1
    self.label_SampleLoad.grid(row=1,column=columnum )
    columnum = columnum+1
    self.label_TM9.grid(row=1,column=columnum )
    columnum = columnum+1
    self.label_owner.grid(row=1,column=columnum )
    columnum = columnum+1
    self.label_FMA.grid(row=1,column=columnum )
    columnum = columnum+1
    self.label_hauledBy.grid(row=1,column=columnum )
    columnum = columnum+1
    #1st row Emtry and Combobox


    #2nd row layout Widgets
    columnum = 0
    self.label_workingCircle.grid(row=3,column=columnum)
    columnum = columnum+1
    self.label_BlockNum.grid(row=3,column=columnum)
    columnum = columnum+1
    self.label_loggingCo.grid(row=3,column=columnum)
    columnum = columnum+1
    self.label_TruckPlate.grid(row=3,column=columnum)
    columnum = columnum+1
    self.label_TruckNum.grid(row=3,column=columnum)
    columnum = columnum+1
    self.label_TruckAxle.grid(row=3,column=columnum)
    columnum = columnum+1
    self.label_pcs.grid(row=3,column=columnum)
    columnum = columnum+1

    #3rd row labels
    self.label_gross.grid(row=5,column=0)
    self.label_tare.grid(row=5,column=1)
    self.label_net.grid(row=5,column=2)


    #3rd row values
    columnum = 0
    self.label_scaleGross.grid(row=6,column=columnum)
    columnum = columnum+1
    self.label_scaleTare.grid(row=6,column=columnum)
    columnum = columnum+1
    self.label_scaleNet.grid(row=6,column=columnum)
    columnum = columnum+1


    # Buttons
    columnum = 0
    self.button_weighIn.grid(row=7,column=columnum,pady=100)
    columnum = columnum+1
    self.button_weighOut.grid(row=7,column=columnum,pady=100)

# Main loop keep at bottom
root = Tk()
A = GUIatFrontDesk(root,"Brisco_logo.png")
root.geometry("1200x800")
A.mainloop()
