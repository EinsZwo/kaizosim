'''
Created on Jan 2, 2023

@author: matth
'''
import pokebase as pb
import random
from kaizosim import constants
import math



def findMoveWithName(moveName):
    moveName = moveName.replace(' ','-').lower()
    return [move for move in constants.ALL_MOVES if move.name==moveName]

def getMove(moveName):
    moveList = findMoveWithName(moveName)
    if (len(moveList)==0):
        return None
    else:
        return moveList[0]


def getBaseStat(pokemonTemplate,statToGet):
    statToGet = statToGet.lower().strip().replace(' ','-')
    for baseStat in pokemonTemplate.stats:
        if (str(baseStat.stat) == statToGet):
            return baseStat.base_stat
    
    return 0
    

class Move:
    
    def __init__(self, move):
        self.move = move
        self.disabled = False
        self.PP = 100
        
    def canUse(self):
        return (not self.disabled) and (self.PP > 0)
    
    def subtractPP(self):
        if(self.PP <= 0):
            raise Exception("Invalid PP remaining for move used")
        self.PP = self.PP - 1
        
    def checkCritical(self):
        # TODO set up moves with increased critical chances
        
        if (random.randint(1,16)==16):
            return True
        
        return False
    
    def isPhysical(self):
        # in Gen 1-3, all moves of a certain type are physical
        return self.move.type.name.title() in constants.PHYSICAL_TYPES
    
    
    def applyMove(self,userPokemon,targetPokemon):
        
        # reference: https://bulbapedia.bulbagarden.net/wiki/Damage#Generation_III
        basePower = self.move.power
        
        userAttack = userPokemon.getAttack() if self.move.isPhysical() else userPokemon.getSpecialAttack()
        targetDef = userPokemon.getDefense() if self.move.isPhysical() else userPokemon.getSpecialDefense()

        
        damage = ((2 * userPokemon.level / 5) + 2 * basePower * (userAttack / targetDef)) / 50
        
        if (userPokemon.pokemonTemplate.type == self.move.type):
            damage = damage * 1.5
            
        if (self.checkCritical()):
            damage = damage * 2    
        
        
        damage = damage * (random.randint(85,100) / 100)
        
        targetPokemon.applyDamage(damage)
        
        # much more to do WRT burn, screens, etc.
        

class Status:
    def __init__(self):
        self.flinch = False
        self.burned = False
        self.paralyzed = False
        self.frozen = False
        self.sleep = False
        self.confused = False 
        self.constrict = False
        self.poisoned = False
        
class BaseStats:
    
    def calculateStat(self,baseStat,individualValue,effortValue,level):
        stat = math.floor((0.01 * (2 * baseStat + individualValue + (.25 * effortValue))) * level) + 5
        return stat
    
    def calculateHP(self,baseStat,individualValue,effortValue,level):
        stat = math.floor((0.01 * (2 * baseStat + individualValue + (.25 * effortValue)))) + level + 10
        return stat
        
    def __init__(self,pokemon,level):
        print([vars(base) for base in pokemon.pokemonTemplate.stats])
        
        self.attack = self.calculateStat(getBaseStat(pokemon.pokemonTemplate,'attack'),pokemon.IVs.attack,0,level)
        self.defense = self.calculateStat(getBaseStat(pokemon.pokemonTemplate,'defense'),pokemon.IVs.defense,0,level)
        self.specialAttack = self.calculateStat(getBaseStat(pokemon.pokemonTemplate,'special-attack'),pokemon.IVs.specialAttack,0,level)
        self.specialDefense = self.calculateStat(getBaseStat(pokemon.pokemonTemplate,'special-defense'),pokemon.IVs.specialDefense,0,level)
        self.speed = self.calculateStat(getBaseStat(pokemon.pokemonTemplate,'speed'),pokemon.IVs.speed,0,level)
        self.HP = self.calculateHP(getBaseStat(pokemon.pokemonTemplate,'hp'),pokemon.IVs.HP,0,level)

class Stat:
    def __init__(self):
        self.stage = 0
    
    def modifyStage(self,modifier):
        self.stage = self.stage + modifier
        self.stage = min(constants.MAX_STAGES,self.stage)
        self.stage = max(-constants.MAX_STAGES,self.stage)
    
    def setStage(self,value):
        self.stage = value

        
    def resetStage(self):
        self.setStage(0)
    
    def getStatModifier(self):
        """
        Get the effective modifier for a stat; used in calculating damage, etc. in combat
        """
        if self.stage < 0:
            return 2 / (2 + self.stage)
        
        else:
            return (2 + self.stage) / 2

       
class CombatStats:
    def __init__(self,maxHP=0):
        self.attack = Stat()
        self.defense = Stat()
        self.speed = Stat()
        self.specialDefense = Stat()
        self.specialAttack = Stat()
        self.currentHP = maxHP
        
        
class IndividualValues():
    def generateRandomIV(self):
        return random.randint(0,constants.MAX_IV)
    
    def __init__(self):
        self.attack = self.generateRandomIV()
        self.defense = self.generateRandomIV()
        self.specialAttack = self.generateRandomIV()
        self.specialDefense = self.generateRandomIV()
        self.speed = self.generateRandomIV()
        self.HP = self.generateRandomIV()
        
    
        

class PokemonInstance:
    
    def generateMoves(self, respectLearnset=False):
        # TODO, allow respecting the learnset
        if (respectLearnset):
            0
              
        validMoves = False
        
        while(not validMoves):
            moves = random.choices(constants.ALL_MOVES,k=4)
            for move in moves:
                if move.power is not None: #ensure at least one damaging move, per rules
                    validMoves = True
        
        
        self.moves = [Move(move) for move in moves]
    
    
    def __init__(self, pokemonName, level, moves = []):
        
        self.pokemonTemplate = pb.pokemon(pokemonName)
        self.name = pokemonName
        self.level = level
        self.moves = moves
        self.status = Status()
        self.IVs = IndividualValues()
        self.baseStats = BaseStats(self,level)
        self.combatStats = CombatStats(self.baseStats.HP) 
        
  
        
        # generate stats and moves
        if(len(moves)==0):
            self.generateMoves()
        else:
            self.moves = moves
        
        # get base stat total
        
        # randomly redistribute
        
        # scale to level
        
        
    
        

    # combat interface  
    def getAttack(self):
        return self.baseStats.attack * self.combatStats.attack.getStatModifier()
    
    def getDefense(self):
        return self.baseStats.defense * self.combatStats.defense.getStatModifier()
    
    def getSpeed(self):
        return self.baseStats.speed * self.combatStats.speed.getStatModifier()
    
    def getSpecialDefense(self):
        return self.baseStats.specialDefense * self.combatStats.specialDefense.getStatModifier()
    
    def getSpecialAttack(self):
        return self.baseStats.specialAttack * self.combatStats.specialAttack.getStatModifier()
    
    def getHP(self):
        return self.combatStats.currentHP
    
    
    def canMove(self):
        if (self.Status.flinch or self.Status.frozen or self.status.sleep or self.status.paralyzed):
            return False
        # todo: confusion, etc.
        return True
    
    
    def useMove(self, move, targetPokemon):
        # todo: subtract PP
        move.applyMove(self,targetPokemon)
        
    def takeDamage(self,damage):
        self.currentHP = max(self.currentHP - damage,0)


        
