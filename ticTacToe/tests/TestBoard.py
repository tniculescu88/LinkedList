import pytest

from board import Board
from player import Player


def test_board_is_updated_for_poz9():
    gb = Board()
    player = Player(is_computer=False)
    # before move
    print(gb.display())
    # after move
    gb.update_poz(player.get_move(9).value, player.mark)
    print(gb.display())
    expectedString = '''
Demo Positions:
|1|2|3|
|4|5|6|
|7|8|9|
Board:
| | | |
| | | |
| | |X|'''
    assert gb.display() == expectedString

def test_board_is_not_updated_for_poz0():
    gb = Board()
    player = Player(is_computer=False)
    # assert that exception thrown when trying to update the poz on the board to an invalid value
    with pytest.raises(Exception):  gb.update_poz(player.get_move(0).value, player.mark)
