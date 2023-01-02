class Vehiculo():
    _color = " rojo "
    _Ruedas = "4 Ruedas "
    _puertas = "2 Puertas "

class Coche(Vehiculo):
    def __init__(self, name):
        print ("estoy en el constructo de" + name)

    velocidad = "100km/H"
    cilindrada = "4 cilindros"

Ferrari = Coche(" Ferrari")
print("el ferrari es de color " + Ferrari._color)
print("tiene " + Ferrari._Ruedas )