notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

while x < 7:
    notas[x] = float(input("Add notas do aluno:"))
    soma+= notas[x]
    x+=1
x = 0
while x < 7:
    print("nota %d - %6.2f" %(x, notas[x]))
    x+=1
print("Média: %5.2f" %(soma / x))