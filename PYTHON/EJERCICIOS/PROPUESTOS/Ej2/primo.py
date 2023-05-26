def primo(n):
    for e in range(2,n):
        if(n%e == 0): return "no es primo"
    return "es primo"
