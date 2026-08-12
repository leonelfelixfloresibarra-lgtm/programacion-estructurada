for i in range(3):   #ciclo externo (filas)
    print("inicio de la fila(i)")
    for j in range(2):
        print("-> columna{1}")

for fila in range (3):
    for columna in range (4):
        print("*", end="")
    print()