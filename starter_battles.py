'''
Created on Dec 29, 2022

@author: matth
'''
import pokebase as pb

STARTERS = ['bulbasaur', 'squirtle', 'charmander']

for pokemon1 in STARTERS:
    others = STARTERS.copy().remove(pokemon1)
    playerPokemon = pb.pokemon(pokemon1)
    for pokemon2 in others:
        rivalPokemon = pb.pokemon(pokemon2)
        
        