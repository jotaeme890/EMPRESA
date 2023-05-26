import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from faker import Faker
import random

fake = Faker('es_ES')

header = ["Name","Age","Surname","Location"]

with open("C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\PANDAS\\prueba.csv","w",encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in range(10):
        name = fake.name()
        age = random.randint(18,33)
        surname = fake.last_name()
        location = fake.unique.street_name()
        data = [name,age,surname,location]
        writer.writerow(data)


# EMPEZAMOS CON DATAFRAME
df = pd.read_csv("C:\\Users\\perma\\Desktop\\PWC\\PYTHON\\EJERCICIOS\\PANDAS\\prueba.csv")
df_mean = df["Age"].mean()
print(df_mean)

df_group = df.groupby("Location")["Age"].mean()
print(df_group)

df.plot()
plt.show()
