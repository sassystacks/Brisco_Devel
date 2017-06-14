from Tkinter import *
from extractCSV import ExtractCSV
from Connect_Brisco_DB import Connect_DB

class CSV_export:

    def __init__(self, master):
        # self.main_container = Frame(master, background="bisque")
        # self.main_container.pack(side="top", fill="both", expand=True)
        self.master = master
        master.title("Export CSV")

        self.month_chosen = 'jan'
        self.entered_number = 0

        self.label1 = Label(master, text="month")
        self.label2 = Label(master, text = self.month_chosen)

        self.export_button = Button(master, text="Export CSV", command=self.export)
        self.export_button.config(bg='green')
        # create dropdown menu for months
        self.lst1 = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
                    'Sep','Oct','Nov','Dec']
        self.var1 = StringVar()
        self.drop = OptionMenu(root,self.var1,*self.lst1)


        # LAYOUT

        self.label1.grid(row=0, column=0, sticky=W)
        self.drop.config(width=10)
        self.drop.grid(row=1, column=0, columnspan=2, rowspan =2, sticky=E+W)
        self.export_button.grid(row=15,column=0,columnspan=2,rowspan=2, sticky=E+W)


    # def validate(self, new_text):
    #     if not new_text: # the field is being cleared
    #         self.entered_number = 0
    #         return True
    #
    #     try:
    #         self.entered_number = int(new_text)
    #         return True
    #     except ValueError:
    #         return False
    #
    # def export_button(self):
    #     dt_selected = self.var1.get()
    #     print(dt_selected)
    #     try:
    #         self.indx_date = self.lst1.index(dt_selected)+1
    #         self.month_chosen = self.lst1[dt_selected]
    #         print(indx_date)
    #     except:
    #         print"Please Select a date"

    def export(self):
        print"hi"

root = Tk()
root.geometry('{}x{}'.format(500, 500))
my_gui = CSV_export(root)
root.mainloop()
