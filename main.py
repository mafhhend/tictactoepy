board=["-"] * 9

game_still_going=True
winner=None
current_player="X"


def display_board():
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])


def  handle_turn(player):
    position= int(input("Choose a position from 1-9:")) -1
    board[position] = player
    display_board()


def check_for_winner():
    global winner

    row_winner=check_rows()
    column_winner=check_columns()
    diagonal_winner=check_diagonals()
    if row_winner:
        winner=row_winner
        pass
    elif column_winner:
        winner=column_winner
        pass
    elif diagonal_winner:
        winner=diagonal_winner
        pass
    else:
        winner=None
        pass


    return
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False

    pass

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player ="X"
    return


def check_rows():
    # Setup global variables
    global game_still_going
    row_1=board[0] == board [1] == board[2] !="-"
    row_2=board[3] == board [4] == board[5] !="-"
    row_3=board[6] == board [7] == board[8] !="-"

    if row_1 or row_2 or row_3:
        game_still_going=False
    # Return the winner 
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # Setup global variables
    global game_still_going
    column_1=board[0] == board [3] == board[6] !="-"
    column_2=board[1] == board [4] == board[7] !="-"
    column_3=board[2] == board [5] == board[8] !="-"

    if column_1 or column_2 or column_3:
        game_still_going=False
    # Return the winner 
    if column_1:
        return board[0]
    elif column_2:
        return board[3]
    elif column_3:
        return board[6]
    return



def check_diagonals():
    # Setup global variables
    global game_still_going
    diagonal_1=board[0] == board [4] == board[8] !="-"
    diagonal_2=board[6] == board [4] == board[2] !="-"

    if diagonal_1 or diagonal_2:
        game_still_going=False
    # Return the winner 
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_game_over():
    check_for_winner()
    check_if_tie()
def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        # Change Player
        flip_player()
    if winner =="X" or winner == "O":
        print(winner,"won")
    elif winner ==None:
        print("Tie.")

play_game()