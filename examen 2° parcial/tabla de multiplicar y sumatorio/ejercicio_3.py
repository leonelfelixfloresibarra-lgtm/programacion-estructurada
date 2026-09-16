def calcular_tabla(numero):
	resultados = []
	total = 0
	for multiplicador in range(1, 13):
		resultado = numero * multiplicador
		resultados.append((multiplicador, resultado))
		total += resultado
	return resultados, total