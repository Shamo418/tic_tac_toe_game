"""This is a tic-tac-toe game for two players"""


# Game data
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

X, O = 'X', 'O'


# Game functions
def intro():
    """print a welcome text and a rules of game"""
    print("Welcome players :) Have a nice game.")
    print("Choose your move. Remember that the answer can only be: \n"
          "11 or 12 or 13 or \n21 or 22 or 23 or \n31 or 32 or 33 \n")


def visualize_board():
    """print the text image of the game board"""
    print(f"      COL1 I COL2 I COL3"
          f"\n     *-----*-----*-----*\nROW1 *  {board[0][0]}  I  {board[0][1]}  I  {board[0][2]}  *\n"
          f"     *-----*-----*-----*\nROW2 *  {board[1][0]}  I  {board[1][1]}  I  {board[1][2]}  "
          f"*\n     *-----*-----*-----*\nROW3 *  {board[2][0]}  I  {board[2][1]}  I  {board[2][2]}  "
          f"*\n     *-----*-----*-----*\n ")


def proper_answer(player) -> str:
    """check if input(players move) is in correct format and return player's move"""
    list_of_correct_answers = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
    correct_form = False
    player_move = None
    while not correct_form:
        player_move = input(
            f"ROW = 1,2,3 COLUMN = 1,2,3\nPlayer {player}\nPlease input row and column:\n")
        correct_form = player_move in list_of_correct_answers
    return player_move


def transform_input(player_move):
    """change a string input (player's answer) to an integer used as coordinates for the board"""
    row = int(int(player_move[0]) - 1)
    column = int(int(player_move[1]) - 1)
    return row, column


def empty_space_on_board(player, row, column):
    """return position of board if player's move is in an empty space"""
    while board[row][column] != ' ':
        player_move = proper_answer(player)
        row, column = transform_input(player_move)
        if board[row][column] == ' ':
            return row, column
    return row, column


def set_mark_on_board(player, row, column):
    """place the player's mark ('X' or 'O') on the board"""
    if player == X:
        if board[row][column] == ' ':
            board[row][column] = X
    elif player == O:
        if board[row][column] == ' ':
            board[row][column] = O


def winner_print(winner, board_is_full, player):
    """print which player won or if there was a draw"""
    if winner is True:
        print(f"Winner is player {player}")
    elif board_is_full is True and winner is False:
        print("It is Draw")


def keep_playing(winner=False, board_is_full=False) -> bool:
    """checks if there is a game winner or if there is a tie. If it is, it ends the game"""
    if winner is True or board_is_full is True:
        return False
    else:
        return True


def is_winner(player) -> bool:
    """return true if player is winner"""
    winner = False
    players_marks = None
    if player == X:
        players_marks = "XXX"
    elif player == O:
        players_marks = "OOO"
    if f"{board[0][0]}{board[0][1]}{board[0][2]}" == players_marks or \
            f"{board[1][0]}{board[1][1]}{board[1][2]}" == players_marks or \
            f"{board[2][0]}{board[2][1]}{board[2][2]}" == players_marks or \
            f"{board[0][0]}{board[1][0]}{board[2][0]}" == players_marks or \
            f"{board[0][1]}{board[1][1]}{board[2][1]}" == players_marks or \
            f"{board[0][0]}{board[1][1]}{board[2][2]}" == players_marks or \
            f"{board[0][2]}{board[1][2]}{board[2][2]}" == players_marks or \
            f"{board[0][2]}{board[1][1]}{board[2][0]}" == players_marks:
        winner = True
    return winner


def is_full_board() -> bool:
    """return True if a board of game is full"""
    board_is_full = False
    # Create list of place from the board of game
    all_position = [position for sublist in board for position in sublist]
    # Check if all positions are full
    if all(position != ' ' for position in all_position):
        board_is_full = True
    return board_is_full


def main():
    """tic tac toe game"""
    player_one = X
    player_two = O
    game_on = True
    visualize_board()
    intro()
    while game_on:
        # Start of game by player X, next will be player O

        # Choice of place on the board by player
        player_choice = proper_answer(player_one)
        # Transform of choice and add mark on the board
        row, column = transform_input(player_choice)
        row, column = empty_space_on_board(player_one, row, column)
        set_mark_on_board(player_one, row, column)
        visualize_board()
        # Check if there is a winner or a draw
        winner = is_winner(player_one)
        draw = is_full_board()
        winner_print(winner, draw, player_one)
        game_on = keep_playing(winner, draw)
        # Change of player ( X - O)
        player_one, player_two = player_two, player_one


if __name__ == '__main__':
    main()
