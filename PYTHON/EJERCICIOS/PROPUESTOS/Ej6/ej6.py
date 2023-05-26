import csv 

with open("C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\PROPUESTOS\\Ej6\\uno.csv",mode="r",encoding="UTF-8") as archivoRecep:
    reader = csv.DictReader(archivoRecep)
    for e in reader:
        print(e)
        

with open("C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\PROPUESTOS\\Ej6\\dos.csv",mode="w",encoding="UTF-8", newline="") as archivoLleg:
    writer = csv.writer(archivoLleg,)
    writer.writerow(reader)