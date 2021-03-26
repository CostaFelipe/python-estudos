#coding=utf-8
#Passando uma lista para uma função

def greet_users(names):
    for name in names:
        msg = "hello, " + name.title() + "!"
        print(msg)

usernames = ['felipe', 'ruth', 'levi']
greet_users(usernames)

#Modificando uma lista em uma função
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print("\n------------------------")
#modificando o exemplo
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Evitando que uma função modifique uma lista
print("\nparte 02 ------------------------------------")
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
print("\nEvitando que uma função modifique uma lista")
show_completed_models(completed_models)

print("\n")
#FAÇA VOCÊ MESMO
#8.9 – Mágicos
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

list_magicians = ['Holdining', 'Mr. M', 'full']
great_magicians = []
show_magicians(list_magicians)

print("\n")
#8.10 – Grandes mágicos && 8.11 – Mágicos inalterados:
def make_great(magicians, great_magicians):
    while magicians:
        current_magicians = magicians.pop()
        great_magicians.append("Grande " + current_magicians)

def show_magicians(great_magicians):
    for great_magician in great_magicians:
        print(great_magician)

make_great(list_magicians[:], great_magicians)
show_magicians(great_magicians)
