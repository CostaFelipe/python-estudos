valor = 0

while True:
    n = int(input("Digite o codigo do produto:"))
    if n == 0:
        break
    else:
        if n == 1:
            qtd = int(input("Digite a quantidade do produto"))
            valor = qtd * 0.5