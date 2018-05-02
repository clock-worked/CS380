from pegGame import Game
import random

def backTrack(selectedRules=[]):
    game.describeState()
    rules = game.applicableRules()

    for i, rule in enumerate(rules):
        print"{}:\t{}".format(i, rule)
    rule = random.choice(rules)
    game.describeRule(rule)


    if rule not in selectedRules:
        selectedRules.append(rule)


    if len(rules) < 2:
        if game.goal() and game.softApplyRule(rule):
            return rules
        else:
            print "BackTracking..."
            selectedRules.pop()
    else:
        game.applyRule(rule)

    return backTrack(allChoices)






game = Game()
game.refBoard()
allChoices = []
backTrack(allChoices)

