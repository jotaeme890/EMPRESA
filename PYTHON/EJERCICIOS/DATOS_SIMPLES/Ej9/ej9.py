print("Dime la altura deseada: ", end="")

altura = int(input())

def validaNum(num):
    if(num < 0): return False
    else: return True

if(validaNum(altura)):
    for i in range(altura):
        for j in range (i+1):
            print("*",end="")

        print()
else:
    print("La altura debe de ser positiva")