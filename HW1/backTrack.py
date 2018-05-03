from pegGame import Game
def backTrack(stateList, allRules=[]):
    state = stateList[0]

    if state in stateList[1:]:
        stateList.pop(0)
        return False

    #dead end
    if game.applicableRules(state) == []:
        stateList.pop(0)
        return False

    if game.applicableRules(state) < 2 and not game.goal(state):
        return False

    if game.goal(state):
        return None

    if len(stateList) > 20:
        return False


    rules = game.applicableRules(state)

    for rule in rules:
        # game.refBoard()
        newState = game.applyRule(rule, state)
        game.describeState(state)
        game.describeRule(rule)
        stateList.insert(0, newState)
        path = backTrack(stateList)
        if path != False:
            return path.append(rule)
            path = True


    return False



game = Game()
game.refBoard()
backTrack([game.boardState])




