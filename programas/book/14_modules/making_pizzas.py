#importando funcoes especifica
from pizza import make_pizza
#palavra reservada
from pizza import make_pizza as mp

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

mp(12, 'pepperoni')
