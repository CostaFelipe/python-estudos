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
