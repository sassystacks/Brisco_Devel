from Tkinter import *
import ttk, tkFont, tkMessageBox
import itertools
import datetime
from Connect_Brisco_DB import Connect_DB
from DB_searchandFill import DB_search
from psycopg2 import sql
import serial
from psycopg2.extensions import AsIs

class GUIatFrontDesk:

    def __init__(self,master):

        from PIL import Image, ImageTk
        self.master = master

        self.ip_add = '192.168.1.214'
        self.psswd  = 'crunchyAAA32'

        self.init_list_truck = self.initializeLists('truckers_db')
        self.init_list_owner = self.initializeLists('owner_db')

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~ Initialize Frames ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''

        self.frame1 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame1.grid(row=0,column=0,sticky='ew')

        self.frame2 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame2.grid(row=1,column=0,sticky='ew',ipady=20)

        self.frame3 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame3.grid(row=2,column=0,sticky='ew',ipady=20)

        self.frame4 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame4.grid(row=3,column=0,sticky='ew',ipady=20)

        self.frame5 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame5.grid(row=0,column=1,sticky='nsew')

        self.frame6 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame6.grid(row=1,column=1,sticky='nsew',rowspan=3)

        self.frame7 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame7.grid(row=0,column=2,rowspan=4,sticky='nwes')

        #list of dictionaries for trucks in the yard and info attached to them
        self.Lst_truckInfo = []

        '''
        ~~~~~~~~~~~~~~~ Create initial vals for comboboxes ~~~~~~~~~~~~~~~
        '''
        self.owner_combo_val = StringVar()
        self.FMA_combo_val = StringVar()
        self.wCircle_combo_val = StringVar()
        self.block_combo_val = StringVar()
        self.logCo_combo_val = StringVar()
        self.truckLicense_combo_val = StringVar()
        self.truckNum_combo_val = StringVar()
        self.axle_combo_val = StringVar()
        self.hauledBy_combo_val = StringVar()
        self.popDD_val = StringVar()
        self.sampleDD_val = StringVar()
        self.loggingCo_combo_val = StringVar()

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~  Frame 1  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        framenum = 1

        framenum = self.frame1
        colm = 0
        rown = 0
        f1_lst_labels = ["TM9 Ticket","Block #","Pieces"]

        for strng in f1_lst_labels:
            self.create_place_label(framenum,strng,rown,colm,("Courier", 20,"bold"),W)
            rown = rown + 1

        colm = 1
        rown = 0
        pddx = (90,0)
        self.TM9_entry_var = StringVar()
        self.numPieces_entry_var = StringVar()
        self.blockNum_entry_var = StringVar()

        self.TM9_entry = self.create_place_entry(framenum,self.TM9_entry_var, rown, colm, ("Courier", 16,"bold"),20,E,pddx)
        self.TM9_entry.bind('<Key>',self.activate_weighIN)
        rown = rown + 1
        self.blockNum_entry = self.create_place_entry(framenum,self.blockNum_entry_var, rown, colm, ("Courier", 16,"bold"),40,E,pddx)
        rown = rown + 1
        self.numPieces_entry = self.create_place_entry(framenum,self.numPieces_entry_var, rown, colm, ("Courier", 16,"bold"),None,E,pddx)

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~  Frame 2  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''

        framenum = self.frame2
        #labels
        colm = 0
        rown = 0
        f2_lst_labels = ["Truck #","License Plate ","Hauling Contractor","Truck Axle"]

        for strng in f2_lst_labels:
            if rown==0:
                fnt_size=20
            else:
                fnt_size = 16
            self.create_place_label(framenum,strng,rown,colm,("Courier", fnt_size,"bold"),W)
            rown = rown + 1

        List_frame2 = self.initializeLists('truckers_db')


        #Menus
        rown = 0
        colm = 1
        pddx = None
        self.truckNum_combo = self.create_place_combo(framenum,self.init_list_truck[0],self.truckNum_combo_val,rown,colm,("Courier", 20,"bold"),"truck",W,pddx,'normal')
        self.truckNum_combo.bind("<<ComboboxSelected>>", lambda event: self.update_lists(event,'truck',self.truckNum_combo,self.init_list_truck))

        rown = rown + 1
        self.truckLicense_combo = self.create_place_combo(framenum,self.init_list_truck[1],self.truckLicense_combo_val,rown,colm,("Courier", 16,"bold"),"truck",W,pddx,'disabled')
        rown = rown + 1
        self.hauledBy_combo = self.create_place_combo(framenum,self.init_list_truck[2],self.hauledBy_combo_val,rown,colm,("Courier", 16,"bold"),"truck",W,pddx,'disabled')
        rown = rown + 1
        self.axle_combo = self.create_place_combo(framenum,self.init_list_truck[3],self.axle_combo_val,rown,colm,("Courier", 16,"bold"),"truck",W,pddx,'disabled')

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~  Frame 3  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''

        framenum = self.frame3
        colm = 0
        rown = 0
        f3_lst_labels = ["Owner","FMA #","Working Circle","Logging Contractor"]
        for strng in f3_lst_labels:
            if rown==0:
                fnt_size=20
            else:
                fnt_size = 16
            self.create_place_label(framenum,strng,rown,colm,("Courier", fnt_size,"bold"),W)
            rown = rown + 1

        rown = 0
        colm = 1
        pddx = None
        self.init_list_owner_set =list(set(self.init_list_owner[0]))
        self.owner_combo = self.create_place_combo(framenum,self.init_list_owner_set,self.owner_combo_val,rown,colm,("Courier", 20,"bold"),"owner",W,pddx,'normal')
        self.owner_combo.bind("<<ComboboxSelected>>", lambda event: self.update_lists(event,'owner',self.owner_combo,self.init_list_owner_set))

        rown = rown + 1
        self.FMA_combo = self.create_place_combo(framenum,self.init_list_owner[1],self.FMA_combo_val,rown,colm,("Courier", 16,"bold"),"owner",W,pddx,'disabled')
        rown = rown + 1
        self.wCircle_combo = self.create_place_combo(framenum,self.init_list_owner[2],self.wCircle_combo_val,rown,colm,("Courier", 16,"bold"),"owner",W,pddx,'disabled')
        rown = rown + 1
        self.loggingCo_combo = self.create_place_combo(framenum,self.loggingco_list,self.loggingCo_combo_val,rown,colm,("Courier", 16,"bold"),"owner",W,pddx,'disabled')
        rown = rown + 1
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~  Frame 4  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        framenum = self.frame4
        colm = 0
        rown = 0
        f4_lst_labels = ["Population","Sample Load"]

        for strng in f4_lst_labels:
            self.create_place_label(framenum,strng,rown,colm,("Courier", 20,"bold"),W)
            rown = rown + 1
        lst_pop = ['726','720','730','740','750','760','780','785']
        lst_sample = ['No','Yes']

        colm = 1
        rown = 0
        paddx = (180,0)
        self.popDD = self.create_place_dropdown(framenum, lst_pop, self.popDD_val , rown, colm, ("Courier", 20,"bold"),'ew',paddx)
        rown = rown + 1
        self.sampleDD = self.create_place_dropdown(framenum, lst_sample , self.sampleDD_val , rown, colm, ("Courier", 20,"bold"),'ew',paddx)

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~  Frame 5  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        framenum = self.frame5
        colm = 0
        rown = 0
        f6_lst_labels = ["Date: ","Time in: ","Time out: ","Gross Weight: ","Tare Weight: ","Net Weight: ","Load Slip #: "]

        self.dict_labels = {}
        for strng in f6_lst_labels:
            self.create_place_label(framenum,strng,rown,colm,("Courier", 16),E)
            self.create_place_label(framenum,'',rown,colm+1,("Courier", 16),'ew')
            rown = rown + 1


        '''
        ~~~~~~~~~~~~~~~~~~~~~~~  Frame 6  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''

        framenum = self.frame6

        self.orig_colour = 'light grey'
        self.truckin_colour = 'orange'

        self.label_lstbox = Label(framenum, text = "Trucks to Weigh Out", borderwidth=2,relief='ridge')
        self.label_lstbox.config(font=("Courier", 20,"bold"),bg=self.orig_colour)
        self.label_lstbox.pack(side=TOP,expand=Y)
        self.TrucksInYard = Listbox(framenum)
        self.TrucksInYard.config(font=("Courier", 20,"bold"),bg=self.orig_colour)
        self.TrucksInYard.pack(side=TOP,expand=Y)
        self.TrucksInYard.bind("<<ListboxSelect>>", self.enable_weighOut)


        '''
        ~~~~~~~~~~~~~~~~~~~~~~~  Frame 7  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        framenum = self.frame7

        self.img = Image.open("Brisco_logo.png")
        self.tk_img = ImageTk.PhotoImage(self.img)

        self.label_image = Label(framenum,image=self.tk_img ,relief='groove')
        self.label_image.config(height = 250, width =250)
        self.label_image.grid(row = 0, column = 0, columnspan=2)

        pddx =35
        pddy = (15,0)
        dimh = 1
        dimw = 10
        rown = 1
        colm = 0
        self.WeighIN = self.create_place_button(framenum, 'Weigh In',1, 0, ("Courier", 22, "bold"),(100,0),pddx,dimh,dimw,E,self.weighIN)
        self.WeighOUT = self.create_place_button(framenum, 'Weigh Out', 2, 0, ("Courier", 22, "bold"),pddy,pddx,dimh,dimw,E,self.weighOUT)
        self.clearEntry = self.create_place_button(framenum, 'Clear', 3, 0, ("Courier", 22, "bold"),pddy,pddx,dimh,dimw,E,self.clearEntry)
        # self.WeighIN.config(state='Disabled')
        self.WeighOUT.config(state='disabled',bg='grey')
        self.WeighIN.config(state='disabled',bg='grey')
        self.clearEntry.config(bg='ivory4')

        '''
        ~~~~~~~~~~~~~~~  close program with escape key  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        self.master.bind('<Escape>', lambda e: self.master.destroy())

    '''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GUI Methods ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
    def clearEntry(self):
        self.TM9_entry_var.set('')
        self.blockNum_entry_var.set('')
        self.numPieces_entry_var.set('')
        self.WeighIN.config(state='disabled',bg='grey')
	    self.WeighOUT.config(state='disabled',bg='grey')

    def activate_weighIN(self,event):
        self.WeighIN.config(state='normal',bg='green')
	self.WeighOUT.config(state='disabled',bg='grey')


    def enable_weighOut(self,event):
        self.WeighIN.config(state='disabled',bg='grey')
        self.WeighOUT.config(state='normal',bg='green')

    def weighIN(self):
        Connect_Brisco_DB = Connect_DB('postgres','postgres',self.ip_add,self.psswd)
        cur1 = Connect_Brisco_DB.crsr()

        try:
            ser = serial.Serial('/dev/ttyUSB0',9600)
            str_weight = ser.readline()
            self.gross_weight =  str_weight.split()[1]
            self.gross_weight =int(self.gross_weight)
            ser.close()
        except:
            self.gross_weight =  100

        self.date_now = str(datetime.datetime.now().date())
        self.timeIn_now = str(datetime.datetime.now().strftime("%H:%M:%S"))

        cur1.execute(sql.SQL("SELECT poploadslip,count FROM barkies2018_db WHERE {} = %s;").format(sql.Identifier('poploadslip')), (self.popDD_val.get(),))
        a = cur1.fetchall()

        try:
            self.new_popCount = int(a[-1][1])+1
        except:
            self.new_popCount = 1

        if self.sampleDD_val.get()=='No':
            binary_sample = 0
        else:
            binary_sample = 1

        #Set labels after weign in
        label_list = [self.date_now,self.timeIn_now,'',str(self.gross_weight),'','',str(self.new_popCount) ]
        rown = 0
        for labl in label_list:

            self.create_place_label(self.frame5, labl, rown, 1, ("Courier", 16), E)
            rown = rown + 1

        self.TrucksInYard.insert(END,self.truckNum_combo_val.get())
        self.TrucksInYard.config(bg=self.truckin_colour)
        self.label_lstbox.config(bg=self.truckin_colour)


        #update Data base
        Weighin_dict = {
                    'daterecieved': self.date_now,
                    'poploadslip' : int(self.popDD_val.get()),
                    'count' : self.new_popCount,
                    'sampleloads' : binary_sample,
                    'tm9_ticket' : self.TM9_entry.get(),
                    'owner' : self.owner_combo_val.get(),
                    'disposition_fmanum' : self.FMA_combo_val.get(),
                    'workingcircle' : self.wCircle_combo_val.get(),
                    'blocknum' : self.blockNum_entry.get(),
                    'loggingco' : self.logCo_combo_val.get(),
                    'haulingcontractor' : self.hauledBy_combo_val.get(),
                    'truckplate' : self.truckLicense_combo_val.get(),
                    'trucknum' : self.truckNum_combo_val.get(),
                    'truckaxle' : int(self.axle_combo_val.get()),
                    'grossweight' : self.gross_weight,
                    'timeIn'  :     self.timeIn_now,
                    'numpcsreceived' : self.numPieces_entry.get()
                   }

        self.Lst_truckInfo.append(Weighin_dict)
        trucknum_indx = len(self.Lst_truckInfo)-1

        columns = Weighin_dict.keys()
        # values = [Weighin_dict[column] for column in columns]
        values = [None if Weighin_dict[key] == '' else Weighin_dict[key] for key in columns]

        insert_statement = 'INSERT INTO barkies2018_db (%s) VALUES %s'

        #check if previous TM9 same was entered
        check_statement = 'SELECT tm9_ticket FROM barkies2018_db'

        cur1.execute('SELECT tm9_ticket FROM barkies2018_db')
        check_tm9 = cur1.fetchall()

        keys = ['tm9_ticket','blocknum','numpcsreceived']

        if [item for item in check_tm9 if Weighin_dict['tm9_ticket'] in item]:
            tkMessageBox.showinfo("WHOOPS!","That TM9 already Exists!")
            del self.Lst_truckInfo[trucknum_indx]
            self.TrucksInYard.delete(trucknum_indx)

        elif not any(Weighin_dict[key] for key in keys):
            tkMessageBox.showinfo("WHOOPS!","I think you forgot to enter something!")
            del self.Lst_truckInfo[trucknum_indx]
            self.TrucksInYard.delete(trucknum_indx)
        else:

            try:
                cur1.execute(insert_statement, (AsIs(','.join(columns)), tuple(values)))
                self.change_state(self.truckLicense_combo)
                self.change_state(self.hauledBy_combo)
                self.change_state(self.axle_combo)
                self.change_state(self.FMA_combo)
                self.change_state(self.wCircle_combo)

            except:
                tkMessageBox.showinfo("WHOOPS!","Make sure all values are filled in!")
                # trucknum_indx = next(index for (index, d) in enumerate(self.Lst_truckInfo) if d['trucknum'] == self.TrucksInYard.get(self.TrucksInYard.curselection()))
                del self.Lst_truckInfo[trucknum_indx]
                self.TrucksInYard.delete(trucknum_indx)

	self.WeighOUT.config(state='disabled',bg='grey')
        self.WeighIN.config(state='disabled',bg='grey')
        self.update_colors_truck()
        cur1.close()

    def weighOUT(self):

        Connect_Brisco_DB = Connect_DB('postgres','postgres',self.ip_add,self.psswd)
        cur1 = Connect_Brisco_DB.crsr()
        trucknum_indx = next(index for (index, d) in enumerate(self.Lst_truckInfo) if d['trucknum'] == self.TrucksInYard.get(self.TrucksInYard.curselection()))

        dict_to_fill = self.Lst_truckInfo[trucknum_indx]

        del self.Lst_truckInfo[trucknum_indx]


        self.owner_combo.set(dict_to_fill['owner'])
        self.FMA_combo.set(dict_to_fill['disposition_fmanum'])
        self.wCircle_combo.set(dict_to_fill['workingcircle'])
        self.truckNum_combo.set(dict_to_fill['trucknum'])
        self.truckLicense_combo.set(dict_to_fill['truckplate'])
        self.hauledBy_combo.set(dict_to_fill['haulingcontractor'])
        self.axle_combo.set(dict_to_fill['truckaxle'])
        self.TM9_entry_var.set(dict_to_fill['tm9_ticket'])
        self.blockNum_entry_var.set(dict_to_fill['blocknum'])
        self.numPieces_entry_var.set(dict_to_fill['numpcsreceived'])

        try:
            ser = serial.Serial('/dev/ttyUSB0',9600)
            str_weight = ser.readline()
            self.tare_weight =  str_weight.split()[1]
            self.net_weight = int(dict_to_fill['grossweight'])-int(self.tare_weight)
            ser.close()

        except:
            self.tare_weight = 50
            self.net_weight = int(dict_to_fill['grossweight'])-self.tare_weight

        self.timeOut_now = str(datetime.datetime.now().strftime("%H:%M:%S"))

        label_list = []

        #Set labels after weign in

        label_list = [dict_to_fill['daterecieved'],dict_to_fill['timeIn'],self.timeOut_now,str(dict_to_fill['grossweight']),str(self.tare_weight),str(self.net_weight),dict_to_fill['count'] ]
        rown = 0
        for labl in label_list:

            self.create_place_label(self.frame5, labl, rown, 1, ("Courier", 16), E)
            rown = rown + 1

        self.TrucksInYard.delete(trucknum_indx)

        self.TrucksInYard.config(bg='bisque')
        self.label_lstbox.config(bg='bisque')

        WeighOut_dict = {
                    'tareweight': self.tare_weight,
                    'netweight' : self.net_weight,
                    'timeOut'   : self.timeOut_now
                   }

        columns = WeighOut_dict.keys()
        values = [WeighOut_dict[column] for column in columns]

        insert_statement = 'UPDATE barkies2018_db SET (%s) = %s WHERE tm9_ticket = %s;'
        strng = self.TM9_entry.get()

        cur1.execute(insert_statement, (AsIs(','.join(columns)), tuple(values), strng))

        self.WeighOUT.config(state='disabled',bg='grey')
        self.WeighIN.config(state='disabled',bg='grey')
        self.update_colors_truck()
        cur1.close()

    def update_colors_truck(self):
        if self.Lst_truckInfo:

            self.TrucksInYard.config(bg=self.truckin_colour)
            self.label_lstbox.config(bg=self.truckin_colour)
        else:
            self.TrucksInYard.config(bg=self.orig_colour)
            self.label_lstbox.config(bg=self.orig_colour)

    def select_db(self,table,column,value,entry):

        Connect_Brisco_DB = Connect_DB('postgres','postgres',self.ip_add,self.psswd)
        cur1 = Connect_Brisco_DB.crsr()

        sql = 'SELECT %s FROM %s WHERE %s' % (entry,table,column) + ' = %s'
        cur1.execute(sql, (value, ))

        row = cur1.fetchall()
        cur1.close()
        return row

    def update_lists(self,event,strng,name_combo,Lst):

        var_Selected = name_combo.current()

        if strng == 'owner':
            valToQuery = self.init_list_owner_set[var_Selected]

            self.owner_combo.set(valToQuery)

            #enable the other comboboxes
            self.change_state(self.FMA_combo,1)
            self.change_state(self.wCircle_combo,1)
            self.change_state(self.loggingCo_combo,1)

            vals = self.select_db('owner_db','owner',valToQuery,'*')

            lst_FMA = [val[1] if val[1] is not [None] else '' for val in vals ]
            lst_wCirc = [val[2] if val[2] is not [None] else '' for val in vals ]
            lst_FMA = list(set(lst_FMA))
            lst_wCirc =list(set(lst_wCirc))

            self.FMA_combo['values'] = lst_FMA
            self.wCircle_combo['values'] = lst_wCirc

            self.chk_exist(lst_FMA,self.FMA_combo)
            self.chk_exist(lst_wCirc,self.wCircle_combo)

        elif strng == 'truck':
            valToQuery = self.init_list_truck[0][var_Selected]
            self.truckNum_combo.set(valToQuery)

            #enable the other comboboxes
            self.change_state(self.truckLicense_combo,1)
            self.change_state(self.hauledBy_combo,1)
            self.change_state(self.axle_combo,1)

            vals = self.select_db('truckers_db','trucknum',valToQuery,'*')

            lst_license = [val[1]  for val in vals ]
            lst_haulingco = [val[2]  for val in vals ]
            lst_axle = [val[3]  for val in vals ]

            lst_license = list(set(lst_license))
            lst_haulingco =list(set(lst_haulingco))
            lst_axle =list(set(lst_axle))

            self.truckLicense_combo['values'] = lst_license
            self.hauledBy_combo['values'] = lst_haulingco
            self.axle_combo['values'] = lst_axle

            self.truckLicense_combo.set(lst_license[0])
            self.hauledBy_combo.set(lst_haulingco[0])
            self.axle_combo.set(lst_axle[0])

    def chk_exist(self,lst,combobx):
        #if no value in list makes entry blank
        if lst[0]:
            combobx.set(lst[0])
        else:
            combobx.set('')

    def change_state(self,cmbobx,*args):

        a = str(cmbobx['state'])

        if args:
            a = 'disabled'

        if a == 'disabled':
            ste = 'normal'
        else:
            ste = 'disabled'

        cmbobx.config(state=ste)

    def initializeLists(self,table):
        Connect_Brisco_DB = Connect_DB('postgres','postgres',self.ip_add,self.psswd)
        cur1 = Connect_Brisco_DB.crsr()

        query = 'SELECT * from "{}"'.format(table)
        cur1.execute(query)
        rows = cur1.fetchall()
        rows=sorted(rows)
        sorted_list = map(list, itertools.izip_longest(*rows))
        if table == 'owner_db':
            table1 = 'barkies2018_db'
            query = 'select loggingco from "{}"'.format(table1)
            cur1.execute(query)
            rows = cur1.fetchall()
            t_list  =[str(x[0]) for x in rows]
            self.loggingco_list =list(set(t_list))
        cur1.close()
        return sorted_list

    def create_place_label(self,frme,strng,rownum,columnum,fnt,stcky):

        labl_name = Label(frme, text = '        ')
        labl_name.grid(row=rownum, column=columnum,sticky=stcky)
        labl_name.config(font=fnt, text=strng)
        return labl_name

    def create_place_combo(self,frme,Lst,cmboVal,rownum,columnum,fnt,strng,stcky,pdx,ste):

        bigfont = tkFont.Font(root=frme,family="Courier",size=30, weight='bold')
        frme.option_add("*TCombobox*Listbox*Font", bigfont)

        name_combo = ttk.Combobox(frme,textvariable = cmboVal)
        name_combo.grid(row=rownum, column=columnum,sticky=stcky,padx=pdx)
        name_combo.config(font=fnt,state=ste)
        name_combo['values'] = Lst
        name_combo.set(Lst[1])
        # self.owner_combo.bind("<<ComboboxSelected>>",lambda event: self.DB_Search_n_Fill(event,"owner",self.Connect_Brisco_DB))
        return name_combo

    def create_place_dropdown(self, frme, DD_lst, ddVal, rownum, columnum, fnt,stcky,pdx):

        ddVal.set(DD_lst[0])
        name_DD = OptionMenu(frme, ddVal, *DD_lst)
        name_DD.config(font=fnt,bg='tan')
        name_DD.grid(row=rownum, column=columnum, sticky=stcky,padx=pdx)
        return name_DD

    def create_place_entry(self, frme, txt, rownum, columnum, fnt,pdy,stcky,pdx):

        name_entry = Entry(frme,text=txt)
        name_entry.config(font=fnt)
        name_entry.grid(row=rownum, column=columnum,pady=pdy,sticky=stcky,padx=pdx)
        return name_entry

    def create_place_button(self, frme ,txt_name, rownum, columnum, fnt,pdy,pdx,dimmh,dimmw,stcky,cmmd):

        name_button = Button(frme, text=txt_name, command = cmmd)
        name_button.config(height=dimmh, width=dimmw, activebackground='red',font=fnt)
        name_button.grid(row=rownum, column=columnum, pady=pdy, padx=pdx, sticky = stcky)
        return name_button

    def print_test(self,event,strng,name_combo,Lst):
        var_Selected = name_combo.current()
        selection_val = str(Lst[var_Selected])
        print(strng)
        print(selection_val)


def main():

    root = Tk()
    mainApp = GUIatFrontDesk(root)
    root.attributes('-fullscreen',True)
    #root.geometry("1200x500")
    root.mainloop()

if __name__ == '__main__':
    main()
