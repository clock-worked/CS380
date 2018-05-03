from pegGame import Game
def backTrack(stateList):

    state = stateList[0]

    if state in stateList[1:]:
        return

    #dead end
    if state.applicableRules() == []:
        return

    if state.goal():
        return None

    if len(stateList) > 20:
        return

    state.describeState()
    rules = game.applicableRules()

    for rule in rules:
        newState = state.applyRule(rule)
        newStateList = stateList.insert(0, newState)
        path = backTrack(newStateList)
    #
    #
    # if rule not in selectedRules:
    #     selectedRules.append(rule)
    #
    #
    # if len(rules) < 2:
    #     if game.goal() and game.softApplyRule(rule):
    #         return rules
    #     else:
    #         print "BackTracking..."
    #         selectedRules.pop()
    # else:
    #     game.applyRule(rule)
    #
    # return backTrack(allChoices)


game = Game()
game.refBoard()
backTrack([game])




