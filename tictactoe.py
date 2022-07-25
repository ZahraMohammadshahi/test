import random

player_1 = input("player_1: ")
player_2 = input("player_2: ")

def player(x,y):
    player = []
    player.append(x)
    player.append(y)
    first = random.choice(player)
    return first


user = player(player_1, player_2)
print(f"{user} starts the game and is shown by 'x' on board")
turns = 0
board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
    ]

def board_game(board):
    for i in board:
        for j in i:
            print(f"{j} ", end="")
        print()

def quit(user_input):
    if user_input == "q":
        print("quit of game, thanks")
        return True
    else:
        return False

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "_":
        print("this position isn't empty")
        return True
    return False

def coordinate(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(user_input % 3)
    return(row, col)

def add_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user):
    if user : return "x"
    else: return "o"

def is_win(user, board):
    if check_row(user, board) : return True
    if check_col(user, board): return True
    if check_diame(user, board): return True
    return False

def check_diame(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[2][0] == user and board[1][1] == user and board[0][2] == user:
        return True
    else: return False

def check_row(user, board):
    for row in board:
        completed_row = True
        for j in row:
            if j != user:
               completed_row = False 
               break
        if completed_row : return True
    return False
    

def check_col(user, board):
    for col in range(3):
        completed_col = True
        for row in range(3):
            if board[row][col] != user:
               completed_col = False 
               break
        if completed_col : return True     
    return False


while turns < 9:                                                                
    active_user = current_user(user)
    board_game(board)
    user_input = input("please eneter position 1 to 9 or enter 'q' :")
    if quit(user_input):
        break
    user_input = int(user_input)-1
    coords = coordinate(user_input)
    if istaken(coords, board):
        print("try again")
        continue
    add_board(coords, board, active_user)
    if is_win(active_user, board):
        print(f"{active_user}, WIN!")
        break
 
    turns += 1
    user = not user