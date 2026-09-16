def generar_fibonacci(cantidad):
    sucesion = []
    anterior, actual = 0, 1

    for _ in range(cantidad):
        sucesion.append(anterior)
        anterior, actual = actual, anterior + actual

    return sucesion
