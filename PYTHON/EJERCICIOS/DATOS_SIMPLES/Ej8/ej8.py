print("Dime un número positivo: ", end="")
num = int(input())

def validaNum(num):
    if(num < 0): return False
    else: return True

if(validaNum(num)):
    for i in range(num,-1,-1):
        print(i, end=",")
else:
    print("El número debe ser positivo")



