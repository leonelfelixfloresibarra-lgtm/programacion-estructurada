from ejercicio_3 import calcular_tabla
def main():
	try:
		numero = int(input("Ingrese un número entero entre 1 y 10: "))
		if numero < 1 or numero > 10:
			print("Error: el número debe estar entre 1 y 10.")
		else:
			resultados, total = calcular_tabla(numero)

			print(f"\nTabla del {numero}:")
			for multiplicador, resultado in resultados:
				print(f"{numero} x {multiplicador} = {resultado}")

			print(f"\nSumatorio total: {total}")
	except ValueError:
		print("Error: ingrese un número entero válido.")
if __name__ == "__main__":
	main()