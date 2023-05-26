import csv

# PRUEBA 1) METIENDO TODOS EN UN DICCIONARIO ES EL MÁS USADO
with open('C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\PROPUESTOS\\Ej3\\archivo.csv','r',encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print (row)

print()


# PRUEBA 2) METIENDO TODOS EN UNA LISTA DE DICCIONARIOS
with open('C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\PROPUESTOS\\Ej3\\archivo.csv','r',encoding='UTF-8') as file2:
    reader2 = csv.DictReader(
        file2)
    data2 = list(reader2)
    print(data2)
    print(data2[1].values())

print()


# PRUEBA 3) METIENDO TODOS EN UN DICCIONARIO EN UN ARCHIVO SIN CABECERA, POR LO QUE LA PONDREMOS NOSOTROS CON fieldnames
with open('C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\PROPUESTOS\\Ej3\\archivo2.csv','r',encoding='UTF-8') as file:
    # PONEMOS LAS CABECERAS CON fieldnames
    reader3 = csv.DictReader(file,fieldnames=["Name","Age","Website","Location"])
    for row3 in reader3:
        print (row3["Location"])

print()