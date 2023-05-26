import psycopg2
from psycopg2 import extras

conn = None
cursor = None

try:
    conn = psycopg2.connect(
        host="localhost",
        database="INSTITUTO",
        user="postgres",
        password=1234,
        port= 5432
    )
    print("Todo bien")

    # .cursor ES LO QUE DE VERDAD NOS DEJA HACER COSAS EN LA BBDD PODREMOS HACER CUALQUIER COSA DE CRUD
    cursor = conn.cursor()

    # SELECT
    cursor.execute("SELECT * FROM alumno")
    # NOS DEVOLVERÁ UN DATO, POR LO QUE LO COGEMOS CON .fecthone() (ASÍ SOLO COGERÁ UN VALOR, SI PONEMOS .fecthall() COGERÁ TODOS) Y AL GUARDARLO EN UNA VARIABLE, LA PODREMOS IMPRIMIR POSTERIORMENTE
    result = cursor.fetchall()
    # print(result) 

    # CREATE TABLE
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS nomina(
                        id serial primary key not null,
                        tipo varchar not null)
                    """);
    # PARA GUARDAR LOS CAMBIOS QUE SE HACEN DENTRO DE UNA BBDD, TENDREMOS QUE USAR EL MÉTODO .commit() QUE TIENE LA CONEXIÓN PARA QUE SE GUARDEN LOS DATOS
    conn.commit()

    # INSERT INTO
    cursor.execute("""
                    INSERT INTO nomina(tipo) VALUES ('Pepe'),('Juan')
                    """)
    conn.commit()

    cursor.execute("SELECT * FROM nomina")
    result = cursor.fetchall()
    # print(result)

    # SI QUEREMOS AGREGAR MÁS DATOS EN UNA SOLA SENTENCIA USAREMOS .executemany(primer,segundo) siendo el primer parametro la sentencia a hacer y el segundo una lista
    multiple_input = [
        ("Pedro"), ("Federico")
    ]
    insert = "INSERT INTO nomina (tipo) VALUES (%s)";

    cursor.executemany(insert, multiple_input)
    conn.commit()

    # SI QUEREMOS RECIBIR UN DICCIONARIO EN VEZ DE UNA TUPLA AL HACER UNA CONSULTA, HAREMOS
    # .DictCursor NO ES UN VERDADERO DICCIONARIO, PARA QUE FUESE 100X100 UN DICCIONARIO, USAREMOS .RealDictCursor
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM alumno")

    for row in cursor.fetchall():
        print(row["id_alumno"], row["nombre_alumno"]) 

    # DELETE
    delete = "DELETE FROM profesor where id_profesor = %s"
    delete_in = "2"
    cursor.execute(delete,delete_in)
    conn.commit()

    # UPDATE
    update = "UPDATE profesor set id_profesor = 2 WHERE id_profesor=%s"
    update_in = "1"
    cursor.execute(update,update_in)
    conn.commit() 

    # DROP TABLE
    cursor.execute("DROP table nomina")
    conn.commit()

except Exception as error:
    print(error)
    print("Ha salido mal")

finally:
    # LO SUYO ES HACERLO AL FINAL, PARA NO TENER QUE CERRAR TODAS LAS SENTENCIAS A CADA RATO
    # None ES UN TIPO DE DATO QUE NO LLEGA A SER NULL
    if(cursor is not None):
        cursor.close()
    
    if(conn is not None):
        conn.close()
