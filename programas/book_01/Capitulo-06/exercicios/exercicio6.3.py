primeira = [1, 10, 9, 8, 7, 5]
segunda  = [1, 2, 4, 11, 10, 4, 5]

terceira = primeira[:]
terceira.extend(segunda)
x = 0

while x < len(terceira):
    quarta = set(terceira)
    x+=1
print(quarta)

