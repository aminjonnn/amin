from tkinter import *

root = Tk()
root.title("Урок по Tkinter")
root.geometry("400x200+700+500")
root.resizable(width=False, height=False)

value = StringVar()

def test():
    get = value.get()
    l["text"] = get

l = Label(text="Тестовый текст")
e = Entry(textvariable=value)
b = Button(command=test, text="")
l.pack(side=BOTTOM)
e.pack()
b.pack()