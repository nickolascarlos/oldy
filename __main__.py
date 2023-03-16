from GameController import *
from OldyGame import *
from utils import getConnection

def main():
    # Conectar-se ou hospedar o jogo?
    option = int(input('[1] - Conectar\n[2] - Hospedar\n\n>'))
    connection = getConnection(option)
    gameController = GameController(1 if option == 2 else -1, connection)

    # Convidado inicia o jogo!
    # Se você for o host,
    # Espere-o fazer a primeira jogada
    # antes de entrar no loop principal
    if option == 2:
        gameController.waitForOponent()
    while True:
        gameController.makeMyMove(input('>>'))
        gameController.waitForOponent()

if __name__ == '__main__':
    main()



