preco = float(input("Valor da mercadoria: "))
desconto = int(input("Valor do desconto: "))

total = preco - (preco * desconto / 100)
print("Valor com desconto: R$%5.2f" % total)
