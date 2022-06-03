Numero_inicial= 2
Numero_final = 33
numeros_impares = []

for a in range(Numero_inicial,Numero_final+1):
    if a % 2 != 0:
        numeros_impares.append(a)

print(f"lista de numeros impares entre {Numero_inicial} y {Numero_final}:")
print(numeros_impares)