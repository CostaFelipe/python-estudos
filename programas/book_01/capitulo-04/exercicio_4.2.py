velocidade = float(input("Digite a velocidade do carro:"))

if velocidade > 80:
    valor_multa = 5.00
    print("Usuário multado, o valor da multa é %5.2f" %valor_multa)
else:
    print("Sem multa")
