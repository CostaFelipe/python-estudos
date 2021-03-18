#coding=utf-8
#laços while e entradas

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
