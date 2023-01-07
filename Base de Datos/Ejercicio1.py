import sqlite3
# Se creo la tabla de alumnos 
conexion = sqlite3.connect('Base de Datos/database.db')
try:
    conexion.execute("""create table Estudiantes (
                              id integer primary key autoincrement,
                              alumno text,
                              Edad integer
                        )""")
    print("se creo la tabla Alumnos")                        
except sqlite3.OperationalError:
    print("La tabla Alumnos ya existe")    


# Ingreso los alumnos
conexion.execute("insert into Estudiantes(alumno,Edad) values (?,?)", ("Jose", 17))
conexion.execute("insert into Estudiantes(alumno,Edad) values (?,?)", ("Daniel", 21))
conexion.execute("insert into Estudiantes(alumno,Edad) values (?,?)", ("Felipe", 30))
conexion.execute("insert into Estudiantes(alumno,Edad) values (?,?)", ("Juan", 24))
conexion.execute("insert into Estudiantes(alumno,Edad) values (?,?)", ("Yeison", 56))
conexion.execute("insert into Estudiantes(alumno,Edad) values (?,?)", ("Pedro", 24))
conexion.execute("insert into Estudiantes(alumno,Edad) values (?,?)", ("Luis", 22))
conexion.execute("insert into Estudiantes(alumno,Edad) values (?,?)", ("Andres", 19))
conexion.commit()

cursor = conexion.cursor()

rows = cursor.execute('SELECT * FROM Estudiantes WHERE alumno="Luis"')
for row in rows:
    print (row)

conexion.close()