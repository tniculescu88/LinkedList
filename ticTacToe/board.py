class Board:
    ACTUAL_BOARD = 1
    DEMO_BOARD = 0
    def __init__(self):
        self._b_dict = {1:" ", 2:" ", 3:" ",
                        4:" ", 5:" ", 6:" ",
                        7:" ", 8:" ", 9:" "}


    def make_move(self, poz, player_symbol):
        if poz in self._b_dict:
            self._b_dict[poz] = player_symbol

    def display_aux(self, value):
        if value == Board.ACTUAL_BOARD:
            ret_string = "Board:"
        else:
            ret_string = "Demo Positions:"
        for i in range(3):
            ret_string += "\n|"
            for poz in sorted(self._b_dict)[i*3:(i+1)*3]:
                if value == Board.ACTUAL_BOARD:
                    ret_string += f"{self._b_dict[poz]}|"
                else:
                    ret_string += f"{poz}|"
        print(ret_string)


    def display(self):

        self.display_aux(Board.DEMO_BOARD)
        self.display_aux(Board.ACTUAL_BOARD)
