import sys
import pytest
from game import Game
from board import Board
from player import Player

@pytest.fixture()
def initialize_game():
    b = Board()
    human = Player(is_computer=False)
    comp = Player(is_computer=True)
    g = Game(board=b, comp=comp, human=human)

# def test_game_first_few_moves():
#     b = Board()
#     human = Player(is_computer=False)
#     comp = Player(is_computer=True)
#
#     g = Game(board=b, comp=comp, human=human)
#     human_list_of_moves = [1,3]
#     comp_list_of_moves =  [2,4]
#     g.play_game(human_list_of_moves, comp_list_of_moves)


def test_board_is_full():
    b = Board()
    human = Player(is_computer=False)
    comp = Player(is_computer=True)
    g = Game(board=b, comp=comp, human=human)
    human_list_of_moves = [1,7,3,6,8]
    comp_list_of_moves =  [4,2,5,9]
    g.play_game(human_list_of_moves, comp_list_of_moves)
    print(f"Board = {g.board._b_dict}")
    assert g.board.is_board_full()


def test_human_wins_1st_row():
    b = Board()
    human = Player(is_computer=False)
    comp = Player(is_computer=True)
    g = Game(board=b, comp=comp, human=human)
    human_list_of_moves = [1,2,3]
    comp_list_of_moves =  [4,5,9]
    g.play_game(human_list_of_moves, comp_list_of_moves)
    assert g.winner == "X"

def test_comp_wins_1st_row():
    b = Board()
    human = Player(is_computer=False)
    comp = Player(is_computer=True)
    g = Game(board=b, comp=comp, human=human)
    human_list_of_moves = [4,5,9]
    comp_list_of_moves =  [1,2,3]
    g.play_game(human_list_of_moves, comp_list_of_moves)
    assert g.winner == "0"

def test_human_wins_2nd_row():
    b = Board()
    human = Player(is_computer=False)
    comp = Player(is_computer=True)
    g = Game(board=b, comp=comp, human=human)
    human_list_of_moves = [4,5,6]
    comp_list_of_moves =  [3,7,9]
    g.play_game(human_list_of_moves, comp_list_of_moves)
    assert g.winner == "X"

def test_comp_wins_2nd_row():
    b = Board()
    human = Player(is_computer=False)
    comp = Player(is_computer=True)
    g = Game(board=b, comp=comp, human=human)
    human_list_of_moves = [3,7,9]
    comp_list_of_moves =  [4,5,6]
    g.play_game(human_list_of_moves, comp_list_of_moves)
    assert g.winner == "0"