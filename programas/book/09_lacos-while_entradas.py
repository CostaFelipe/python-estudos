#coding=utf-8
#Um dicionário em um dicionário

#exercicio
locacao_carro = input("Qual tipo de carro que deseja alugar?")
print("Deixe-me ver se consigo um " + locacao_carro + " para você.")

mesa = input("Quantas pessoas estão em seu grupo para jantar?")
mesa = int(mesa)
if mesa >= 8:
    print("Por favor você deve esperar uma mesa")
else:
    print("Sua mesa está pronta")
