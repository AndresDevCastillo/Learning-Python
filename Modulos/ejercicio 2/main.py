import datetime
# Transformo las horas en un formato de dos digitos 
Hora = datetime.datetime.now()
Hora = int(Hora.strftime("%I"))

if Hora > 7:
    print("Es hora de ir a casa campeon!")
else:
    Faltante = (7-Hora)
    print("faltan " + str(Faltante) + " horas para salir")
