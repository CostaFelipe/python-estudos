operador = input("Digite o simbolo do operador que deseja calcular:")
number01 = float(input("Digite o primeiro numero:"))
number02 = float(input("Digite o segundo numero:"))

if operador == "+":
    calcular = number01 + number02
elif operador == "-":
    calcular = number01 - number02
elif operador == "*":
    calcular = number01 * number02
elif operador == "/":
    calcular = number01 / number02
else:
    print("Digite os simbolos do operadores: +, -, *, /")
    calcular = 0
print("O resultado é:", calcular)
