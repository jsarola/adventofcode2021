fitxer = open('input.txt', 'r')

files = fitxer.readlines()

count = 0
increased = 0

horitzontal = 0
vertical = 0

for fila in files:
    lafila = fila.split()
    
    operacio = lafila[0]
    moviment = int(lafila[1].strip())
    
    if operacio == 'forward':
        horitzontal = horitzontal + moviment
    if operacio == 'down':
        vertical = vertical + moviment
    if operacio == 'up':
        vertical = vertical - moviment

print("Part1 -> horitzontal: ", horitzontal)
print("Part1 -> vertical: ", vertical)
print("Part1 -> total: ", horitzontal * vertical)

horitzontal = 0
vertical = 0
aim = 0

for fila in files:
    lafila = fila.split()
    
    operacio = lafila[0]
    moviment = int(lafila[1].strip())
    
    if operacio == 'forward':
        horitzontal = horitzontal + moviment
        vertical = vertical + (aim * moviment)
    if operacio == 'down':
        aim = aim + moviment
    if operacio == 'up':
        aim = aim - moviment

print("Part2 -> horitzontal: ", horitzontal)
print("Part2 -> vertical: ", vertical)
print("Part2 -> total: ", horitzontal * vertical)
