#Welcome to the TP. Good luck and have fun!
# Your name: Jacob Helm
# Your andrew id: jhelm

from cmu_112_graphics import *
import copy


#------------Classes------------------------

class Pokemon:
    #variables
    def __init__(self, name, level, type, moves,
                 attack, defense, spAttack, spDefense, hitpoints, speed):
        self.name = name
        self.level = level
        self.type = type #list of one or two length
        self.moves = moves

        #Base stats and calculation for stats based on level
        self.attackStat = attack
        self.attack = self.attackStat * (self.level / 50)
        self.defenseStat = defense
        self.defense = self.defenseStat * (self.level / 50)
        self.spAttackStat = spAttack
        self.spAttack = self.spAttackStat * (self.level / 50)
        self.spDefenseStat = spDefense
        self.spDefense = self.spDefenseStat * (self.level / 50)
        self.hitPointsStat = hitpoints
        self.hitpoints = self.hitPointsStat * (self.level / 50)
        self.maxHitPoints = self.hitpoints
        self.speedStat = speed
        self.speed = self.speedStat * (self.level / 50)
        if self.hitpoints > 0:
            self.fainted = False
        else: self.fainted = True


    def useMove(self, otherPokemon, move):
        if move.atkType == 'attack':
            atkDamage = (move.power * (self.attack * 0.25)
                        * effectiveness(move.type, otherPokemon.type))
            otherPokemon.hitpoints -= int(atkDamage / otherPokemon.defense)

        elif move.atkType == 'spAttack':
            atkDamage = (move.power * (self.spAttack * 0.25)
                        * effectiveness(move.type, otherPokemon.type))
            otherPokemon.hitpoints -= int(atkDamage / otherPokemon.spDefense)
        
        if otherPokemon.hitpoints <= 0:
            otherPokemon.hitpoints = 0
            otherPokemon.fainted = True
        
    

class Move:
    def __init__(self, name, type, power, accuracy, atkType):
        self.name = name
        self.type = type
        self.power = power
        self.atkType = atkType #spAtk/Atk
        self.accuracy = accuracy



#--------------Animation-------------------

def minimaxHelper(app, pokemon1, pokemon2, depth, prevPokemon,
moveHis, possibleMoves):
    if pokemon1.fainted == True or pokemon2.fainted == True:
        qualityOfMove = ((pokemon2.hitpoints / pokemon2.maxHitPoints) -
                        (pokemon1.hitpoints / pokemon1.maxHitPoints))
        possibleMoves += [(qualityOfMove, moveHis[0].name, depth)]
        
        
        
    else:
        moveHis = moveHis[:depth]
        
        if prevPokemon == None or prevPokemon == pokemon1: 
            for x in range(len(pokemon2.moves)):
                newPokemon = copy.deepcopy(pokemon1)
                pokemon2.useMove(newPokemon, pokemon2.moves[x])
                print('-' + '***' * depth + pokemon2.moves[x].name)
                if len(moveHis) > depth:
                    moveHis[-1] = pokemon2.moves[x]
                else:
                    moveHis.append(pokemon2.moves[x])
                for x in moveHis:
                    print(x.name)
                minimaxHelper(app, newPokemon, pokemon2, depth + 1, pokemon2, moveHis[: depth + 1], possibleMoves)
        else:
            for x in range(len(pokemon1.moves)):
                newPokemon = copy.deepcopy(pokemon2)
                pokemon1.useMove(newPokemon, pokemon1.moves[x])
                moveHis.append(pokemon1.moves[x])
                minimaxHelper(app, pokemon1, newPokemon, depth + 1, pokemon1, moveHis[: depth + 1], possibleMoves)
    
    return possibleMoves

def minimax(app, pokemon1, pokemon2):
    return minimaxHelper(app, pokemon1, pokemon2, 0, None, [], [])

