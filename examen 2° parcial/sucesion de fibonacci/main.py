from ejercicio_1 import generar_fibonacci
def main():
    try:
        cantidad = int(input("Ingrese la cantidad de términos N: "))

        if cantidad <= 0:
            print("Error: N debe ser mayor que 0.")
        else:
            sucesion = generar_fibonacci(cantidad)
            print("Primeros términos de Fibonacci:")
            print(", ".join(map(str, sucesion)))
    except ValueError:
        print("Error: ingrese un número entero válido.")
if __name__ == "__main__":
    main()