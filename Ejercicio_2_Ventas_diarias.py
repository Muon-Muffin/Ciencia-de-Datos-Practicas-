
ventas = [120, 85, 200, 150, 90, 300, 75, 180]

#Contadores
total = 0
suma = 0
dias_menores_de_100 = 0
dias_mayores_de_100 = 0


#Desiciones
for venta in ventas:
    if venta <100:
        print ("Venta menor a 100:", venta)
    else:
        print ("Venta mayor o igual a 100:", venta)

    if venta < 100:
        dias_menores_de_100 += 1
    else:
        dias_mayores_de_100 += 1

    suma += venta

total = len(ventas)
promedio = suma / total

print("Total de ventas: ", total)
print("Suma de ventas: ", suma)
print("Promedio de ventas: ", promedio)
print("Días con ventas menores a 100: ", dias_menores_de_100)
print("Días con ventas mayores o iguales a 100: ", dias_mayores_de_100)
print("Venta mayor: ", max(ventas))
print("Venta menor: ", min(ventas))