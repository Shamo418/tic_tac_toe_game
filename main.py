# This is a tic-tac-toe game for two players
# Game data
GAME_ON = True
player_one = False
player_two = True

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


# Game functions

def visuale_board():
    print(f"      COL1 I COL2 I COL3"
          f"\n     *-----*-----*-----*\nROW1 *  {board[0][0]}  I  {board[0][1]}  I  {board[0][2]}  *\n"
          f"     *-----*-----*-----*\nROW2 *  {board[1][0]}  I  {board[1][1]}  I  {board[1][2]}  "
          f"*\n     *-----*-----*-----*\nROW3 *  {board[2][0]}  I  {board[2][1]}  I  {board[2][2]}  "
          f"*\n     *-----*-----*-----*\n ")


def check_input():
    if player_two:
        player_name = "Player O"
    elif player_one:
        player_name = "Player X"
    player_move = input(f"ROW = 1,2,3 COLUMN = 1,2,3\n{player_name} - Please input row and column in format XX:\n")
    while player_move != '11' and player_move != '12' and player_move != '13' and \
            player_move != '21' and player_move != '22' and player_move != '23' and \
            player_move != '31' and player_move != '32' and player_move != '33':
        player_move = input(
            f"ROW = 1,2,3 COLUMN = 1,2,3\n{player_name} - \nThe answer can only be: \n11 or 12 or 13 or 21 or 22 or "
            f"23 or 31 or 32 or 33 \nPlease input row and column:\n")
    if player_move == '11' or player_move == '12' or player_move == '13' or \
            player_move == '21' or player_move == '22' or player_move == '23' or \
            player_move == '31' or player_move == '32' or player_move == '33':
        row = int(int(player_move[0]) - 1)
        column = int(int(player_move[1]) - 1)
        while board[row][column] != ' ':
            player_move = input(
                f"ROW = 1,2,3 COLUMN = 1,2,3\n{player_name} - Please input row and column in empty place\n")
            row = int(int(player_move[0]) - 1)
            column = int(int(player_move[1]) - 1)
        return row, column
    else:
        print("Error :)")


def game_move(player_choice):
    row = player_choice[0]
    column = player_choice[1]
    if player_one:
        if board[row][column] == ' ':
            board[row][column] = 'X'
    elif player_two:
        if board[row][column] == ' ':
            board[row][column] = 'O'


def winner_check():
    global GAME_ON
    all_pol = [val for sublist in board for val in sublist]
    if f"{board[0][0]}{board[0][1]}{board[0][2]}" == "XXX" or f"{board[1][0]}{board[1][1]}{board[1][2]}" == "XXX" or \
            f"{board[2][0]}{board[2][1]}{board[2][2]}" == "XXX" or f"{board[0][0]}{board[1][0]}{board[2][0]}" == "XXX" or \
            f"{board[0][1]}{board[1][1]}{board[2][1]}" == "XXX" or f"{board[0][0]}{board[1][1]}{board[2][2]}" == "XXX" or \
            f"{board[0][2]}{board[1][2]}{board[2][2]}" == "XXX" or f"{board[0][2]}{board[1][1]}{board[2][0]}" == "XXX":
        print("Winner is player X")
        GAME_ON = False
    elif f"{board[0][0]}{board[0][1]}{board[0][2]}" == "OOO" or f"{board[1][0]}{board[1][1]}{board[1][2]}" == "OOO" or \
            f"{board[2][0]}{board[2][1]}{board[2][2]}" == "OOO" or f"{board[0][0]}{board[1][0]}{board[2][0]}" == "OOO" or \
            f"{board[0][1]}{board[1][1]}{board[2][1]}" == "OOO" or f"{board[0][0]}{board[1][1]}{board[2][2]}" == "OOO" or \
            f"{board[0][2]}{board[1][2]}{board[2][2]}" == "OOO" or f"{board[0][2]}{board[1][1]}{board[2][0]}" == "OOO":
        print("Winner is player O")
        GAME_ON = False
    elif all(n != ' ' for n in all_pol):
        print("It is Draw")
        GAME_ON = False


# Game
visuale_board()
while GAME_ON:
    if not player_two:
        player_one = False
        player_two = True
    elif player_two:
        player_one = True
        player_two = False
    player_choice = check_input()
    game_move(player_choice)
    print('\n' * 40)
    visuale_board()
    winner_check()
