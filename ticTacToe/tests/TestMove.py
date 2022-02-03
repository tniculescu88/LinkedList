from move import Move
from player import Player
from board import Board

def test_move_validPoz():
    move = Move(1)
    assert move.is_valid()
    move1 = Move(9)
    assert move1.is_valid()


def test_move_invalidPozNegative():
    move = Move(-1)
    assert not move.is_valid()

def test_move_invalidPoz10():
    move = Move(10)
    assert not move.is_valid()

def test_move_invalidPozString():
    move = Move('abc')
    assert not move.is_valid()

def test_getColPoz1():
    move = Move(1)
    assert move.get_row() == 0
    assert move.get_column() == 0


