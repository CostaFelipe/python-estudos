s = 0
m = 0

while True:
    n = int(input("Digite numeros ou 0 para SAIR:"))
    if n == 0:
        break
    s = s + n
    m = m + 1
    
print("resultado: %d - Media: %5.2f" %(s, s / m))