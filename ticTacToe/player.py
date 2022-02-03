class Player:
    HUMAN_SYMB = 1
    COMP_SYMB = 0

    def __init__(self, name, is_computer):
        self.name = name
        self._is_computer = is_computer

    @property
    def is_computer(self):
        return self._is_computer




