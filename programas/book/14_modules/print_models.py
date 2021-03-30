import printing_functions as p
import printing_functions
from printing_functions import *
from printing_functions import print_models as md

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

p.print_models(unprinted_designs, completed_models)

print("\n")
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
printing_functions.print_models(unprinted_designs, completed_models)

print("\n")
unprinted_designs = ['iphone', 'robot', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)

print("\n")
unprinted_designs = ['iphone', 'robot', 'dodecahedron']
completed_models = []
md(unprinted_designs, completed_models)
