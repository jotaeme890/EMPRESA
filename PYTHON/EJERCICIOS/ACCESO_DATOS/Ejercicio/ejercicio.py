# NECCESARY IMPORTS OF MODULES
import csv
from faker import Faker
import psycopg2
import random
# SPANISH
fake = Faker('es_ES')
# POOL CONNECTION
conn = psycopg2.connect(
                        host='localhost', 
                        database="SantanderBank",
                        user='postgres', 
                        password=1234, 
                        port=5432
        )
cursor = conn.cursor()

eleccion = 0;

while(eleccion != 5):
    print("\nMETER DATOS\n1)Clientes\n2)Cuentas\n3)Movimientos\n4)Agregar cuenta a cliente\n5)Salir")
    eleccion = int(input())

    if(eleccion == 1):
        try:
            # OPEN THE FILE IN WRITE MODE
            file = open("C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\ACCESO_DATOS\\Ejercicio\\clientes.csv",'a',encoding="UTF-8",newline="")
            writer = csv.writer(file)

            for i in range (10):
                    # CREATE DATA
                    nombre = fake.first_name()
                    apellido = fake.last_name()
                    date = fake.date_between()
                    dni = fake.unique.nif()
                    numero = str(random.randint(6,9))
                    for k in range(8):
                        numero += str(random.randint(0,9))
                    email = fake.ascii_email()
                    direccion = fake.unique.street_name()
                    data = [nombre,apellido,date,dni,numero,email,direccion]
                    writer.writerow(data)

                    # INSERT DATA INTO TABLE
                    insert_query = f"""INSERT INTO cliente (
                                    nombre_cliente,
                                    apellido_cliente,
                                    fechanac_cliente,
                                    dni_cliente,
                                    telefono_cliente,
                                    correo_cliente,
                                    calle_cliente
                                    ) VALUES (
                                        '{nombre}',
                                        '{apellido}',
                                        '{date}',
                                        '{dni}',
                                        '{numero}',
                                        '{email}',
                                        '{direccion}')"""
                    cursor.execute(insert_query)
                    conn.commit()
            file.close()

        except Exception as e:
            print("ERROR")
        except psycopg2.OperationalError as ec:
            print("Lo siento, ha ocurrido un problema de conexión, revisa bien los datos para la conexión a la Base de Datos")

    if(eleccion == 2):
        try:
            file = open("C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\ACCESO_DATOS\\Ejercicio\\cuentas.csv",'a',encoding="UTF-8",newline="")
            writer = csv.writer(file)

            for i in range (100):
                    iban = fake.unique.iban()
                    data = [iban]
                    writer.writerow(data)

                    insert_query = f"""INSERT INTO cuenta (
                                    iban_cuenta
                                    ) VALUES (
                                        '{iban}')"""
                    cursor.execute(insert_query)
                    conn.commit()
            file.close()

        except Exception as e:
            print("ERROR")
        except psycopg2.OperationalError as ec:
            print("Lo siento, ha ocurrido un problema de conexión, revisa bien los datos para la conexión a la Base de Datos")

    if(eleccion == 3):
            try:
                file = open("C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\ACCESO_DATOS\\Ejercicio\\movimientos.csv",'a',encoding="UTF-8",newline="")
                writer = csv.writer(file)
                    # 1000 DATOS ALEATORIOS
                for i in range(1000):
                        # VALOR MAXIMO
                    maximo = "SELECT MAX(id_cuenta) FROM CUENTA"
                    cursor.execute(maximo)
                    id_max = cursor.fetchone()
                    maximo = id_max[0]
                        # VALOR MINIMO
                    minimo = "SELECT MIN(id_cuenta) FROM CUENTA"
                    cursor.execute(minimo)
                    id_min = cursor.fetchone()
                    minimo = id_min[0]
                        # VALOR ALEATORIO
                    aleatorio = random.randint(minimo,maximo)
                        # TIPO DE MOVIMIENTO
                    tipo_mov = random.randint(0,1)
                    if(tipo_mov == 0):
                        mov = "Retiro"
                    if(tipo_mov == 1):
                        mov = "Ingreso"
                        # FECHA MOV
                    date = fake.date_between()
                        # CANTIDAD
                    cantidad = random.randint(0,3000)

                    data = [aleatorio,mov,cantidad,date]
                    writer.writerow(data)
                        # INSERTAR EN POSTGRE
                    insert_mov = f"""INSERT INTO movimiento (
                                        id_cuenta,
                                        tipo_movimiento,
                                        cantidad_movimiento,
                                        fecha_movimiento
                                    ) VALUES (
                                    {aleatorio},
                                    '{mov}',
                                    {cantidad},
                                    '{date}'
                                    )"""
                    cursor.execute(insert_mov)
                    conn.commit()
                file.close()

            except Exception as e:
                print("ERROR")
            except psycopg2.OperationalError as ec:
                print("Lo siento, ha ocurrido un problema de conexión, revisa bien los datos para la conexión a la Base de Datos")
    
    if (eleccion == 4):
        try:
            file = open("C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\ACCESO_DATOS\\Ejercicio\\clientes_cuentas.csv",'a',encoding="UTF-8",newline="")
            writer = csv.writer(file)
            for i in range (50):
                maximo = "SELECT MAX(id_cuenta) FROM CUENTA"
                cursor.execute(maximo)
                id_max = cursor.fetchone()
                maximo = id_max[0]

                minimo = "SELECT MIN(id_cuenta) FROM CUENTA"
                cursor.execute(minimo)
                id_min = cursor.fetchone()
                minimo = id_min[0]
                aleatorio1 = random.randint(minimo,maximo)

                maximo = "SELECT MAX(id_cliente) FROM CLIENTE"
                cursor.execute(maximo)
                id_max = cursor.fetchone()
                maximo = id_max[0]

                minimo = "SELECT MIN(id_cliente) FROM CLIENTE"
                cursor.execute(minimo)
                id_min = cursor.fetchone()
                minimo = id_min[0]
                aleatorio2 = random.randint(minimo,maximo)
                
                date = fake.date_between()

                data = [aleatorio2,aleatorio1,date]
                writer.writerow(data)

                insert_mov = f"""INSERT INTO cliente_cuenta (
                                            id_cliente,
                                            id_cuenta,
                                            fecha_creacion
                                        ) VALUES (
                                        {aleatorio2},
                                        {aleatorio1},
                                        '{date}'
                                        )"""
                cursor.execute(insert_mov)
                conn.commit()
            file.close()

        except Exception as e:
                print("ERROR")
        except psycopg2.OperationalError as ec:
                print("Lo siento, ha ocurrido un problema de conexión, revisa bien los datos para la conexión a la Base de Datos")

conn.close()