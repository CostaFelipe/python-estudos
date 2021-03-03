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

#Adicionando novos pares chave-valor
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