def appStarted(app):
    #Booleans to decide whether or not to draw things
    app.moveBoxes = False
    app.optionBoxes = True


    bodyslam = Move('bodyslam', 'normal', 85, 100, 'attack')
    tackle = Move('tackle', 'normal', 35, 100, 'attack')
    app.pokemon1 = Pokemon('Snorlax', 50, 'normal', [bodyslam],
                            110, 65, 65, 110, 100, 30)
    
    app.pokemon2 = Pokemon('Snorlax', 50, 'normal', [bodyslam ,tackle],
                            110, 65, 65, 110, 100, 30)
    


def effectiveness(atkType, pokemonType, effectiveness = 1):
    if atkType == 'normal':
        if 'steel' in pokemonType:
            effectiveness /= 2
    elif atkType == 'ice':
        if 'flying' in pokemonType:
            effectiveness *= 2
        if 'dragon' in pokemonType:
            effectiveness *= 2
        if 'ground' in pokemonType:
            effectiveness *= 2
        if 'grass' in pokemonType:
            effectiveness *= 2
        if 'ice' in pokemonType:
            effectiveness /= 2
        if 'water' in pokemonType:
            effectiveness /= 2
    elif atkType == 'steel':
        if 'rock' in pokemonType:
            effectiveness *= 2
        if 'fairy' in pokemonType:
            effectiveness *= 2
        if 'ice' in pokemonType:
            effectiveness *= 2
        if 'fire' in pokemonType:
            effectiveness /= 2
        if 'steel' in pokemonType:
            effectiveness /= 2
        if 'water' in pokemonType:
            effectiveness /= 2
        if 'electric' in pokemonType:
            effectiveness /= 2
    elif atkType == 'dragon':
        if 'dragon' in pokemonType:
            effectiveness *= 2
        if 'steel' in pokemonType:
            effectiveness /= 2
        if 'fairy' in pokemonType:
            effectiveness = 0
    elif atkType == 'fairy':
        if 'dragon' in pokemonType:
            effectiveness *= 2
        if 'dark' in pokemonType:
            effectiveness *= 2
        if 'fighting' in pokemonType:
            effectiveness *= 2
        if 'steel' in pokemonType:
            effectiveness /= 2
        if 'fire' in pokemonType:
            effectiveness /= 2
        if 'poison' in pokemonType:
            effectiveness /= 2
    elif atkType == 'fire':
        if 'grass' in pokemonType:
            effectiveness *= 2
        if 'ice' in pokemonType:
            effectiveness *= 2
        if 'bug' in pokemonType:
            effectiveness *= 2
        if 'steel' in pokemonType:
            effectiveness *= 2
        if 'fire' in pokemonType:
            effectiveness /= 2
        if 'water' in pokemonType:
            effectiveness /= 2
        if 'rock' in pokemonType:
            effectiveness /= 2
        if 'dragon' in pokemonType:
            effectiveness /= 2
    elif atkType == 'water':
        if 'fire' in pokemonType:
            effectiveness *= 2
        if 'ground' in pokemonType:
            effectiveness *= 2
        if 'rock' in pokemonType:
            effectiveness *= 2
        if 'water' in pokemonType:
            effectiveness /= 2
        if 'grass' in pokemonType:
            effectiveness /= 2
        if 'dragon' in pokemonType:
            effectiveness /= 2 
    elif atkType == 'grass':
        if 'water' in pokemonType:
            effectiveness *= 2
        if 'ground' in pokemonType:
            effectiveness *= 2
        if 'rock' in pokemonType:
            effectiveness *= 2
        if 'grass' in pokemonType:
            effectiveness /= 2
        if 'fire' in pokemonType:
            effectiveness /= 2
        if 'poison' in pokemonType:
            effectiveness /= 2
        if 'flying' in pokemonType:
            effectiveness /= 2
        if 'bug' in pokemonType:
            effectiveness /= 2
        if 'dragon' in pokemonType:
            effectiveness /= 2
        if 'steel' in pokemonType:
            effectiveness /= 2
    elif atkType == 'ground':
        if 'fire' in pokemonType:
            effectiveness *= 2
        if 'electric' in pokemonType:
            effectiveness *= 4
        if 'steel' in pokemonType:
            effectiveness *= 2
        if 'rock' in pokemonType:
            effectiveness *= 2
        if 'poison' in pokemonType:
            effectiveness *= 2
        if 'grass' in pokemonType:
            effectiveness /= 2
        if 'bug' in pokemonType:
            effectiveness /= 2
        if 'flying' in pokemonType:
            effectiveness = 0
    elif atkType == 'rock':
        if 'fire' in pokemonType:
            effectiveness *= 2
        if 'ice' in pokemonType:
            effectiveness *= 2
        if 'flying' in pokemonType:
            effectiveness *= 2
        if 'bug' in pokemonType:
            effectiveness *= 2
        if 'fighting' in pokemonType:
            effectiveness /= 2
        if 'ground' in pokemonType:
            effectiveness /= 2
        if 'steel' in pokemonType:
            effectiveness /= 2
    elif atkType == 'electric':
        if 'water' in pokemonType:
            effectiveness *= 2
        if 'flying' in pokemonType:
            effectiveness *= 2
        if 'electric' in pokemonType:
            effectiveness /= 2
        if 'grass' in pokemonType:
            effectiveness /= 2
        if 'dragon' in pokemonType:
            effectiveness /= 2
        if 'ground' in pokemonType:
            effectiveness = 0
    elif atkType == 'flying':
        if 'bug' in pokemonType:
            effectiveness *= 2
        if 'grass' in pokemonType:
            effectiveness *= 2
        if 'fighting' in pokemonType:
            effectiveness *= 2
        if 'electric' in pokemonType:
            effectiveness /= 2
        if 'rock' in pokemonType:
            effectiveness /= 2
        if 'steel' in pokemonType:
            effectiveness /= 2
    elif atkType == 'fighting':
        if 'normal' in pokemonType:
            effectiveness *= 2
        if 'ice' in pokemonType:
            effectiveness *= 2
        if 'rock' in pokemonType:
            effectiveness *= 2
        if 'dark' in pokemonType:
            effectiveness *= 2
        if 'steel' in pokemonType:
            effectiveness *= 2
        if 'poison' in pokemonType:
            effectiveness /= 2
        if 'flying' in pokemonType:
            effectiveness /= 2
        if 'fairy' in pokemonType:
            effectiveness /= 2
        if 'bug' in pokemonType:
            effectiveness /= 2
        if 'psychic' in pokemonType:
            effectiveness /= 2
        if 'ghost' in pokemonType:
            effectiveness = 0
    elif atkType == 'dark':
        if 'psychic' in pokemonType:
            effectiveness *= 2
        if 'ghost' in pokemonType:
            effectiveness *= 2
        if 'fairy' in pokemonType:
            effectiveness /= 2
        if 'dark' in pokemonType:
            effectiveness /= 2
        if 'fighting' in pokemonType:
            effectiveness /= 2
    elif atkType == 'ghost':
        if 'ghost' in pokemonType:
            effectiveness *= 2
        if 'psychic' in pokemonType:
            effectiveness *= 2
        if 'dark' in pokemonType:
            effectiveness /= 2
        if 'normal' in pokemonType:
            effectiveness = 0
    elif atkType == 'psychic':
        if 'fighting' in pokemonType:
            effectiveness *= 2
        if 'poison' in pokemonType:
            effectiveness *= 2
        if 'psychic' in pokemonType:
            effectiveness /= 2
        if 'steel' in pokemonType:
            effectiveness /= 2
        if 'dark' in pokemonType:
            effectiveness = 0
    elif atkType == 'bug':
        if 'grass' in pokemonType:
            effectiveness *= 2
        if 'psychic' in pokemonType:
            effectiveness *= 2
        if 'dark' in pokemonType:
            effectiveness *= 2
        if 'steel' in pokemonType:
            effectiveness /= 2
        if 'fire' in pokemonType:
            effectiveness /= 2
        if 'fairy' in pokemonType:
            effectiveness /= 2
        if 'ghost' in pokemonType:
            effectiveness /= 2
        if 'flying' in pokemonType:
            effectiveness /= 2
        if 'poison' in pokemonType:
            effectiveness /= 2
        if 'fighting' in pokemonType:
            effectiveness /= 2
    elif atkType == 'poison':
        if 'grass' in pokemonType:
            effectiveness *= 2
        if 'fairy' in pokemonType:
            effectiveness *= 2
        if 'poison' in pokemonType:
            effectiveness /= 2
        if 'ground' in pokemonType:
            effectiveness /= 2
        if 'rock' in pokemonType:
            effectiveness /= 2
        if 'ghost' in pokemonType:
            effectiveness /= 2
        if 'steel' in pokemonType:
            effectiveness = 0
    return effectiveness

