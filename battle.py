'''
Main module for running simulations of battles
'''

import random
import pokemon
from kaizosim import logger
from kaizosim.statusconditions import StatusConditions




def determineTurnOrder(pokemon1,pokemon2):
    # determine who goes first
    if pokemon1.getSpeed() > pokemon2.getSpeed():
        return pokemon1, pokemon2
    
    if pokemon1.getSpeed() < pokemon2.getSpeed():
        return pokemon2, pokemon1
    
    else:
        first = random.choice([pokemon1,pokemon2])
        second = [pokemon1,pokemon2].remove(first)[0]
        return first,second


def takeTurn(pokemonToMove,oppPokemon):
    
    # determine a valid move randomly
    
    move = pokemonToMove.getRandomMove()
    
    # log move
    logger.logMove(pokemonToMove,move)
    pokemonToMove.useMove(move,oppPokemon)
    logger.logPokemonStatus(oppPokemon)


    

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
        pokemon.takeDamagePercentage(StatusConditions.POISON_DAMAGE_FRACTION)
    
    if (pokemon.Status.burned):
        # apply burn damage
        pokemon.takeDamagePercentage(StatusConditions.BURN_DAMAGE_FRACTION)
        

    
def oneBattleIteration(pokemon1,pokemon2):
    
    logger.logPokemonInitial(pokemon1)
    logger.logPokemonInitial(pokemon2)
    
    while(not pokemon1.isFainted() and not pokemon2.isFainted()):
        firstToMove, secondToMove = determineTurnOrder(pokemon1,pokemon2)
        
        takeTurn(firstToMove,secondToMove)
        
        
        if(not secondToMove.isFainted() and not firstToMove.isFainted()):
            takeTurn(secondToMove,firstToMove)
        