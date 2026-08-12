aulas=4
estudiantes=5
notas=[]
for i in range (aulas):
    aula=[]
    for j in range (estudiantes):
        nota = float(input(f" nota estudiante {j+1} del aula {i+1}: "))
        aula.append(nota)
    notas.append(aula)
    promedio= sum(notas[i])/ estudiantes
    print(f" promedio del aula {i+1}: {promedio:.2f}")