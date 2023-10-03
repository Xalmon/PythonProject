class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self):
        while True:
            try:
                move = int(input(f"{self.name}, enter your move (1-9): ")) - 1
                if 0 <= move < 9:
                    return move
                else:
                    print("Invalid input. Enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Enter a valid number.")
