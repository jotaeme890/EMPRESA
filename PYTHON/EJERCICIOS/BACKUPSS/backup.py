import datetime
import os

# RUTA HACIA DONDE TENEMOS pg_dump
pg_dump_path = '"C:\\Program Files\\PostgreSQL\\15\\bin\\pg_dump.exe"'
# NOMBRE BBDD PARA HACER LA BUCKUP
db_name = 'SantanderBank'
# USUARIO
db_user = 'postgres'
# CONTRASEÑA
db_password = 12345
# HOST DE LA BBDD
db_host = 'localhost'
# CONTRASEÑA
db_port = 5432
# MODIFICAR EL NOMBRE QUE QUEREMOS, USAMOS EL strftime PARA PONER EL FORMATO QUE QUEREMOS
file = f"C:\\backup\\{db_name}_python_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
# .system ES PARA EJECUTAR UN COMANDO COMO SI FUERA EN CONSOLA, POR LO QUE USAREMOS pg_dump QUE SIRVE PARA BU DE POSTGRESQL CUYA SINTAXIS ES LA SIGUIENTE (PERO CON LOS DATOS EN VARIABLES PARA QUE SEA MÁS ENTENDIBLE) Y LO VOLCAREMOS EN EL ARCHIVO
os.system(f"{pg_dump_path} --dbname=postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name} 1> {file} 2> C:\\backup\\resultado_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")