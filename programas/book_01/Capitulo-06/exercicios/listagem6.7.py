numeros = [0, 0, 0]
x = 0

while x < 3:
    numeros[x] = int(input("Enter numbers %d:" %(x+1)))
    x += 1

while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair:)"))
    if escolhido == 0:
        break
    print("O numero escolhido é %d" %(numeros[escolhido-1]))

