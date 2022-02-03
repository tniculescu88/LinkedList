import pytest
from player import Player
from move import Move

# def mocked_get_move(input_valid_value):
#     return Move(input_valid_value)

def test_human_player_valid_move9():
    human = Player(is_computer=False)
    actual_value = human.get_move(9).value
    assert actual_value == 9

def test_human_player_valid_move1():
    human = Player(is_computer=False)
    actual_value = human.get_move(1).value
    assert actual_value == 1

def test_human_player_invalid_move0():
    human = Player(is_computer=False)
    with pytest.raises(Exception):  actual_value = human.get_move(0).value
