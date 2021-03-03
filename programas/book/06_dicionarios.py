#dicionario simples
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#Acessando valores em um dicionario
print(alien_0['color'])
print(alien_0['points'])

print("\n")
#exemplo
alien = {'color': 'green', 'points': 10}
new_points = alien['points']
print("You just earned " + str(new_points) + " points!")

print("\n")
#Adicionando novos pares chave-valor
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("\n")
#Comecando com um dicionario vazio
alien = {}
alien['color'] = 'green'
alien['points'] = 5
print(alien)

print("\n")
#Modificando valores em um dicionario
alien_1 = {'color': 'green'}
print("the alien is " + alien_1['color'])
alien_1['color'] = 'yellow'
print("the alien is now " + alien_1['color'])

print("\n")
alien_2 = {'x_positions': 0, 'y_positions': 25, 'speed': 'medium'}
if alien_2['speed'] == 'slow': x_positions = 1
elif alien_2['speed'] == 'medium': x_positions = 2
else: x_positions = 3

alien_2['x_positions'] = alien_2['x_positions'] + x_positions
print("o novo valor x_positions e: " + str(alien_2['x_positions']))

print("\nremovendo chave-valor")
#removendo chave-valor
alien = {'color': 'green', 'points': 5}
print(alien)
del alien['points']
print(alien)

print("\nUm dicionario de objetos semelhantes")
#Um dicionario de objetos semelhantes
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python'
                      }
print("Sarah favorite language is " +
       str(favorite_languages['sarah'].title()) +
      ".")

print("\nFaca voce mesmo")
#Faca voce mesmo
#6.1
people = {'first_name': 'sarah', 'last_name': 'costa',
          'age': 32, 'city': 'varsovia'}
print(people)
