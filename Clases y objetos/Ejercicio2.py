class Alumno():
    Nombre = None
    Nota = None

    def __init__(self, a):
        Nombre = a
        Nota = 10
        print("Se inicializa Alumno")
        print("su nombre es " + Nombre)
        if Nota > 6:
            print("tu nota es " + str(Nota) + " Y has aprobado")
       

A1 = Alumno("Andres")


