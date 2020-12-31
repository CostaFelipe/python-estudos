notas = [0, 0, 0]
soma = 0
x = 0

while x < 3:
    notas[x] = float(input("Diga a nota da prova %d:" %x))
    soma += notas[x]
    x += 1

x = 0
while x < 3:
    print("%d prova c/ nota %5.2f" %(x, notas[x]))
    x += 1
print("Média: %5.2f" % (soma/x))