import sqlite3

def main():
    """
    Metodo Principal Tema 11
    """
    print("<>----<> TEMA 11 <>----<>")
    print("+" + 13 * "-" + "+")
    print(("|" + " Ejercicio 1 " + "|\n"), end="")
    print("+" + 13 * "-" + "+")

    print("Crear Tabla Alumnos")
    creaTablaAlumnos()

    print("Insertar Datos")
    listaId=[1,2,3,4,5,6,7,8]
    listaNombres=["Alejandro", "Fernando","Diego","Marcos","Lucia","Dolores","Paloma","Sara"]
    listaApellidos=["Fernandez", "Garcia","Garcia","Alvarez","Cuervo","Martinez","Franganillo","Tamargo"]

    for i in range(0,8):
        insertarAlumno(listaId[i], listaNombres[i], listaApellidos[i])
        print(f'INSERT {i+1}')

    alumno: str=input("Que alumno quieres buscar: ")
    alumnoBuscado=buscarAlumno(alumno)

    if alumnoBuscado != None:
        print(f'Datos Alumno Buscado \nID: {int(alumnoBuscado[0])} Nombre: {alumnoBuscado[1]} Apellidos: {alumnoBuscado[2]}')
    else:
        print("No se encuentra en la base de datos el alumno buscado "+alumno)


def buscarAlumno(nombre: str):
    conn = sqlite3.connect('BBDD_Alumnos.db')
    cursor = conn.cursor()
    query = '''select * from alumnos where nombre=(?);'''
    row = cursor.execute(query, (nombre,))
    alumnoBuscado=row.fetchone()
    cursor.close()
    conn.close()

    return alumnoBuscado

def insertarAlumno(id: int, nombre: str, apellido: str):
    conn = sqlite3.connect('BBDD_Alumnos.db')
    cursor = conn.cursor()

    alumno=buscarAlumno(nombre)
    if alumno == None:
        query = '''INSERT INTO alumnos(id, nombre, apellido) VALUES(?,?,?)'''
        row = cursor.execute(query, (id, nombre, apellido))
        conn.commit()
        cursor.close()
        conn.close()
    else:
        cursor.close()
        conn.close()

def creaTablaAlumnos():
    conn = sqlite3.connect('BBDD_Alumnos.db')
    cursor = conn.cursor()
    query = f'CREATE TABLE IF NOT EXISTS alumnos(id INT PRIMARY KEY, nombre TEXT, apellido TEXT);'
    row = cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()