from tkinter import *

root = Tk()

Button1 = Button(root, text="Button1", fg="red")
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)  # Ask for a blank field. Il faut ensuite préciser où est-ce qu'on le met.
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
Button1.grid(center=LEFT, row=2, sticky=E)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()
