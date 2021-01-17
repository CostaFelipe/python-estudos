L = [1, 2, 4, 7]
x = 0
soma = 0

print(len(L))

while x < len(L):
    print(L[x])
    soma += L[x]
    x += 1 
    
print(soma)