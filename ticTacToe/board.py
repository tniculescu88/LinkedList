from player import Player

class Board:
    ACTUAL_BOARD = 1
    DEMO_BOARD = 0
    EMPTY_CELL = " "

    def __init__(self):
        self._b_dict = {1:" ", 2:" ", 3:" ",
                        4:" ", 5:" ", 6:" ",
                        7:" ", 8:" ", 9:" "}

    def update_poz(self, poz:int, player_symbol:int):
        if poz in self._b_dict:
            if self._b_dict[poz] == Board.EMPTY_CELL:
                self._b_dict[poz] = player_symbol
            else:
                print("Current player attempted to mark an already marked place. Player looses his turn")

    def display_aux(self, value):
        if value == Board.ACTUAL_BOARD:
            ret_string = "\nBoard:"
        else:
            ret_string = "\nDemo Positions:"
        for i in range(3):
            ret_string += "\n|"
            for poz in sorted(self._b_dict)[i*3:(i+1)*3]:
                if value == Board.ACTUAL_BOARD:
                    ret_string += f"{self._b_dict[poz]}|"
                else:
                    ret_string += f"{poz}|"
        return ret_string

    def display(self):
        final_string = ""
        final_string += self.display_aux(Board.DEMO_BOARD)
        final_string += self.display_aux(Board.ACTUAL_BOARD)
        return final_string

# print("bogus")
# gb = Board()
# player = Player(is_computer=False)
# # before move
# print(gb.display())
# # after move
# gb.update_poz(player.get_move().value, player.mark)
# print(gb.display())


