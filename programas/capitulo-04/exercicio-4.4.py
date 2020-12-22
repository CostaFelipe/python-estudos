salario = float(input("Add o salario do funcionario:"))
valor   = salario

if valor > 1250:
    novo_salario = valor + ( valor * 10) / 100
    print("R$%5.2f" %novo_salario)
else:
    novo_salario = valor + (valor * 15) / 100
    print("R$%5.2f" %novo_salario)



