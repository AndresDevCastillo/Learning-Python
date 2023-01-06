from tkinter import *

Window = Tk()
elemento = StringVar()
lista = Listbox(Window)
for item in ["Manzana", "Pera", "Piña"]:
 lista.insert(END, item)
lista.pack()
label = Label(text="Fruta")
label.pack()
Window.mainloop()