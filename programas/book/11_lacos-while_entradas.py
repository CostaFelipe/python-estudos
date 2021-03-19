#coding=utf-8
#Usando um laço while com listas e dicionários
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
