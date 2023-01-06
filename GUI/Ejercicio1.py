from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def Reiniciar():
    opcion.set(None)
    monitor.config(text="")

Window = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(Window, text="Peugeot", variable=opcion, 
            value='Peugeot', command=seleccionar).pack(anchor=W)

Radiobutton(Window, text="Opel", variable=opcion, 
            value='Opel', command=seleccionar).pack(anchor=W)
Radiobutton(Window, text="Renault", variable=opcion,   
            value='Renault', command=seleccionar).pack(anchor=W)
Radiobutton(Window, text="Seat", variable=opcion,   
            value='Seat', command=seleccionar).pack(anchor=W)

monitor = Label(Window)
monitor.pack()
Button(Window, text="Reiniciar", command=Reiniciar).pack()

Window.mainloop()