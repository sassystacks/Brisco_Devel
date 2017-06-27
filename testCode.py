from Tkinter import *



class TestButton:

    def __init__(self,root):
        self.v = IntVar()
        self.v.set(1)
        self.A=Radiobutton(master, text="One", variable=self.v, value=1, command=self.changetext).pack(anchor=W)
        self.B=Radiobutton(master, text="Two", variable=self.v, value=2, command=self.changetext).pack(anchor=W)

        self.a ="Func1"
        self.Bigbutton = Button(master,text=self.a, command=self.buttonFunc)
        # self.Bigbutton.bind("<Button-1>", lambda event: self.buttonFunc(event,self.v.get()))
        self.Bigbutton.pack()

    def buttonFunc(self):
        if self.v.get()==1:
            self.buttonFunc1()
        else:
            self.buttonFunc2()

    def buttonFunc1(self):
        self.a = "Func1"
        print(self.a )

    def buttonFunc2(self):

        print(self.a )

    def changetext(self):
        if self.v.get()==1:

            self.a="Func1"
        else:
            self.a = "Func2"
        print(self.v.get())
        self.Bigbutton.config(text=self.a)

master = Tk()
A = TestButton(master)
master.mainloop()
