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

multiplo_zhen = input("Informe um número para vê se é multiplo de 10: ")
multiplo_zhen = int(multiplo_zhen)
if multiplo_zhen % 10 == 0:
    print(str(multiplo_zhen) + " é multiplo de 10")
else:
    print("O número " + str(multiplo_zhen) + "não é multiplo de 10" )
