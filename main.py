# This is a tic-tac-toe game for two players


# Game data
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


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


def check_player(player):
    """check with player is now playing"""
    player_name = None
    if not player:
        player_name = "Player O"
    elif player:
        player_name = "Player X"
    return player_name


def check_input(player_name) -> str:
    """check if input is in correct format"""
    list_of_correct_answers = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
    correct_form = False
    player_move = None
    while not correct_form:
        player_move = input(
            f"ROW = 1,2,3 COLUMN = 1,2,3\n{player_name}\nPlease input row and column:\n")
        correct_form = player_move in list_of_correct_answers
    return player_move


def transform_input(player_move):
    """change a string input to an integer"""
    row = int(int(player_move[0]) - 1)
    column = int(int(player_move[1]) - 1)
    return row, column


def check_empty_space(player_name, row, column):
    """check if player's input is in an empty space in the board of game"""
    while board[row][column] != ' ':
        player_mov = check_input(player_name)
        row, column = transform_input(player_mov)
        if board[row][column] == ' ':
            return row, column
    return row, column


def game_move(player, row, column):
    """place the player's mark ('X' or 'O') on the board"""
    if player:
        if board[row][column] == ' ':
            board[row][column] = 'X'
    elif not player:
        if board[row][column] == ' ':
            board[row][column] = 'O'


def winner_check(x_winner=False, o_winner=False, board_is_full=False):
    """print which player won"""
    if x_winner is True:
        print("Winner is player X")
    elif o_winner is True:
        print("Winner is player O")
    elif board_is_full is True:
        print("It is Draw")


def game_over(x_winner=False, o_winner=False, board_is_full=False):
    """end of game condition"""
    if x_winner is True or o_winner is True or board_is_full is True:
        return False
    else:
        return True


def if_x_winner():
    """check if X player is winner"""
    x_winner = False
    if f"{board[0][0]}{board[0][1]}{board[0][2]}" == "XXX" or \
            f"{board[1][0]}{board[1][1]}{board[1][2]}" == "XXX" or \
            f"{board[2][0]}{board[2][1]}{board[2][2]}" == "XXX" or \
            f"{board[0][0]}{board[1][0]}{board[2][0]}" == "XXX" or \
            f"{board[0][1]}{board[1][1]}{board[2][1]}" == "XXX" or \
            f"{board[0][0]}{board[1][1]}{board[2][2]}" == "XXX" or \
            f"{board[0][2]}{board[1][2]}{board[2][2]}" == "XXX" or \
            f"{board[0][2]}{board[1][1]}{board[2][0]}" == "XXX":
        x_winner = True
    return x_winner


def if_o_winner():
    """check if O player is winner"""
    o_winner = False
    if f"{board[0][0]}{board[0][1]}{board[0][2]}" == "OOO" or \
            f"{board[1][0]}{board[1][1]}{board[1][2]}" == "OOO" or \
            f"{board[2][0]}{board[2][1]}{board[2][2]}" == "OOO" or \
            f"{board[0][0]}{board[1][0]}{board[2][0]}" == "OOO" or \
            f"{board[0][1]}{board[1][1]}{board[2][1]}" == "OOO" or \
            f"{board[0][0]}{board[1][1]}{board[2][2]}" == "OOO" or \
            f"{board[0][2]}{board[1][2]}{board[2][2]}" == "OOO" or \
            f"{board[0][2]}{board[1][1]}{board[2][0]}" == "OOO":
        o_winner = True
    return o_winner


def full_board():
    """check if a board of game is full"""
    board_is_full = False
    all_pol = [val for sublist in board for val in sublist]
    if all(n != ' ' for n in all_pol):
        board_is_full = True
    return board_is_full


def main():
    """tic tac toe game"""
    player_one = True
    player_two = False
    game_on = True
    visualize_board()
    intro()
    while game_on:
        player = check_player(player_one)
        player_choice = check_input(player)
        row, column = transform_input(player_choice)
        row, column = check_empty_space(player, row, column)
        game_move(player_one, row, column)
        visualize_board()
        winner_x = if_x_winner()
        winner_o = if_o_winner()
        draw = full_board()
        winner_check(winner_x, winner_o, draw)
        game_on = game_over(winner_x, winner_o, draw)
        player_one, player_two = player_two, player_one


if __name__ == '__main__':
    main()
