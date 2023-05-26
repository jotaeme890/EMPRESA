import subprocess

# Parámetros de conexión a la base de datos
db_host = 'localhost'
db_port = 5432
db_name = 'SantanderBank'
db_user = 'postgres'
db_password = 12345

# Ruta del archivo de respaldo de la base de datos
backup_file = 'C:\\backup\\SantanderBank_python_20230522_132426.sql'

try:
    # Comando para restaurar la base de datos usando pg_restore
    restore_command = f'pg_restore --dbname=postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name} --no-owner {backup_file}'
    # Ejecutar el comando de restauración en el sistema operativo
    subprocess.run(restore_command, shell=True, check=True)
    print("Restauración de la base de datos completada con éxito.")

except subprocess.CalledProcessError as e:
    print("Error al restaurar la base de datos:", e)