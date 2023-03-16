class OldyGame:
    currentTurn = -1
    currentGame = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __init__(self, starter = -1):
        self.currentTurn = starter

    def check(self, coords, myValue):
        if self.currentTurn != myValue:
            return False
        
        x, y = (int(c) for c in coords.split(','))
        self.currentGame[y][x] = myValue

        self.currentTurn *= -1
        return True

    def printIt(self):
        for row in self.currentGame:
            for column in row:
                match(column):
                    case 1:
                        print('| X |', end='')
                    case -1:
                        print('| O |', end='')
                    case 0:
                        print('|   |', end='')
            print()