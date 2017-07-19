from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import os
from Connect_Brisco_DB import Connect_DB
from extractCSV import ExtractCSV
from datetime import datetime, date, time
from PIL import Image, ImageTk
from psycopg2.extensions import AsIs

class CindyProgram:
    def __init__(self,master):

        cwd = os.getcwd()

        self.master = master

        self.Connect_Brisco_DB = Connect_DB('postgres','postgres','192.168.1.214','crunchyAAA32')
        self.cur1 = self.Connect_Brisco_DB.crsr()

        self.img = Image.open("Brisco_logo.png")
        self.tk_img = ImageTk.PhotoImage(self.img)

        self.frame1 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame1.grid(column=0, row=0,padx=50)
        self.label_image = Label(self.frame1,image=self.tk_img,borderwidth=2,relief='raised')
        #Layout Widgets frame 1
        self.label_image.grid(row=1,column=0,sticky=E,pady=70,padx=70)
        #initialize frames

        self.frame2 = Frame(self.master,borderwidth =2,relief='raised',padx=50,pady=20)
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame3.grid(row=0,column=1,sticky='nsew',pady=50)
        self.frame4 = Frame(self.master,borderwidth =5,relief='raised')
        self.frame4.grid(row=1,column=1,sticky='nsew',pady=50)

        # Label Widgets

        self.label_year = Label(self.frame2,text ="Year")
        self.label_month = Label(self.frame2,text ="Month")
        self.label_day = Label(self.frame2,text ="Day")
        self.label_folder = Label(self.frame2,text ="Folder")
        self.label_Fname = Label(self.frame2, text="Filename")

        # Button widgets
        self.button_printGov = Button(self.frame2, text="Gov CSV",command=self.Create_GovCSV,bg='green')
        self.button_barkies = Button(self.frame2, text="Full Barkies",command=self.Create_barkiesCSV,bg='green')
        self.button_VbyS = Button(self.frame2, text="Volume by Supplier",command=self.Create_VbySCSV,bg='green')
        self.Dir_to_Save = Button(self.frame2, text = "Browse", command=self.Browse_dir)

        # text entry Widgets
        self.Dir_entry = Entry(self.frame2)
        self.Year_entry = Entry(self.frame2)
        self.Fname_entry = Entry(self.frame2)

        #Drop down menu Widgets
        self.DD_L_month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
                                'Sep','Oct','Nov','Dec']

        # self.DD_month = self.Create_DropDown()
        self.var1 = StringVar()
        self.test_dd = self.Create_DropDown(self.var1,self.DD_L_month,self.frame2)

        #initial values in entry boxes
        self.Dir_entry.insert(0,cwd)
        self.Year_entry.insert(0,"2017")

        self.Dir_entry_row = 1
        self.Fname_entry_row = 2

        #Layout Widgets frame 2
        self.label_folder.grid(row=1,column=0,sticky=W)
        self.Dir_entry.grid(row=1,column=1)
        self.Dir_to_Save.grid(row=1,column=3,sticky=E,padx=(20,0))
        self.label_Fname.grid(row=2, column=0,sticky=W)
        self.Fname_entry.grid(row=2, column=1,sticky=E)
        self.label_month.grid(row=3,column=0,pady=(20,0))
        self.label_year.grid(row=3,column=1,pady=(20,0))
        self.Year_entry.grid(row=4,column=1)
        self.test_dd.grid(row=4, column= 0)
        self.button_printGov.grid(row=5, column= 3,padx=20)
        self.button_barkies.grid(row=6, column = 3)
        self.button_VbyS.grid(row=6, column = 4)
        self.label_CSV = Label(self.frame2,text='Export SpreadSheets',relief='sunken')
        self.label_CSV.grid(row=0,column=1,pady=(0,20))

        #Start Frame 3
        self.label_frame3= Label(self.frame3,text='Edit Database',relief='sunken')
        self.label_frame3.grid(row=0, column=1,pady=25)

        self.Edit_DD_lst = ['Block #','All','Date','Population','Load Slip #','Sample Load','TM9 Ticket','Owner',
            'Disposition/FMA #','Working Circle','Logging Co.','Hauling Contractor','Truck License Plate #',
            'Truck #','Truck Axle','Gross Weight','Tare Weight','Net Weight']

        #Labels for frame 3
        self.label_searchBy = Label(self.frame3,text='TM9 to Search for')
        self.label_Colchange = Label(self.frame3,text='Value to Edit')
        self.label_valtoEnter = Label(self.frame3,text='New Value')

        #Widgets for menus for frame 3
        self.confirmEdit = Button(self.frame3, text = 'Confirm\nEdit',command=self.EditDB,bg='green')
        self.var_for_edit = StringVar()
        self.dd_edit_db = self.Create_DropDown(self.var_for_edit, self.Edit_DD_lst,self.frame3)
        self.enterTM9_forEdit = Entry(self.frame3)
        self.replace_val = Entry(self.frame3)

        #Layout for frame 3
        self.confirmEdit.grid(row=3,column=0,padx=30,pady=20)
        self.label_searchBy.grid(row=1,column=0)
        self.label_Colchange.grid(row=1,column=1)
        self.dd_edit_db.grid(row=2,column=1)
        self.enterTM9_forEdit.grid(row=2,column=0,padx=30)
        self.label_valtoEnter.grid(row=1,column=3,padx=30)
        self.replace_val.grid(row=2,column=3,padx=30,pady=30)

        #Labels for Frame 4
        labellist = ['TM9','Total Volume Barkies','Avg pc Barkies','Net Wgt',
                    '# of Pcs','conversions','Total Volume SawLogs','Avg pc Sawlogs',
                    'Sawlogs/Returns','Pole Material','rejects']

        self.label_frame4 = Label(self.frame4, text='Input Scaler Data',relief='sunken')
        indx = 0
        self.inputTM9_label = Label(self.frame4, text = str(labellist[indx]),padx=10)
        indx = indx+1
        self.TotalVol_label = Label(self.frame4, text = labellist[indx],padx=10)
        indx = indx+1
        self.AvgpcBark_label = Label(self.frame4, text = labellist[indx],padx=10)
        indx = indx+1
        self.NetWgt_label = Label(self.frame4, text = labellist[indx],padx=10)
        indx = indx+1
        self.numPcs_label = Label(self.frame4, text = labellist[indx],padx=10)
        indx = indx+1
        self.Conversion_label = Label(self.frame4, text = labellist[indx],padx=10)
        indx = indx+1
        self.TotV_label = Label(self.frame4, text = labellist[indx],padx=10)
        indx = indx+1
        self.AvgpcSaw_label = Label(self.frame4, text = labellist[indx],padx=10)
        indx = indx+1
        self.returns_label = Label(self.frame4, text = labellist[indx],padx=10)
        indx = indx+1
        self.poleMat_label = Label(self.frame4, text = labellist[indx],padx=10)
        indx = indx+1
        self.rejects_label = Label(self.frame4, text = labellist[indx],padx=10)


        #Widgets for Frame 4
        self.confirmEntry = Button(self.frame4, text = 'Confirm\nEntry',command=self.EnterScaler,bg='green')
        self.enterTM9_enter = Entry(self.frame4)
        self.enterTM9_enter.config(bd=5,relief = 'sunken')
        self.label_frame4 = Label(self.frame4, text='Input Scaler Data',relief='sunken')
        self.inputTM9_enter = Entry(self.frame4)
        self.TotalVol_enter = Entry(self.frame4)
        self.AvgpcBark_enter = Entry(self.frame4)
        self.NetWgt_enter = Entry(self.frame4)
        self.numPcs_enter = Entry(self.frame4)
        self.Conversion_enter = Entry(self.frame4)
        self.TotV_enter = Entry(self.frame4)
        self.AvgpcSaw_enter = Entry(self.frame4)
        self.returns_enter = Entry(self.frame4)
        self.poleMat_enter = Entry(self.frame4)
        self.rejects_enter = Entry(self.frame4)

        #Layout for frame 4
        rownum = 4
        padX = 10
        self.confirmEntry.grid(row=0,column=4,pady=30)
        self.label_frame4.grid(row=0,column=2,pady=20)
        self.inputTM9_enter.grid(row=1,column=0,padx=padX, pady=(0,20))
        self.TotalVol_enter.grid(row=rownum,column=0,padx=padX)
        self.AvgpcBark_enter.grid(row=rownum,column=1,padx=padX)
        self.NetWgt_enter.grid(row=rownum,column=2,padx=padX)
        self.numPcs_enter.grid(row=rownum,column=3,padx=padX)
        self.Conversion_enter.grid(row=rownum,column=4,padx=padX)
        self.TotV_enter.grid(row=(rownum+2),column=0,padx=padX,pady=10)
        self.AvgpcSaw_enter.grid(row=(rownum+2),column=1,padx=padX,pady=10)
        self.returns_enter.grid(row=(rownum+2),column=2,padx=padX,pady=10)
        self.poleMat_enter.grid(row=(rownum+2),column=3,padx=padX,pady=10)
        self.rejects_enter.grid(row=(rownum+2),column=4,padx=padX,pady=10)

        #Label layout for frame 4
        rownum = 3
        self.inputTM9_label.grid(row=0 ,column=0,sticky=S)
        self.TotalVol_label.grid(row=rownum ,column=0)
        self.AvgpcBark_label.grid(row=rownum ,column=1)
        self.NetWgt_label.grid(row=rownum ,column=2)
        self.numPcs_label.grid(row=rownum ,column=3)
        self.Conversion_label.grid(row=(rownum ),column=4)
        self.TotV_label.grid(row=(rownum+2 ) ,column=0)
        self.AvgpcSaw_label.grid(row=(rownum+2 ), column=1)
        self.returns_label.grid(row=(rownum+2 ), column=2)
        self.poleMat_label.grid(row=(rownum+2 ), column=3)
        self.rejects_label.grid(row=(rownum+2 ) ,column=4)

        self.master.bind('<Escape>', lambda e: self.master.destroy())
        
    def Create_LoadSumCSV(self):
        pass

    def Create_GovCSV(self):

