cursos=4
estudiantes=6
for i in range (cursos):
    asistieron=0
    faltaron=0
    for j in range(estudiantes):
        asistencia=int(input(f"asistencia estudiante {j+1} del curso {i+1} (1=asistio , 0=falto):"))
        if asistencia == 1:
            asistieron +=1
        else:
            faltaron+=1
    print(f"curso { i+1} -> asistieron: {asistieron}, faltaron: {faltaron}")