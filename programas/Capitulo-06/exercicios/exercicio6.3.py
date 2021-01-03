primeira = []
segunda  = []
x = 0

while True:
    n = int(input("Add numbers list 01:"))
    if n == 0:
        break
    primeira.append(n)

while True:
    n = int(input("Add numbers list 02:"))
    if n == 0:
        break
    segunda.append(n)

terceira = primeira[:]
terceira.extend(segunda)
print(set(terceira))
