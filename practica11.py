print("Este programa hace tablas de multiplicar: ")

num = int(input("Cuantas Tablas desea generar: "))


t = 1
while t <= num:
    i = 10
    while i >= 1:
        resul = t * i
        print(f"{t} * {i} = {resul}")
        i -= 1  
    input("Pulse una tecla para continuar...") 
    t += 1
