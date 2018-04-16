from pegGame import Game
import random

game = Game()
game.refBoard()
rules = game.applicableRules()
while rules:
    rule = random.choice(rules)
    game.describeState()
    game.describeRule(rule)
    game.applyRule(rule)
    rules = game.applicableRules()