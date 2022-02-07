from board import Board
from player import Player
import random


class Game:

    welcome_message = "===============\nTic Tac Toe\n================"

    def __init__(self, human, comp, board):
        self.human = human
        self.comp = comp
        self.board = board
        self.winner = ""
        self.game_terminated = False
        self.tie = False

    def welcome_message(self):
        return self.welcome_message

    def play_game(self, user_input_list, comp_input_list):
        print("Print works")
        index = 0
        while not (self.game_terminated or self.tie or index == (len(user_input_list) + len(comp_input_list))):
            if index % 2 == 0:  # player's turn
                human_move = user_input_list[index // 2]
                print(f"Player's move:{human_move}")
                user_value = self.human.get_move(user_input=human_move).value
                self.board.update_poz(user_value, self.human.mark)
                print(self.board.display())
            else:  # computer's turn
                computer_move = comp_input_list[index // 2]
                print(f"Computer's move:{computer_move}")
                computer_value = self.comp.get_move(user_input=computer_move).value
                self.board.update_poz(computer_value, self.comp.mark)
                print(self.board.display())
            index += 1
            self.is_game_terminated()
            self.is_tie()

        if self.tie:
            print("Game ended in a tie !!!")
        elif self.game_terminated:
            print(f"The winner is {self.winner}")


    def is_game_terminated(self):
        winner = ""
        return_value = False
        # test each row:
        if (self.board._b_dict[1] == self.board._b_dict[2] == self.board._b_dict[3]) and (not (self.board._b_dict[1] == Board.EMPTY_CELL)):
            return_value, winner = (True, Player.HUMAN_SYMB) if self.board._b_dict[1] == Player.HUMAN_SYMB else (True, Player.COMP_SYMB)
        elif self.board._b_dict[4] == self.board._b_dict[5] == self.board._b_dict[6] and (not (self.board._b_dict[4] == Board.EMPTY_CELL)):
            return_value, winner = (True, Player.HUMAN_SYMB) if self.board._b_dict[4] == Player.HUMAN_SYMB else (
            True, Player.COMP_SYMB)
        elif self.board._b_dict[7] == self.board._b_dict[8] == self.board._b_dict[9] and (not (self.board._b_dict[7] == Board.EMPTY_CELL)):
            return_value, winner = (True, Player.HUMAN_SYMB) if self.board._b_dict[7] == Player.HUMAN_SYMB else (
            True, Player.COMP_SYMB)
        # test each col
        elif self.board._b_dict[1] == self.board._b_dict[4] == self.board._b_dict[7] and (not (self.board._b_dict[1] == Board.EMPTY_CELL)):
            return_value, winner = (True, Player.HUMAN_SYMB) if self.board._b_dict[1] == Player.HUMAN_SYMB else (
            True, Player.COMP_SYMB)
        elif self.board._b_dict[2] == self.board._b_dict[5] == self.board._b_dict[8] and (not (self.board._b_dict[2] == Board.EMPTY_CELL)):
            return_value, winner = (True, Player.HUMAN_SYMB) if self.board._b_dict[2] == Player.HUMAN_SYMB else (
            True, Player.COMP_SYMB)
        elif self.board._b_dict[3] == self.board._b_dict[6] == self.board._b_dict[9] and (not (self.board._b_dict[3] == Board.EMPTY_CELL)):
            return_value, winner = (True, Player.HUMAN_SYMB) if self.board._b_dict[3] == Player.HUMAN_SYMB else (
            True, Player.COMP_SYMB)
        # test main diagonal
        elif self.board._b_dict[1] == self.board._b_dict[5] == self.board._b_dict[9] and (not (self.board._b_dict[1] == Board.EMPTY_CELL)):
            return_value, winner = (True, Player.HUMAN_SYMB) if self.board._b_dict[7] == Player.HUMAN_SYMB else (
            True, Player.COMP_SYMB)
        # test second diagonal
        elif self.board._b_dict[7] == self.board._b_dict[5] == self.board._b_dict[3] and (not (self.board._b_dict[7] == Board.EMPTY_CELL)):
            return_value, winner = (True, Player.HUMAN_SYMB) if self.board._b_dict[7] == Player.HUMAN_SYMB else (
            True, Player.COMP_SYMB)

        if return_value:
            self.winner = winner
            self.game_terminated = True
        return return_value


    def is_tie(self):
        return False