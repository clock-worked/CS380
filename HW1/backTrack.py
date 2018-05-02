from pegGame import Game
import random

game = Game()
game.refBoard()
allChoices = []
selectedRules = []

def backTrack(allChoices):
    game.describeState()
    rules = game.applicableRules()
    for i, rule in enumerate(rules):
        print"{}:\t{}".format(i, rule)
    rule = random.choice(rules)
    game.describeRule(rule)

    allChoices.append(rules)
    selectedRules.append(rule)


    if len(rules) == 1:
        if game.goal() and game.softApplyRule(rule)
            return rules
        else:
            selectedRules.pop()
            allChoices



