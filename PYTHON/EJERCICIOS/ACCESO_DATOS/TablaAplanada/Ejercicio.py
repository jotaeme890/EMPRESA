def create_select(table):
    sentence = f"""SELECT column_name
                    FROM information_schema.columns
                    WHERE table_schema = 'public' AND table_name = '{table}' ;"""
    if(table == "movimiento"):
        sentence = """SELECT column_name
                    FROM information_schema.columns
                    WHERE table_schema = 'public' AND table_name = 'movimiento' and column_name <> 'id_cuenta'"""
    return sentence

def create_insert(lista_cliente, lista_cuenta, lista_movimiento):
    sentence = f"""SELECT {lista_cliente}, {lista_cuenta}, {lista_movimiento}
                FROM cliente AS cl INNER JOIN cliente_cuenta AS cl_cu ON(cl.id_cliente = cl_cu.id_cliente) 
                INNER JOIN cuenta AS ct ON(ct.id_cuenta = cl_cu.id_cuenta)
                INNER JOIN movimiento AS mv ON(ct.id_cuenta = mv.id_cuenta)
                ORDER BY cl.id_cliente"""
    return sentence

# IMPORTS NECESARIOS
import csv
import psycopg2

try:
    # CREAMOS LA CONEXIÓN Y EL CURSOR
    conn = psycopg2.connect(
                            host='localhost', 
                            database="SantanderBank",
                            user='postgres', 
                            password=1234, 
                            port=5432
            )
    cursor = conn.cursor()
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error en la conexión de la BBDD")

try:
    # SENTENCIAS DE CLIENTE
    select_clientes = create_select("cliente")
    cursor.execute(select_clientes)
    list_cols_cliente = cursor.fetchall()
    # AL PASARLE UNALISTA DE TUPLAS, PARA PODER PASARLO A UN STRING TENDREMOS QUE HACER LO SIGUIENTE
    list_cols_cliente_str = "cl." +  ",cl.".join([str(item[0]) for item in list_cols_cliente]) 

    select_cuentas =  create_select("cuenta")
    cursor.execute(select_cuentas)
    list_cols_cuentas = cursor.fetchall()
    list_cols_cuentas_str = "ct." +  ",ct.".join([str(item[0]) for item in list_cols_cuentas])

    # LE QUITAMOS id_cuenta YA QUE LA MISMA COLUMNA NO PUEDE ESTAR REPETIDA
    select_movimientos = create_select("movimiento")
    cursor.execute(select_movimientos)
    list_cols_movimientos = cursor.fetchall()
    list_cols_movimientos_str = "mv." + ",mv.".join([str(item[0]) for item in list_cols_movimientos])
except Exception as e:
    print(type(e))
    print("Ha currido un error al crear las litas modulares")

try:    
    # EJECUTAMOS LA SENTENCIA PARA LA TABLA APLANADA
    with open("C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\ACCESO_DATOS\\TablaAplanada\\aplanada.csv",'w',encoding="UTF-8",newline="") as file:
        writer = csv.writer(file)
        # HACEMOS EL SELECT DE TODOS LOS ATRIBUTOS DE LAS TABLAS
        sql_txt = create_insert(list_cols_cliente_str, list_cols_cuentas_str, list_cols_movimientos_str)
        cursor.execute(sql_txt)
        select = cursor.fetchall()
        # ESCRIBIMOS EN EL .csv
        header = (list_cols_cliente_str,list_cols_cuentas_str,list_cols_movimientos_str)
        # PASAMOS A STR
        header = str(header)
        # LE QUITAMOS LOS ( ) DEL PRINCIPIO Y DEL FINAL
        headerN = header.strip("()")
        # SEPARMAOS LOS ELEMENTOS POR '
        elem = headerN.split("','")
        # LE AÑADIMOS A CADA ELEMENTO ,
        head = ",".join(elem)
        # QUITAMOS LAS COMILLAS QUE SEPARAN CADA ELEMENTO Y LO PONEMOS COMO SIN ESPACIOS Y LOS ESPACIOS EN BLANCO SIN ESPACIOS
        head = head.replace("'", "")
        head = head.replace(" ", "")
        # LO PASAMOS A LISTA PARA PODER PASARLO AL WRITE ROW
        head_list = head.split(",")
        # ESCRIBIMOS LA CABECERA DESPUES DE HACERLE TODOS LOS CAMBIOS
        writer.writerow(head_list)
        # ESCRIBIMOS TODOS LOS DATOS
        writer.writerows(select)
except Exception as e:
    print(type(e))
    print("Ha currido un error al escribir en el .csv")

# CREAREMOS LA TABLA EN POSTGRESQL CON CTAS
create = f"""
            DROP TABLE IF EXISTS tabla_aplanada;
            CREATE TABLE tabla_aplanada AS {sql_txt}
        """
cursor.execute(create)
conn.commit()