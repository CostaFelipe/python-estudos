L = []

L.append(1)
L.append("Linda")
L.append("Ruth")
print(L)

numeros = []
while True:
    n = int(input("Digite numeros para add:"))
    if n == 0:
        break
    numeros.append(n)

x = 0
while x < len(numeros):
    print(numeros)
    x+=1