import sqlite3
# Se creo la tabla de alumnos 
conexion = sqlite3.connect('Base de Datos/database.db')
try:
    conexion.execute("""create table Estudiantes (
                              id integer primary key autoincrement,
                              alumno text,
                              Apellido text
                        )""")
    print("se creo la tabla Alumnos")                        
except sqlite3.OperationalError:
    print("La tabla Alumnos ya existe")    


# Ingreso los alumnos
conexion.execute("insert into Estudiantes(alumno,Apellido) values (?,?)", ("Jose", "Cogollo"))
conexion.execute("insert into Estudiantes(alumno,Apellido) values (?,?)", ("Daniel", "Medrano"))
conexion.execute("insert into Estudiantes(alumno,Apellido) values (?,?)", ("Felipe", "Arteaga"))
conexion.execute("insert into Estudiantes(alumno,Apellido) values (?,?)", ("Juan", "Barreras"))
conexion.execute("insert into Estudiantes(alumno,Apellido) values (?,?)", ("Yeison", "Montes"))
conexion.execute("insert into Estudiantes(alumno,Apellido) values (?,?)", ("Pedro", "Casilla"))
conexion.execute("insert into Estudiantes(alumno,Apellido) values (?,?)", ("Luis", "Ochoa"))
conexion.execute("insert into Estudiantes(alumno,Apellido) values (?,?)", ("Andres", "Castillo"))
conexion.commit()

cursor = conexion.cursor()

rows = cursor.execute('SELECT * FROM Estudiantes WHERE alumno="Andres"')
for row in rows:
    print (row)

conexion.close()