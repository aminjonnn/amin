# Creating address book using Tkinter
from tkinter import *

root = Tk()

root.geometry('900x800')

datas = []

def add():
    global datas
    datas.append([Name.get(),Number.get(),address.get(1.0, "end-1c")])
    update_book()

def view():
    Name.set(datas[int(select.curselection()[0])][0])
    Number.set(datas[int(select.curselection()[0])][1])
    address.delete(1.0,"end")
    address.insert(1.0, datas[int(select.curselection()[0])][2])

def delete():
    del datas[int(select.curselection()[0])]
    update_book()

def reset():
    Name.set('')
    Number.set('')
    address.delete(1.0, "end")

def update_book():
    select.delete(0, END)
    for n,p,a in datas:
        select.insert(END, n)

Name = StringVar()
Number = StringVar()

# Frames
frame = Frame()
frame.pack(pady=10)

frame1 = Frame()
frame1.pack()

frame2 = Frame()
frame2.pack(pady=10)

# Adding elements into frames
Label(frame, text='Name', font="arial 12 bold").pack(side=LEFT)
Entry(frame, textvariable = Name, width=70).pack()

Label(frame1, text='Phone Number', font="arial 12 bold").pack(side=LEFT)
Entry(frame1, textvariable = Number, width=65).pack()

Label(frame2, text='Address', font="arial 12 bold").pack(side=LEFT)
address = Text(frame2, width=37, height=10)
address.pack()

# Adding buttons for functions
Button(root, text="Add    ", font="arial 12 bold",command=add).place(x=0, y=270)
Button(root, text="Open  ", font="arial 12 bold",command=view).place(x=0, y=310)
Button(root, text="Delete", font="arial 12 bold",command=delete).place(x=0, y=350)
Button(root, text="Reset ", font="arial 12 bold",command=reset).place(x=0, y=390)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=65, y=260)

root.mainloop()