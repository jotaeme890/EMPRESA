from primo import primo

try:
    while True:
        print("Dime el número: ",end="")
        num1 = int(input())
        print(f"El número {primo(num1)}")
except KeyboardInterrupt:
    print("\nHas salido correctamente")

