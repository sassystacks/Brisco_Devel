from Tkinter import *

root = Tk()

f = Frame(root, bg = "orange", width = 500, height = 500)
f.pack(side=LEFT, expand = 1, fill= Y)

f3 = Frame(f, bg = "red",padx = 200, pady=50)
f3.pack(side=LEFT, expand = 1,fill=BOTH)

f2 = Frame(root, bg = "black")
f2.pack(side=LEFT, fill = BOTH)

b = Button(f2, text = "test")
b.pack()

b = Button(f3, text = "1", bg = "red")
b.grid(row=1, column=3)
b2 = Button(f3, text = "2")
b2.grid(row=1, column=4)
b3 = Button(f3, text = "2")
b3.grid(row=2, column=0)

root.mainloop()
