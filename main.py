import random

def print_board(board):
    for row in board:
        print("+---+---+---+")
        print("| {} | {} | {} |".format(row[0], row[1], row[2]))
    print("+---+---+---+")

def check_win(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]


    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def board_full(board):
    for row in board:
        for col in row:
            if col == ' ':
                return False
    return True

def play_tic_tac_toe():
    board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
    print_board(board)

    board = [[' ' for _ in range(3)] for _ in range(3)]
    play_now = 'O'


    while True:
        print_board(board)

        if play_now == 'O':
            num = int(input('Your move: '))
            if 1 <= num <= 9:
                row = (num - 1) // 3
                col = (num - 1) % 3
            else:
                print('Please a number 1 to 9: ')
                continue
        else:

            row, col = random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == ' '])

        if board[row][col] == ' ':
            board[row][col] = play_now

            winner = check_win(board)
            if winner:
                print_board(board)
                print(f'¡You win!')
                break
            elif board_full(board):
                print_board(board)
                print('It´s a tie!')
                break

            play_now = 'O' if play_now == 'X' else 'X'
        else:
            print('Invalid move. Try again.')

if __name__ == "__main__":
    play_tic_tac_toe()







