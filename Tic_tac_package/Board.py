class Board:
    def __init__(self):
        self.board_state = [" " for _ in range(9)]

    def display_board(self):
        for row in [self.board_state[i:i + 3] for i in range(0, 9, 3)]:
            print(" | ".join(row))
            print("-" * 9)

    def empty_board(self, position):
        return self.board_state[position] == " "

    def full_board(self):
        return " " not in self.board_state

    def make_move(self, position, symbol):
        if self.empty_board(position):
            self.board_state[position] = symbol
            return True
        else:
            return False

    def check_winner(self, symbol):
        for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                      [0, 3, 6], [1, 4, 7], [2, 5, 8],
                      [0, 4, 8], [2, 4, 6]]:
            if all(self.board_state[i] == symbol for i in combo):
                return True
        return False
