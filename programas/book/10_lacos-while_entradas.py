#coding=utf-8
#laços while e entradas

#Laço while em ação
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#Deixando o usuário decidir quando quer sair
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != quit:
        print(message)

#Usando uma flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#Usando break para sair de um laço
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

#Usando continue em um laço
current_numbers = 0
while current_numbers < 10:
    current_numbers += 1
    if current_numbers % 2 == 0:
        continue
    print(current_numbers)

#Evitando loops infinitos
x = 1
while x <= 5:
    print(x)
    x += 1

#FAÇA VOCÊ MESMO
prompt = "\nEscreva os ingredientes para sua pizza"
prompt += "\nSeus ingridientes são:"
active = True
while active:
    ingredientes = input(prompt)
    if ingredientes == 'quit':
        print("Você finalizou seu pedido")
        active = False
    else:
        print(ingredientes)
