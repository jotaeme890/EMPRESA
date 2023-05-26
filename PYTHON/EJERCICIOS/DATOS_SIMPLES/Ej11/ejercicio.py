print ("¿Qué quieres comprar (fruta, carne)?")

product = input()

if (product == "fruta"):
    print ("¿Cuánta cantidad?")
    kg = int(input())

    if (kg <= 0):
        print ("No puede ser menor que 0")
    else:
        total = kg * 2.10
        operation1 =  total * 0.10
        totalFinal = total - operation1
        print(f"El total asciende a {totalFinal}")

elif (product == "carne"):
    print ("¿Cuánta cantidad?")
    kg = int(input())
    if (kg <= 0):
        print ("No puede ser menor que 0")
    elif (kg >= 3):
        total = (kg * 3) - 1
        print (f"El total es de  {total}")
    else:
        totalfinal = kg * 3
        print (f"El total es de {totalfinal}")

else:
    print ("No tenemos eso")