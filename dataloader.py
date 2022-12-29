'''
Created on Dec 29, 2022

@author: matth
'''

import pokebase as pb

char = pb.pokemon('charmander')

for move in char.moves:
    print(vars(move))