from suma import sum

try:
    while True:
        print("Say me the first number: ",end="")
        num1 = int(input())
        print("Say me the second number: ",end="")
        num2 = int(input())
        print(f"The result is {sum(num1,num2)}")
        # EXCEPCION QUE DA AL DARLE A CONTROLC PARA SALIR
except KeyboardInterrupt:
    print("\nHas salido correctamente")