distancia = int(input("Qual distancia que será pecorrida:"))
base = distancia 

if base <= 200:
    calcular_preco = base * 0.50
    print("O preço é: R$%5.2f" %calcular_preco)
else:
    calcular_preco = base * 0.45
    print("O preço é: R$%5.2f" %calcular_preco)


