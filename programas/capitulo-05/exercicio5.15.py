valor = 0
s = 0

while True:
    n = int(input("Digite o codigo do produto:"))
    if n == 0:
        break
    qtd = int(input("Digite a quantidade do produto:"))
    if n == 1:
        valor = qtd * 0.5
    if n == 2:
        valor = qtd * 1.00
    if n == 3:
        valor = qtd * 4.00
    if n == 5:
        valor = qtd * 7.00
    if n == 9:
        valor = qtd * 8.00
    s = s + valor
    print("Total do carrinho %5.2f" %s)

print("Valor final ca compra:%5.2f" %s)