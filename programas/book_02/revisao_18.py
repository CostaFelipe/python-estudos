List1 = []

Avengers = ['Hulk', 'Iron-Man', 'Captain', 'Thor']

a, b = [1, 2]
print(a)
print(b)

Avengers = ['Hulk', 'Iron-Man', 'Captain', 'Thor']
print(Avengers[0])
print(Avengers[1])
print(Avengers[1:3])

Avengers = ['Hulk', 'Iron-Man', 'Captain', 'Thor']
Avengers[2] = "Captain-America"
print(Avengers)

C_W_team = ['Hulk', 'iron-man', 'Captain-American', 'Thor', "Vision"]
del C_W_team[0]
print(C_W_team)
del C_W_team[2:4]
print(C_W_team)

Avengers1 = ['hulk', 'iron-man', 'Captain-America', 'Thor']
Avengers2 = ["Vision","sam"]
Avengers = Avengers1 + Avengers2
print(Avengers)

Av = ['Vision', 'sam']
new_Av = Av * 2
print(new_Av)

Avengers= ['hulk', 'iron-man', 'Captain-America', 'Thor']
if "iron-man" in Avengers:
    print("Yes")

print(len(Avengers))

lista = [1, 2, 6, 45, 100]
print(max(lista))

lista = ["1", "2"]
print(max(lista))


