#importando total o modulo
import pizza
#importando funcoes especifica
from pizza import make_pizza
#palavra reservada
from pizza import make_pizza as mp

#Usando a palavra reservada as para atribuir um alias a um modulo
import pizza as p

#Importando todas as funcoes de um modulo
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

p.make_pizza(12, 'peppori')

pizza.make_pizza(12, 'peppori')

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

mp(12, 'pepperoni')
