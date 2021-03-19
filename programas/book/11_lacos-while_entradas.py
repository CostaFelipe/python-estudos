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
    if repeat == 'no':
        polling_active =  False
        print("\n--- Poll Results ---")
        for name, response in responses.items():
            print(name + " would like to climb " + response + ".")
