from Tkinter import *
import ttk, tkFont, tkMessageBox

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.default_bg = self.master.cget('bg')

        Lst = [1,2,3,4,5]
        self.combo1_val = StringVar()
        self.combo2_val = StringVar()
        self.combo3_val = StringVar()
        self.combo4_val = StringVar()

        self.Lbx1 = self.create_place_listbox(self.master,0,0)
        # self.Lbx1.bind("<<ComboboxSelected>>", self.update_lists)

        self.Lbx2 = self.create_place_listbox(self.master,1,0)
        self.Lbx3 = self.create_place_listbox(self.master,2,0)
        self.Lbx4 = self.create_place_listbox(self.master,3,0)

    def create_place_listbox(self,frme,rw,col):
        lbox = Listbox(frme)
        lbox.config(font=("Courier", 16,"bold"),height=10)
        lbox.grid(row = rw, column = col)

        # self.TrucksInYard.bind("<<ListboxSelect>>", self.enable_weighOut)

    def create_place_combo(self,frme,Lst,cmboVal,rownum,columnum):

        bigfont = tkFont.Font(root=frme,family="Courier",size=30, weight='bold')
        frme.option_add("*TCombobox*Listbox*Font", bigfont)

        name_combo = ttk.Combobox(frme,textvariable = cmboVal)
        name_combo.grid(row=rownum, column=columnum)
        name_combo['values'] = Lst
        name_combo.set(Lst[1])
        # self.owner_combo.bind("<<ComboboxSelected>>",lambda event: self.DB_Search_n_Fill(event,"owner",self.Connect_Brisco_DB))
        # name_combo.bind("<<ComboboxSelected>>", lambda event: self.update_lists(event,strng,name_combo,Lst))
        return name_combo


    def update_lists(self,event):
        print self.combo1.get()
        self.change_state(self.combo2)
        self.change_state(self.combo3)
        self.change_state(self.combo4)

    def change_state(self,cmbobx):
        a = str(cmbobx['state'])

        if a == 'disabled':
            ste = 'normal'
        else:
            ste = 'disabled'

        cmbobx.config(state=ste)

def main():
    root = Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
