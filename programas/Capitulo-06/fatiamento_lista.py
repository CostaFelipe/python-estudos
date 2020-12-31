l = [ 1, 2, 3, 5]
v = l
v[0] = 3

print("Primeira lista:", l)
print("Segunda lista:", v)

# agora vamos  fazer corretamente

l = [2, 4, 6, 7]
v = l[:] #referenciando uma nova copia

v[0] = 7

print("Primeira lista:", l)
print("Segunda lista:", v)
