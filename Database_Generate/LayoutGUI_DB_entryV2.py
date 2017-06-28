from Tkinter import *
import ttk
import Tkinter, Tkconstants, tkFileDialog
import datetime
from Connect_Brisco_DB import Connect_DB
from DB_searchandFill import DB_search
from psycopg2 import sql
import serial
from psycopg2.extensions import AsIs

# Function Defs

# B = ExtractCSV(A,'test.csv',11,2016)

class GUIatFrontDesk:

    def __init__(self,master):

        from PIL import Image, ImageTk
        self.master = master


        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~            Connect to Database              ~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        connect_ip = '192.168.20.200'
        self.Connect_Brisco_DB = Connect_DB('postgres','postgres','192.168.20.200','coffeegood')
        self.cur1 = self.Connect_Brisco_DB.crsr()

        #create initial lists to populate dropdown and combobox
        init_list_Licensee = []
        init_list_FMA = []
        init_list_wCircle = []

        init_list_hauledBy = []
        init_list_truckLicense = []
        init_list_truckNum = []
        init_list_loggingco = []

        self.cur1.execute("SELECT * FROM owner_DB")
        rows = self.cur1.fetchall()
        for row in rows:
            if row[0] is not None:
                init_list_Licensee.append(row[0])
            if row[1] is not None:
                init_list_FMA.append(row[1])
            if row[2] is not None:
                init_list_wCircle.append(row[2])

        self.init_list_Licensee = list(set(init_list_Licensee))
        self.init_list_FMA = list(set(init_list_FMA))
        self.init_list_wCircle = list(set(init_list_wCircle))

        self.cur1.execute("SELECT haulingcontractor,truckplate,trucknum,loggingco FROM barkies_DB")
        rows = self.cur1.fetchall()
        for row in rows:
            if row[0] is not None:
                init_list_hauledBy.append(row[0])
            if row[1] is not None:
                init_list_truckLicense.append(row[1])
            if row[2] is not None:
                init_list_truckNum.append(row[2])
            if row[3] is not None:
                init_list_loggingco.append(row[3])

        self.init_list_hauledBy = list(set(init_list_hauledBy))
        self.init_list_truckLicense = list(set(init_list_truckLicense))
        self.init_list_truckNum = list(set(init_list_truckNum))
        self.init_list_loggingco = list(set(init_list_loggingco))

        self.img = Image.open("Brisco_logo.png")
        self.tk_img = ImageTk.PhotoImage(self.img)

        # Label Widgets
        self.label_image = Label(master,image=self.tk_img,borderwidth=2,relief='groove')
        self.label_timeIn_tag = Label(master, text = "Time in: ")
        self.label_timeOut_tag = Label(master, text = "Time out: ")
        self.label_date = Label(master,text ="Date")
        self.label_popNum = Label(master,text ="Population")
        self.label_popNumCount = Label(master,text ="Load Slip #")
        self.label_SampleLoad = Label(master,text ="Sample Load")
        self.label_TM9 = Label(master, text="TM9/Ticket #")
        self.label_owner = Label(master, text="Owner")
        self.label_hauledBy = Label(master, text = "Hauling Contractor")
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
        self.label_FMA = Label(master, text="Disposition/FMA #")

        # labels that change with weight entered
        self.textVarGross = "----kg"
        self.textVarTare = "----kg"
        self.textVarNet = "----kgr"
        self.textpopCount = "-------"

        self.label_scaleGross = Label(master,text=self.textVarGross)
        self.label_scaleTare = Label(master,text=self.textVarTare )
        self.label_scaleNet = Label(master,text=self.textVarNet)
        self.label_popCount = Label(master,text=self.textpopCount)

        # Buttons
        self.ButtonText = "Weigh\nIn"
        self.button_weighIn = Button(master, text=self.ButtonText,bg='green',command=self.WeighIN)
        self.button_weighOut = Button(master, text="Weigh Out",bg='green',command=self.new_window)
        self.button_reset = Button(master, text ='Reset',command=self.Reset_button)
        self.button_reset.config(width='10',height='8',activebackground='red')
        self.button_weighIn.config(width='20',height='8',activebackground='red')
        self.button_weighOut.config(width='20',height='8',activebackground='red')

        # Drop Down Menus
        # Generate Time and Date

        self.gen_date = Label(master, text = "-------------")
        self.gen_timeIn = Label(master, text = "-------------")
        self.gen_timeOut = Label(master, text = "-------------")

        #population load slip
        self.DD_lst_popLoad = ['720','726','730','740','750','760','780','785']
        self.popLoad_DD_val = StringVar()
        self.popLoad_DD_val.set(self.DD_lst_popLoad[0])
        self.popLoad_DD_menu = OptionMenu(master, self.popLoad_DD_val, *self.DD_lst_popLoad)

        # Sample Load drop down menu
        self.DD_lst_sample = ['No','Yes']
        self.sample_DD_Val = StringVar()
        self.sample_DD_Val.set(self.DD_lst_sample[0])
        self.sample_DD_menu = OptionMenu(master, self.sample_DD_Val, *self.DD_lst_sample)

        self.DD_lst_axle = ['5','6','7','8','9','10']
        self.axle_DD_Val = StringVar()
        self.axle_DD_Val.set(self.DD_lst_axle[2])
        self.axle_DD_menu = OptionMenu(master, self.axle_DD_Val, *self.DD_lst_axle)

        # textEntry
        self.TM9_entry =Entry(master)
        self.timeIn_entry = Entry(master)
        self.timeOut_entry = Entry(master)
        self.pcs_entry = Entry(master)
        self.block_entry = Entry(master)

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

        # 1st row combobox inisialize with bind to mouseclick
        self.owner_combo = ttk.Combobox(master,textvariable = self.owner_combo_val)
        self.owner_combo['values'] = self.init_list_Licensee
        self.owner_combo.set(self.init_list_Licensee[0])
        self.owner_combo.bind("<<ComboboxSelected>>",lambda event: self.DB_Search_n_Fill(event,"owner",self.Connect_Brisco_DB))

        #hauling Contractor Combobox
        self.FMA_combo = ttk.Combobox(master,textvariable = self.FMA_combo_val)
        self.FMA_combo['values'] = self.init_list_FMA
        self.FMA_combo.set(self.init_list_FMA[0])

        self.wCircle_combo = ttk.Combobox(master,textvariable = self.wCircle_combo_val)
        self.wCircle_combo['values'] = self.init_list_wCircle
        self.wCircle_combo.set(self.init_list_wCircle[0])

        # 2nd Row combobox initialize

        self.logCo_combo = ttk.Combobox(master,textvariable = self.logCo_combo_val)
        self.logCo_combo['values'] = self.init_list_loggingco
        self.logCo_combo.set(self.init_list_loggingco[0])

        self.truckLicense_combo = ttk.Combobox(master,textvariable = self.truckLicense_combo_val)
        self.truckLicense_combo['values'] = self.init_list_truckLicense
        self.truckLicense_combo.set(self.init_list_truckLicense[0])

        self.truckNum_combo = ttk.Combobox(master,textvariable = self.truckNum_combo_val)
        self.truckNum_combo['values'] = self.init_list_truckNum
        self.truckNum_combo.set(self.init_list_truckNum[0])

        self.hauledBy_combo = ttk.Combobox(master, textvariable = self.hauledBy_combo_val)
        self.hauledBy_combo['values'] = self.init_list_hauledBy
        self.hauledBy_combo.set(self.init_list_hauledBy[0])

        #Drop down menu Widgets
        pady_val = 100
        columnum = 0
        rownum = 2
        self.popLoad_DD_menu.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
        self.label_popCount.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
        self.sample_DD_menu.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
        self.TM9_entry.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
        self.owner_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
        self.hauledBy_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
        self.FMA_combo.grid(row = 2, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
                # 4th Row
        columnum = 0
        self.wCircle_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
        self.block_entry.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
        self.logCo_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
        self.truckLicense_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
        self.truckNum_combo.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
        columnum = columnum+1
        self.axle_DD_menu.grid(row = 4, column = columnum,sticky='nwe',pady=(0,pady_val))
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
        self.label_hauledBy.grid(row=1,column=columnum )
        columnum = columnum+1
        self.label_FMA.grid(row=1,column=columnum )
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
        columnum = columnum+1
        self.button_reset.grid(row=7,column=7,pady=100)



    def WeighOUTfill(self):

        self.cur1.execute("SELECT * FROM testscale WHERE tareweight IS Null;")

    def CreateLists(self):
        pass


    def DB_Search_n_Fill(self, event, strg, DB_instance):
        t_list_FMA = []
        t_list_workingCirc = []


        self.var_Selected = self.owner_combo.current()
        selection_val = str(self.init_list_Licensee[self.var_Selected])
        self.cur1.execute(sql.SQL("SELECT * FROM owner_db WHERE {} = %s;").format(sql.Identifier(strg)), (selection_val, ))
        rows=self.cur1.fetchall()

        for row in rows:
            t_list_FMA.append(row[1])
            t_list_workingCirc.append(row[2])

        wCircle_combo_list = [x for x in list(set(t_list_workingCirc)) if x is not None]
        FMA_combo_list = list(set(t_list_FMA))

        #Populate the rest of the fields
        self.FMA_combo['values'] = [x for x in FMA_combo_list if x is not None]
        self.wCircle_combo['values'] = [x for x in wCircle_combo_list if x is not None]

        #Populate the combo box with the initial value
        try:
            self.wCircle_combo.set(str(wCircle_combo_list[0]))
        except:
            self.wCircle_combo.set('')
        try:
            self.FMA_combo.set(str(FMA_combo_list[0]))
        except:
            self.FMA_combo.set('')

    def Reset_button(self):

        init_list_Licensee =[]
        init_list_haulingcontractor=[]
        self.cur1.execute("SELECT * FROM trucker_DB")
        rows = self.cur1.fetchall()
        for row in rows:
            if row[0] is not None:
                init_list_Licensee.append(row[0])
            if row[5] is not None:
                init_list_haulingcontractor.append(row[5])

        self.init_list_Licensee = list(set(init_list_Licensee))
        self.init_list_haulingcontractor = list(set(init_list_haulingcontractor))

        self.owner_combo['values'] = self.init_list_Licensee
        self.owner_combo.set(self.init_list_Licensee[0])
        self.hauledBy_combo['values'] =self.init_list_haulingcontractor
        self.hauledBy_combo.set(self.init_list_haulingcontractor[0])

        self.block_entry.delete(0,'end')
        self.block_entry.insert(0,'')

        self.wCircle_combo.set('')

        self.logCo_combo.set('')
        self.truckLicense_combo.set('')
        self.truckNum_combo.set('')
        self.TM9_entry.delete(0,'end')

        self.gen_timeIn.config(text = '----')
        self.gen_timeOut.config(text = '----')
        self.label_scaleTare.config(text = '----')
        self.label_scaleNet.config(text = '----')
        self.label_scaleGross.config(text = '----')
        self.gen_date.config(text = '----')

    def WeighIN(self):

        try:
            ser = serial.Serial('/dev/ttyUSB0',9600)
            str_weight = ser.readline()
            self.gross_weight =  str_weight.split()[1]

        except:
            self.gross_weight =  100

        self.date_now = str(datetime.datetime.now().date())
        self.timeIn_now = str(datetime.datetime.now().strftime("%H:%M:%S"))
        self.gen_date.config(text = self.date_now )
        self.gen_timeIn.config(text = self.timeIn_now)
        self.label_scaleGross.config(text = str(self.gross_weight))

        self.cur1.execute(sql.SQL("SELECT poploadslip,count FROM testscale WHERE {} = %s;").format(sql.Identifier('poploadslip')), (self.popLoad_DD_val.get(),))
        a = self.cur1.fetchall()

        try:
            self.new_popCount = int(a[-1][1])+1
        except:
            self.new_popCount = 1
        self.label_popCount.config(text = str(self.new_popCount) )

        if self.sample_DD_Val.get()=='No':
            binary_sample = 0
        else:
            binary_sample = 1

        #update Data base
        Weighin_dict = {
                    'daterecieved': self.date_now,
                    'poploadslip' : int(self.popLoad_DD_val.get()),
                    'count' : self.new_popCount,
                    'sampleloads' : binary_sample,
                    'tm9_ticket' : self.TM9_entry.get(),
                    'owner' : self.owner_combo_val.get(),
                    'disposition_fmanum' : self.FMA_combo_val.get(),
                    'workingcircle' : self.wCircle_combo_val.get(),
                    'blocknum' : self.block_entry.get(),
                    'loggingco' : self.logCo_combo_val.get(),
                    'haulingcontractor' : self.hauledBy_combo_val.get(),
                    'truckplate' : self.truckLicense_combo_val.get(),
                    'trucknum' : self.truckNum_combo_val.get(),
                    'truckaxle' : int(self.axle_DD_Val.get()),
                    'grossweight' : self.gross_weight,
                    'timeIn'  :     self.timeIn_now,

                   }

        columns = Weighin_dict.keys()
        values = [Weighin_dict[column] for column in columns]

        insert_statement = 'INSERT INTO testscale (%s) VALUES %s'

        self.cur1.execute(insert_statement, (AsIs(','.join(columns)), tuple(values)))

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.mainApp = WeighOutWindow(self.newWindow,self.cur1)

# Second Window For Weigh out
class WeighOutWindow:

    def __init__(self, master,curs):

        self.master = master
        self.cur = curs
        self.master.geometry("800x500")
        self.WeighOutButton = Button(self.master, text = 'Weigh\nOut', width = 25, height=25,command=self.WeighOUT)

        #Define Combobox

        #Layout Widgets
        self.WeighOutButton.pack()


    def WeighOUT(self):
        try:
            ser = serial.Serial('/dev/ttyUSB0',9600)
            str_weight = ser.readline()
            self.tare_weight =  str_weight.split()[1]
        except:
            self.tare_weight = 50

        self.cur.execute("SELECT haulingcontractor,trucknum,netweight,grossweight FROM testscale WHERE tareweight IS NULL;")
        rows = self.cur.fetchall()
        haulList=[]
        truckList=[]
        netList=[]
        grossList=[]

        for row in rows:
            haulList.append(row[0])
            truckList.append(row[1])
            netList.append(row[2])
            grossList.append(row[3])

        hauledBy_combo_val = StringVar()
        truckNum_combo_val = StringVar()

        self.truckNum_combo = ttk.Combobox(self.master,textvariable = truckNum_combo_val)
        self.truckNum_combo['values'] = haulList
        self.truckNum_combo.set(haulList[0])

        self.hauledBy_combo = ttk.Combobox(self.master, textvariable = hauledBy_combo_val)
        self.hauledBy_combo['values'] = truckList
        self.hauledBy_combo.set(truckList[0])

        indx_weight = truckList.index(hauledBy_combo.current())
        print(indx_weight)
        # net_weight = gross_weight-self.tare_weight
        #
        # timeOut_now = str(datetime.datetime.now().strftime("%H:%M:%S"))
        # self.gen_timeOut.config(text = timeOut_now)
        # WeighOut_dict = {
        #             'tareweight': self.tare_weight,
        #             'netweight' : self.net_weight,
        #             'timeOut'   : timeOut_now
        #            }
        #
        # columns = WeighOut_dict.keys()
        # values = [WeighOut_dict[column] for column in columns]
        #
        # insert_statement = 'INSERT INTO testscale (%s) VALUES %s'
        #
        # self.cur1.execute(insert_statement, (AsIs(','.join(columns)), tuple(values)))
        self.master.destroy()


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main loop keep at bottom~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

def main():

    root = Tk()

    mainApp = GUIatFrontDesk(root)
    # root.attributes('-fullscreen',True)
    root.geometry("1200x700")
    root.mainloop()

if __name__ == '__main__':
    main()
