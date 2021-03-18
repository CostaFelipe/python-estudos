#coding=utf-8
#Um dicionário em um dicionário

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
