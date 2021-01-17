notas = [5, 5, 5, 5, 5]
soma = 0
x = 0

while x < 5:
    soma += notas[x]
    x += 1

print("Media: %5.2f" %(soma/x))