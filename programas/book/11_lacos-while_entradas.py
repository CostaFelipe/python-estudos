#coding=utf-8
#Usando um laço while com listas e dicionários
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    print(confirmed_users)

#Removendo todas as instâncias de valores específicos de uma lista
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print(pets)

#Preenchendo um dicionário com dados de entrada do usuário
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhats is your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == no:
        polling_active =  False
        print("\n--- Poll Results ---")
        for name, response in responses.items():
            print(name + " would like to climb " + response + ".")

#FAÇA VOCÊ MESMO
sandwich_orders = ['paulistano', 'bauru', 'x-burguer', 'big-mac']
finished_orders = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("preparei seu sanduíche " + current_sandwich)
    finished_orders.append(current_sandwich)
print("esses são os sanduíche prontos:" + str(finished_orders))


print("\n7.9 pastrami")
sandwich_orders = ['paulistano', 'pastrami','bauru', 'x-burguer', 'pastrami', 'big-mac', 'pastrami']
finished_orders = []
print("a lanchonete está sem pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_orders.append(sandwich_orders)
print(finished_orders)

print("\n7.10 Férias dos sonhos")
responses = {}
active = True
while active:
    name = input("Qual é seu nome?")
    response = input("Se pudesse visitar um lugar do mundo, para onde você iria?")
    responses[name] = response
    repeat = input("(yes) para continuar e (no) para sair")
    if repeat == 'no':
        active = False
        for name, response in responses.items():
            print("O(a) " + name + " viajar p/ " + response)
