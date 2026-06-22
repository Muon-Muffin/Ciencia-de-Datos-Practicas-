#ANALISIS DE NOTAS EN LOS ESTUDIANTES

notas = [95, 67, 88, 100, 72, 54, 81, 60, 90, 77]

#Contadores
total = 0
suma = 0
aprobados = 0
reprobados = 0
excelentes = 0
mayor = notas[0]
menor = notas[0]

#Analisis de notas
for nota in notas:
    #Suma de notas 
    suma += nota

    #Cuantos son Excelentes
    if nota >= 90:  
        excelentes += 1

    #Cuantos son Aprobados
    elif 70 <= nota < 90:
            aprobados += 1

    #Cuantos son Reprobados
    else:
        reprobados += 1

    #Que calificacion es mayor o menor
    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

#Total de Calificaciones
total = len(notas)

#Promedio de Calificaciones
promedio = suma / total

#Resultados en pantalla
print("Total de Calificaciones:", total)
print("Promedio de Calificaciones:", promedio)
print("Calificación Mayor:", mayor)
print("Calificación Menor:", menor)
print("Número de Excelentes:", excelentes)
print("Número de Aprobados:", aprobados)
print("Número de Reprobados:", reprobados)