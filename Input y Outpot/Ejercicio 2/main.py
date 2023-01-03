import pickle

class coche:
    puertas = 2
    Motor = "Diesel"
    def __init__(self) -> None:
        print("Estoy en el construcor de coche" )

ferrari = coche()

NuevoPy = open('input y Outpot/Ejercicio 2/ferrari.bin', 'rb')
info = pickle.load(NuevoPy)
print(type(info))
NuevoPy.close()

