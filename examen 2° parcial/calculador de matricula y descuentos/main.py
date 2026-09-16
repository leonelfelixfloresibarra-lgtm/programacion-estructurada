from ejercicio_2 import TARIFAS, calcular_cobro
def main():
	try:
		print("1.Bs 10 por hora - Auto")
		print("2.Bs 5 por hora - Moto")
		print("3.Bs 20 por hora - Camion")
		tipo = int(input("Seleccione el tipo de vehículo: "))
		horas = float(input("Ingrese las horas de parqueo: "))
		if tipo not in TARIFAS:
			print("Error: la opción debe ser 1, 2 o 3.")
		elif horas <= 0:
			print("Error: las horas deben ser mayores que 0.")
		else:
			nombre, tarifa, subtotal, recargo, total = calcular_cobro(tipo, horas)
			print("\n--- Detalle del cobro ---")
			print(f"Vehículo: {nombre}")
			print(f"Horas: {horas:g}")
			print(f"Tarifa por hora: Bs {tarifa:.2f}")
			print(f"Subtotal: Bs {subtotal:.2f}")
			print(f"Recargo: Bs {recargo:.2f}")
			print(f"Total a pagar: Bs {total:.2f}")
	except ValueError:
		print("Error: ingrese valores numéricos válidos.")
if __name__ == "__main__":
	main()