<<<<<<< HEAD
        B = self.setup_extract('Load','Summary')
=======
        B = self.setup_extract()
>>>>>>> ce4a81d57d2225f0305646297ab3fc8fcd65491e
        B.WriteGovCSV()

    def Create_barkiesCSV(self):

<<<<<<< HEAD
        B = self.setup_extract('Barkies','Hauling')
        B.WriteHaulSummaryCSV()

    def Create_VbySCSV(self):
        B = self.setup_extract('Volume','by','Supplier')
=======
        B = self.setup_extract()
        B.WriteHaulSummaryCSV()

    def Create_VbySCSV(self):
        B = self.setup_extract()
>>>>>>> ce4a81d57d2225f0305646297ab3fc8fcd65491e
        B.WriteVbySCSV()

    def setup_extract(self,*args):

        dirPrint =self.Dir_entry.get()
        t_month = self.var1.get()
        month_num =self.DD_L_month.index(t_month)+1
        year_num = int(self.Year_entry.get())
        self.Fname_entry.delete(0,'end')
        s = "_"
        t_year = self.Year_entry.get()

        lst = []
        if args:
            for arg in args:
                lst.append(arg)
            lst_new = [t_month,t_year] + lst

            seq = tuple(lst_new)
        else:
            seq = (t_month,t_year)

        t_fname1 = s.join(seq)
        t_fname2 = ".csv"
        t_fname = t_fname1 + t_fname2
        self.Fname_entry.insert(0,t_fname)
        full_file = os.path.join(dirPrint,t_fname)
        DB_instance=self.Connect_Brisco_DB
        A=ExtractCSV(DB_instance,full_file,month_num,year_num)
        return A

    def Browse_dir(self):

        directory = tkFileDialog.askdirectory()
        self.Dir_entry.delete(0,'end')
        self.Dir_entry.insert(0,directory)

    def Create_DropDown(self,DDvar,DDLst,frameName):

        DDvar.set(DDLst[0])
        DDmenu = OptionMenu(frameName, DDvar, *DDLst)
        return DDmenu

    def EditDB(self):

        DB_list = ['blocknum',
                    'All',
                    'daterecieved',
                    'poploadslip',
                    'count',
                    'sampleloads' ,
                    'tm9_ticket',
                    'owner' ,
                    'disposition_fmanum' ,
                    'workingcircle' ,
                    'loggingco' ,
                    'haulingcontractor',
                    'truckplate',
                    'trucknum' ,
                    'truckaxle' ,
                    'grossweight',
                    'tareweight',
                    'netweight',]

        list_for_int = [
                    'poploadslip',
                    'count',
                    'truckaxle' ,
                    'grossweight',
                    'tareweight',
                    'netweight',]

        get_val = self.replace_val.get()
        dict_for_Edit = dict(zip(self.Edit_DD_lst,DB_list))
        val_to_chng = dict_for_Edit[self.var_for_edit.get()]

        TM9_strng = self.enterTM9_forEdit.get()

        if val_to_chng == 'All':
            sql_statement = 'DELETE FROM barkies2018_db WHERE tm9_ticket = %s;'
            self.cur1.execute(sql_statement, (TM9_strng,))

        else:
            is_int = [int(get_val) for x in list_for_int if val_to_chng in x]

            if not is_int:
                final_replace = get_val

            else:
                final_replace = is_int[0]

            sqlt = 'UPDATE barkies2018_db SET (%s) = %s WHERE tm9_ticket = %s;'
            print self.cur1.mogrify(sql, (AsIs(val_to_chng), (get_val,), TM9_strng))
            self.cur1.execute(sql_statement, (AsIs(val_to_chng), (get_val,), TM9_strng))


    def EnterScaler(self):

        Update_Scaler_keys = ['numpcsreceived' ,
          'logsreject'  ,
          'totalvol'  ,
          'avgpc'  ,
          'conversion'  ,
          'totalvolsaw' ,
          'avgpcsaw'   ,
          'returnssaw'  ,
          'polemat' ]
        Update_Scaler_values = [self.numPcs_enter.get(),self.rejects_enter.get(),self.TotalVol_enter.get(),
                                self.AvgpcBark_enter.get(),self.Conversion_enter.get(),self.TotV_enter.get(),
                                self.AvgpcSaw_enter.get(),self.returns_enter.get(),self.poleMat_enter.get()]
        Update_Scaler_values  = [x if x!= '' else None for x in Update_Scaler_values ]
        dictionary = dict(zip(Update_Scaler_keys, Update_Scaler_values))
        columns = dictionary.keys()
        values = [dictionary[column] for column in columns]
        insert_statement = 'UPDATE barkies2018_db SET (%s) = %s WHERE tm9_ticket = %s;'
        strng = self.inputTM9_enter.get()
        self.cur1.execute(insert_statement, (AsIs(','.join(columns)), tuple(values), strng))

    def killProcess(self):
        pass

    def confirm(self):
        pass

def main():
    root = Tk()
    root.geometry("1300x700")
    app = CindyProgram(root)

    root.mainloop()

if __name__ == '__main__':
        main()
