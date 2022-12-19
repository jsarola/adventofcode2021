fitxer = open('input.txt', 'r')

files = fitxer.readlines()

count = 0
increased = 0

for fila in files:
    fila_actual = int(fila)
    if count == 0:
        fila_anterior = int(fila)
    else:
        if fila_anterior <= fila_actual:
            increased = increased + 1
            # print(fila_anterior, "-", fila_actual)
        fila_anterior = int(fila)
    count = count + 1


print("Part1 -> Count: ", count)
print("Part1 -> Increased: ", increased)

count = 0
increased = 0
suma_anterior = 0
suma_actual = 0

for fila in files:
    if count == 0:
        valor_1 = int(fila)        
    elif count == 1:
        valor_2 = int(fila)
    elif count == 2:
        valor_3 = int(fila)
        suma_anterior = valor_1 + valor_2 + valor_3
    else:
        suma_actual = suma_anterior + int(fila) - valor_1
        if suma_anterior < suma_actual:
            increased = increased + 1
            # print(suma_anterior, "-", suma_actual)
        suma_anterior = suma_actual
        valor_1 = valor_2
        valor_2 = valor_3
        valor_3 = int(fila)
    count = count + 1

print("Part2 -> Count: ", count)
print("Part2 -> Increased: ", increased)

