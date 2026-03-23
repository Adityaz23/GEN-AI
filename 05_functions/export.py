# Everything in the world of python is object , even functions :-
# Q. Why we need import ?
# Ans. imports are used to bring other functionality from other files by simpy importing them in our code .

# This is the local imports like we created the folder recipes and then added the . after the name of the folder which gave us the whole files which are present in their.
'''
import recipes.flavor
print(recipes.flavor.elaichi_chai)
print(recipes.flavor.ginger_chai)'''

# the other method is the using from :-
from recipes.flavor import elaichi_chai
print(elaichi_chai())
from recipes.flavor import ginger_chai
print(ginger_chai())

# or you can also use :-
from recipes.flavor import elaichi_chai, ginger_chai
# and then print them.

# Avoid this method :-
from .recipes.flavor import ginger_chai
print(ginger_chai())

# and never import everythin by everythin means using * after the imports for ex:- (from recipes.flavor import *) this will import everything by which we do not even know what even is there in the flavor file and we are importing everything.