class GameController:
    def __init__(self, myValue, conn):
        self.game = OldeyGame()
        self.myValue = myValue
        self.conn = conn

    def makeMyMove(self, coords):
        self.game.check(coords, self.myValue)
        self.conn.send(coords.encode('utf-8'))
        self.game.printIt()
    
    def waitForOponent(self):
        coords = self.conn.recv(1024).decode('utf-8')
        self.game.check(coords, -self.myValue)
        self.game.printIt()