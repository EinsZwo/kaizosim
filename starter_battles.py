'''
@author: EinsZwo
'''
import pokebase as pb
from kaizosim import constants
from kaizosim.pokemon import PokemonInstance,getMove



def getStarterMoves(pokemonName):
    pokemonName = pokemonName.lower()
    if pokemonName == 'squirtle':
        return [getMove('Tackle'),getMove('Tail Whip')]
    
    if pokemonName == 'charmander':
        return [getMove('Scratch'),getMove('Growl')]
    
    if pokemonName == 'bulbasaur':
        return [getMove('Tackle'),getMove('Growl')]
    
    return []


def generateStarterInstance(pokemonName):
    return PokemonInstance(pokemonName,5,getStarterMoves(pokemonName))


def performBattle(pokemonOne,pokemonTwo):
    # TODO
    return None



charmander = generateStarterInstance('charmander')

print(vars(charmander.baseStats))
print(vars(charmander.IVs))




        
        
        