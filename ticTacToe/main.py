from board import Board
from player import Player
from game import Game

if __name__ == '__main__':
    b1 = Board()
    print(b1.display())
    comp = Player("Computer", is_computer=True)
    human = Player("Human", is_computer=False)
    game = Game(human, comp, b1)
    game.make_move(human)
    print(b1.display())

