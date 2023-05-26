# import NECESARIOS PARA EL USO DE ALGUNOS MÉTODOS
import csv
import random
import datetime

# HEADER PARA EL CSV
header = ['nombre', 'num_hijos', 'fecha_Nacimiento']
# DATOS ALEATORIOS
nombres = ["Wilfredo Guerra-Beltrán","Judith de Tejedor","Maristela Almagro Rosado","Ámbar Carvajal Flores","Artemio de Salvà","Marta de Espinosa",
"Gerardo Alberto Berrocal","José Ángel Máximo Tapia Barrio","Máxima Esteban Flores","Wilfredo Batalla Duarte","Ariel Apolonia Morillo Naranjo",
"Guiomar Calvet Cañas","Vasco Alcolea Almeida","Nuria Amo Jerez","Lucho Ojeda Alcolea"]

hijos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# newline ES PARA QUE NO DEJE LINEAS VACIAS ENTRE LOS VALORES ESCRITOS, ABRIMOS EL ARCHIVO
file = open('C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\PROPUESTOS\\Ej4yEj5\\archivo.csv', 'w', encoding='UTF8', newline="")
# CREAMOS PARA PODER ESCRIBIR
writer = csv.writer(file)
# ESCRIBIMOS EL ARRAY header
writer.writerow(header)
# AQUI NO HE USADO WITH POR POSIBLES PROBLEMAS A LA HORA DE QUE SE CIERRE SOLO EL WIRTER
for e in range(10):
    # CREAMOS LAS FECHAS ALEATORIAS
    fecha = datetime.datetime(int(random.uniform(1014,2023)), int(random.uniform(1,11)), int(random.uniform(1,31)))
    # NUMERO ALEATORIO DEL 0-3
    numero = int(random.uniform(0,14))
    data = [str(nombres[numero]),int(hijos[numero]),fecha]
    writer.writerow(data)
file.close()

# LEEMOS EL ARCHIVO PARA VER SI TODAS LOS DATOS HAN SIDO AÑADIDOS CORRECTAMENTE
with open('C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\PROPUESTOS\\Ej4yEj5\\archivo.csv','r',encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print (row)
        nombre = str(row["nombre"])
        numHij = int(row["num_hijos"])
        fechaNac = datetime.datetime.strptime(row["fecha_Nacimiento"], '%Y-%m-%d %H:%M:%S')
        print(type(nombre))
        print(type(numHij))
        print(type(fechaNac))
        print(fechaNac.year)
print()