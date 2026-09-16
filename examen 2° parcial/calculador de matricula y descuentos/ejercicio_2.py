TARIFAS = {
    1: ("Auto", 10),
    2: ("Moto", 5),
    3: ("Camion", 20),
}
def calcular_cobro(tipo, horas):
    nombre, tarifa = TARIFAS[tipo]
    subtotal = tarifa * horas
    recargo = subtotal * 0.15 if horas > 4 else 0
    return nombre, tarifa, subtotal, recargo, subtotal + recargo