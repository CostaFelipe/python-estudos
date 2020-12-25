# Calcular o valor a ser pago por horas de serviço
horas = int(input("Digite as horas:"))
taxa  = float(input("Digite a taxa:"))
print("O valor a ser pago: R$%5.2f" %(horas * taxa))
