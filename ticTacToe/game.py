from player import Player
import random

class Game:

    def __init__(self, human, comp, board):
        self.human = human
        self.comp = comp
        self.board = board

    def welcome_message(self):
        print("===============")
        print("tic tac toe")
        print("===============")

    def make_move(self, player_obj):
        if player_obj.is_computer:
            self.board.update_poz(random.randint(1, 9), Player.COMP_SYMB)
        else:
            desired_poz = input("Please input a position from 1-9:")
            while not self.board.validate_poz(desired_poz):
                desired_poz = input("Please input a position from 1-9:")
            self.board.update_poz(desired_poz, Player.HUMAN_SYMB)
