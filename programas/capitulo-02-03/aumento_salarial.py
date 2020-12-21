salario = float(input("Informe o valor do salario do funcionario: "))
porcentagem = int(input("Informe o valor de porcnetagem de aumento: "))

novo_salario = salario + (salario * porcentagem / 100)
print("O novo salario do funcionario e: %5.2f" %novo_salario)
