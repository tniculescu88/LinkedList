import random

from move import Move


class Player:
    HUMAN_SYMB = "X"
    COMP_SYMB = "0"

    def __init__(self, is_computer):
        self._is_computer = is_computer
        if is_computer:
            self._mark = Player.COMP_SYMB
        else:
            self._mark = Player.HUMAN_SYMB

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def mark(self):
        return self._mark

    def get_move(self, user_input):
        if self.is_computer:
            return self.get_computer_move(user_input)
        else:
            return self.get_human_move(user_input)


    def get_human_move(self, user_input):
        while True:
            # user_input = int(input("Please enter your move(1-9)"))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                raise Exception(f"user_input = {user_input} and it is reported as invalid move")
        return move

    def get_computer_move(self, computer_val):
        # random_choice = random.choice(list(range(1,10)))
        random_choice = computer_val
        move = Move(random_choice)
        print("Computer move (1-9): ", move.value)
        return move


# test the player move
# human = Player(is_computer=False)
# comp = Player(is_computer=True)
# print(human.get_move().value)
# print(comp.get_move().value)






