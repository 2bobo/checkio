def checkio(game_result):
    row_set = []
    winer = "D"
    for row in game_result:
        if row == u"XXX":
            winer = "X"
        elif row == u"OOO":
            winer = "O"
        row_set.append(list(row))
    for num in range(3):
        if row_set[0][num] == row_set[1][num] == row_set[2][num] == u"X":
            winer = "X"
        elif row_set[0][num] == row_set[1][num] == row_set[2][num] == u"O":
            winer = "O"
    if row_set[0][0] == row_set[1][1] == row_set[2][2] == u"X" or row_set[0][2] == row_set[1][1] == row_set[2][0] == u"X":
        winer = "X"
    elif row_set[0][0] == row_set[1][1] == row_set[2][2] == u"O" or row_set[0][2] == row_set[1][1] == row_set[2][0] == u"O":
        winer = "O"

    return winer

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

