import random
from faker import Faker
# LO PONDREMOS EN ESPAÑOL
fake = Faker('es_ES')
# PARA TENER UN NOMBRE ALEATORIO
nombre = fake.name()
print(nombre)
# CALLE 
direccion = fake.unique.street_name()
print(direccion)
# IBAN
iban =  fake.unique.iban()
print(iban)
# EMAIL
email = fake.ascii_email()
print(email)
# FECHA ENTRE RANGOS
date = fake.date_between()
print(date)
# DNI
dni = fake.unique.nif()
print(dni)
# APELLIDO
apellido = fake.last_name()
print(apellido)
# NÚMERO
numero = str(random.randint(6,9))
for i in range(8):
    numero += str(random.randint(0,9))
print(numero)