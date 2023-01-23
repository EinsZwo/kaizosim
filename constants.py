'''
@author: EinsZwo
'''
import pokebase as pb

GENERATION = 3

MAX_STAGES = 6

PHYSICAL_TYPES = ['Normal', 'Fighting', 'Flying', 'Ground', 'Rock', 'Bug', 'Ghost', 'Poison', 'Steel']

STARTERS = ['Bulbasaur', 'Squirtle', 'Charmander']

ALL_MOVES = []
for gen in range(1,GENERATION+1):
    gen_resource = pb.generation(gen)
    ALL_MOVES.extend(gen_resource.moves)

MAX_IV = 31

