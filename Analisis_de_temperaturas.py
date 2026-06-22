
#ANALISIS DE TEMPERATURAS

#Temperaturas registradas
temperaturas = [28, 31, 25, 33, 29, 35, 27, 30, 32, 26]

#Herramientas de analisis
total = 0
mayor = temperaturas[0]
menor = temperaturas[0]
dias_calurosos = 0
dias_frescos = 0

for temp in temperaturas:

    #Temperatura mayor a 30 grados
    if temp >= 30:
        dias_calurosos += 1
        print("Dia caluroso:", temp)
        

    #Temperatura menor o igual a 30 grados
    else:
        dias_frescos += 1
        print("Dia fresco:", temp)

    #Total de temperaturas
    total += temp

    #Temperatura mayor
    if temp > mayor:
        mayor = temp

    #Temperatura menor
    if temp < menor:
        menor = temp

#Calcular el promedio
promedio = total / len(temperaturas) 

#Resultados
print("Temperatura mayor:", mayor)
print("Temperatura menor:", menor)
print("Promedio:", promedio)
print("Días calurosos:", dias_calurosos)
print("Días frescos:", dias_frescos)