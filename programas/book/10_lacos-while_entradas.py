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
    message = input(prompt) print(message)
