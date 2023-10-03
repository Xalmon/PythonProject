from Tic_tac_package.Board import Board
from Tic_tac_package.Player import Player


def main():
    board = Board()
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")

    current_player = player1

    while not board.full_board():
        board.board()
        move = current_player.make_move()

        if board.make_move(move, current_player.symbol):
            if board.check_winner(current_player.symbol):
                board.board()
                print(f"{current_player.name} wins!")
                break
            else:
                current_player = player2 if current_player == player1 else player1
        else:
            print("Invalid move. That spot is already taken.")

    if not board.check_winner(player1.symbol) and not board.check_winner(player2.symbol):
        board.board()
        print("It's a tie!")


if __name__ == "__main__":
    main()
