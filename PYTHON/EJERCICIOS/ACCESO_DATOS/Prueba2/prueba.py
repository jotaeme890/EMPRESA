def imprimir_menu():
    print("¿Qué quiere hacer?\n1)Insertar datos\n2)Borrar datos\n3)Modificar datos\n4)Listar todos los trabajadores\n5)Salir")

import psycopg2

conn = None
eleccion = 0
print("Bienvenido a la Base de Datos de PWC, POR AHORA SOLO CONTIENE TRABAJADORES, ESTAMOS TRABAJANDO EN PROGRESAR...\n")
try:
    while(eleccion != 5):
        conn = psycopg2.connect(
                host="localhost",
                database="PWC",
                user="postgres",
                password=1234,
                port= 5432
            )
        imprimir_menu()
        
        print("Opción: ", end="")
        eleccion = int(input())
        cur = conn.cursor()
        if (eleccion == 1):
            print("INSERTAR DATOS")
            print("Nombre del trabajador: ",end="")
            nombre = input()
            print("Apellido del trabajador: ",end="")
            apellido = input()
            print("DNI del trabajador: ",end="")
            dni = str(input())
            insert = f"INSERT INTO trabajador (nombre_trabajador,dni_trabajador,apellido_trabajador) VALUES ('{nombre}','{dni}','{apellido}')"

            cur.execute(insert)
            conn.commit()

            print("\nTrabajador añadido correctamente\n")

        if (eleccion == 2):
            print("ELIMINAR DATOS")
            select = "SELECT id_trabajador, nombre_trabajador FROM trabajador"
            cur.execute(select)
            print(cur.fetchall())

            print("\n¿Qué usuario quiere borrar?")
            id_borrado = int(input())
            delete = f"delete from trabajador where id_trabajador = {id_borrado}"
            conn.commit()

            if(cur.rowcount > 0):
                print("\nTrabajador eliminado con éxito\n")
            else:
                print("\nNo se ha borrado nada\n")

        
        if (eleccion == 3): 
            print("MODIFICAR DATOS")
            select = "SELECT id_trabajador, nombre_trabajador FROM trabajador"
            cur.execute(select)
            print(cur.fetchall())

            print("\n¿Qué usuario quiere modificar?")
            id_mod = int(input())
            print("Nombre del trabajador: ",end="")
            nombre = input()
            print("Apellido del trabajador: ",end="")
            apellido = input()
            print("DNI del trabajador: ",end="")
            dni = str(input())

            update = f"update from trabajador set nombre_trabajador = {nombre}, dni_trabajador = {dni},apellido_trabajador = {apellido} where id_trabajador = {id_mod}"
            cur.execute(update)
            conn.commit()

            print("\nTrabajador modificado correctamente\n")
            
        if (eleccion == 4):
            select = "SELECT id_trabajador, nombre_trabajador FROM trabajador"
            cur.execute(select)
            print(cur.fetchall())

except psycopg2.OperationalError as ErrorConexion:
    print("Lo siento, ha ocurrido un problema de conexión, revisa bien los datos para la conexión a la Base de Datos")

finally:
    if(conn is not None) : conn.close()
    if(conn is not None) : conn.close()