'''
Module to log and save a representation of a battle.
'''

from kaizosim.pokemon import PokemonInstance,Move


def logPokemonInitial(pokemon):
    log = [pokemon.pokemonTemplate.name, str(pokemon.ID)]

    log.append(str(vars(pokemon.baseStats)))
        
    return '|'.join(log)

def logPokemonStatus(pokemon):
    log = [pokemon.pokemonTemplate.name, str(pokemon.ID)]
    log.append(str(vars(pokemon.getHP))
    # other combat stats to come
    log.append(str(vars(pokemon.status)))
    return ';'.join(log)

def logMove(pokemon, moveUsed):
    log = [pokemon.pokemonTemplate.name, str(pokemon.ID)]
    log.append(moveUsed)
    return ':'.join(log)

