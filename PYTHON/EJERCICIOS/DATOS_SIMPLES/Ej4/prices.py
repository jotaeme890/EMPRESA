table = {"Plátano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}

print(f"¿Which fruit do you want? ")
fruta = input()

if fruta in table:
    print(f"How many {fruta} Do you want?")
    cantidad = int(input())
    print(f"It costs {round(table[fruta]*cantidad,2)}")
else:
    print(f"Sorry, We dont have {fruta}")
