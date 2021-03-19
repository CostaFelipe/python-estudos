#coding=utf-8
#laços while e entradas

#Como a função input() trabalha
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#Escrevendo prompts claros
name = input("Please enter your name:")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name)

#Usando int() para aceitar entradas numéricas
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#Operador de módulo
#even_or_odd
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0: print("\nThe number " + str(number) + " is even.")
else: print("\nThe number " + str(number) + " is odd.")

#exercicio
locacao_carro = input("Qual tipo de carro que deseja alugar?")
print("Deixe-me ver se consigo um " + locacao_carro + " para você.")

mesa = input("Quantas pessoas estão em seu grupo para jantar?")
mesa = int(mesa)
if mesa >= 8:
    print("Por favor você deve esperar uma mesa")
else:
    print("Sua mesa está pronta")

multiplo_zhen = input("Informe um número para vê se é multiplo de 10: ")
multiplo_zhen = int(multiplo_zhen)
if multiplo_zhen % 10 == 0:
    print(str(multiplo_zhen) + " é multiplo de 10")
else:
    print("O número " + str(multiplo_zhen) + "não é multiplo de 10" )
