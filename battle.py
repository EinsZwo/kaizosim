'''
Created on Jan 2, 2023

@author: matth
'''

import random
import pokemon
from pokemon import logger

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
        return pokemonOne, pokemonTwo
    
    if pokemonOne.getSpeed() < pokemonTwo.getSpeed():
        return pokemonTwo, pokemonOne
    
    else:
        first = random.choice([pokemonOne,pokemonTwo])
        second = [pokemonOne,pokemonTwo].remove(first)[0]
        return first,second


def takeTurn(pokemonToMove,oppPokemon):
    if(not pokemonToMove.canMove()):
        return
    
    pokemonToMove.makeMove(oppPokemon)

def preTurnStatus(pokemon):
    if(pokemon.Status.sleep):
        # chance to wake up
        pokemon.Status.sleep-=1
        
    if(pokemon.Status.confused):
        pokemon.Status.confused-=1
        # chance to snap out
        
        
    # ... more to follow
    
    
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
    
def oneBattleIteration(pokemon1,pokemon2):
    
    while(not pokemon1.isFainted() and not pokemon2.isFainted()):
        