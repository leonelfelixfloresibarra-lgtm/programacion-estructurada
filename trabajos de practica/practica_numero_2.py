categoria=3
productos=4
precios=[]
for i in range (categoria):
    cat=[]
    for j in range(productos):
        precio=float(input(f"Precio por producto {j+1} de categoria {i+1}: "))
        cat.append(precio)
    precios.append(cat)
    total=sum(precios[i])
    print(f"total de ventas categoria 1{i+1}: {total:.2f}")