'''
Created on Jan 2, 2023

@author: matth
'''

import random
import pokemon

# both pokemon select a move at random

# determine who goes first
    # priority moves (e.g. Quick Attack)
    # speed
    # apply modifiers like paralysis (minus speed)
    
    
# do moves


# check status conditions

# check for fainting whenever HP is modified


def determineFirstPokemon(pokemonOne,pokemonTwo):
    if pokemonOne.getSpeed() > pokemonTwo.getSpeed():
        return pokemonOne
    
    if pokemonOne.getSpeed() < pokemonTwo.getSpeed():
        return pokemonTwo
    
    else:
        return random.choice([pokemonOne,pokemonTwo])


def takeTurn(pokemonToMove,oppPokemon):
    if(not pokemonToMove.canMove()):
        return
    
    pokemonToMove.makeMove(oppPokemon)

def preTurnStatus(pokemon):
    if(pokemon.Status.sleep):
        # chance to wake up
        1
    if(pokemon.Status.confused):
        # chance to snap outs
        1
        
    # infatuation...? 
    
def endOfTurnStatuses(pokemon):
    pokemon.Status.flinch = False
    
    if (pokemon.Status.poisoned):
        # apply poison damage
        1
    
    if (pokemon.Status.burned):
        # apply burn damage
        1
    if (pokemon.Status.constrict):
        1 # TODO
    