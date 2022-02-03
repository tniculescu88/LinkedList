from player import Player
import random

class Game:

    welcome_message = "===============\nTic Tac Toe\n================"

    def __init__(self, human, comp, board):
        self.human = human
        self.comp = comp
        self.board = board

    def welcome_message(self):
        return self.welcome_message

    def make_move(self, player_obj):
        if player_obj.is_computer:
            self.board.update_poz(random.randint(1, 9), Player.COMP_SYMB)
        else:
            desired_poz = int(input("Please input a position from 1-9:"))
            while not self.board.is_poz_ok(desired_poz):
                desired_poz = int(input("Please input a position from 1-9:"))
            self.board.update_poz(desired_poz, Player.HUMAN_SYMB)
