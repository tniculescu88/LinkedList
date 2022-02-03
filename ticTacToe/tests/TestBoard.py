from board import Board

def test_board_is_initialized():
    b1 = Board()
    actualString = b1.display()
    print(actualString)
    expectedString = '''
Demo Positions:
|1|2|3|
|4|5|6|
|7|8|9|
Board:
| | | |
| | | |
| | | |'''
    assert actualString == expectedString