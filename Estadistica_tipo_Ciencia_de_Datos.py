#Ejercicio 1: Edades de clientes

edades = [14, 22, 35, 18, 16, 40, 27, 19, 21, 13]

#Contadores
menores = 0
adultos = 0
total = 0
suma = 0

#Desiciones
for edad in edades:

    #Suma de edades
    suma += edad

    #Cuantos son menores
    if edad <18:
        menores += 1

    #Cuantos son adultos
    else: 
        adultos += 1

#Total de personas
total = len(edades)

#Promedio de edades
promedio = suma / total

print("Total de personas: ", total)
print("Promedio: ", promedio)
print("Menores: ", menores)
print("Adultos: ", adultos)
print("Edad Mayor: ", max(edades))
print("Edad Menor: ", min(edades))