def mousePressed(app, event):
    (x, y) = (event.x, event.y)
    if app.optionBoxes == True:
        if 400 <= x <= 550 and 375 <= y <= 435:
            app.optionBoxes = False
            app.moveBoxes = True
    elif app.moveBoxes == True:
        if 400 <= x <= 550 and 375 <= y <= 435:
            app.pokemon1.useMove(app.pokemon2, app.pokemon1.moves[0])
        elif 575 <= x <= 725 and 375 <= y <= 435:
            print(minimax(app, app.pokemon1, app.pokemon2,))
            #app.pokemon1.useMove(app.pokemon2, app.pokemon1.moves[1])
        elif 400 <= x <= 550 and 450 <= y <= 510:
            app.pokemon1.useMove(app.pokemon2, app.pokemon1.moves[2])
        elif 575 <= x <= 725 and 450 <= y <= 510:
            app.pokemon1.useMove(app.pokemon2, app.pokemon1.moves[3])
        print(app.pokemon2.hitpoints)
        print(app.pokemon2.fainted)

def redrawAll(app, canvas):
        #Battle Screen
    #Health Bars
    canvas.create_rectangle(45, 250, 300, 270, fill = 'grey')
    canvas.create_rectangle(45, 250, 45 +
    (app.pokemon1.hitpoints / app.pokemon1.maxHitPoints) * 255, 270, fill = 'green')
    canvas.create_rectangle(450, 20, 705, 40, fill = 'grey')
    canvas.create_rectangle(450, 20, 450 +
    (app.pokemon2.hitpoints / app.pokemon2.maxHitPoints) * 255, 40, fill = 'green')

    #Move Boxes
    if app.moveBoxes == True:
        canvas.create_rectangle(400, 375, 550, 435, fill = 'grey', width = 5)
        canvas.create_text(475, 405, text = app.pokemon1.moves[0].name, font = 'Arial 15')
        canvas.create_rectangle(575, 375, 725, 435, fill = 'grey', width = 5)
        if len(app.pokemon1.moves) > 1:
            canvas.create_text(650, 405, text = app.pokemon1.moves[1].name, font = 'Arial 15')
        canvas.create_rectangle(400, 450, 550, 510, fill = 'grey', width = 5)
        if len(app.pokemon1.moves) > 2:
                canvas.create_text(475, 480, text = app.pokemon1.moves[2].name, font = 'Arial 15')
        canvas.create_rectangle(575, 450, 725, 510, fill = 'grey', width = 5)
        if len(app.pokemon1.moves) > 3:
            canvas.create_text(650, 480, text = app.pokemon1.moves[3].name, font = 'Arial 15')
        
    
    #Option Boxes
    if app.optionBoxes == True:
        canvas.create_rectangle(400, 375, 550, 435, fill = 'grey', width = 5)
        canvas.create_text(475, 405, text = 'Fight', font = 'Arial 15')
        canvas.create_rectangle(575, 375, 725, 435, fill = 'grey', width = 5)
        canvas.create_text(650, 405, text = 'Bag', font = 'Arial 15')
        canvas.create_rectangle(400, 450, 550, 510, fill = 'grey', width = 5)
        canvas.create_text(475, 480, text = 'Pokemon', font = 'Arial 15')
        canvas.create_rectangle(575, 450, 725, 510, fill = 'grey', width = 5)
        canvas.create_text(650, 480, text = 'Run', font = 'Arial 15')
    


def tpAnimation():
    runApp(width=750, height=550)
    





#################################################
# main
#################################################

def main():
    tpAnimation()

main()