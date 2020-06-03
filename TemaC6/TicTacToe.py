import random


def print_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_symbol():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to play as X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def turn_move(board, letter, move):
    board[move] = letter


def is_winner(board, letter):
    if board[7] == letter and board[8] == letter and board[9] == letter:
        return True
    if board[4] == letter and board[5] == letter and board[6] == letter:
        return True
    if board[1] == letter and board[2] == letter and board[3] == letter:
        return True
    if board[1] == letter and board[4] == letter and board[7] == letter:
        return True
    if board[2] == letter and board[5] == letter and board[8] == letter:
        return True
    if board[3] == letter and board[6] == letter and board[9] == letter:
        return True
    if board[1] == letter and board[5] == letter and board[9] == letter:
        return True
    if board[7] == letter and board[5] == letter and board[3] == letter:
        return True


def free_space(board, move):
    if board[move] == ' ':
        return True


def player_move(board):
    move = ' '
    while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or not free_space(board, int(move)):
        print('Your move is... (1-9)')
        move = input()
    return int(move)


def random_move(board, movesList):
    possibleMv = []
    for i in movesList:
        if free_space(board, i):
            possibleMv.append(i)
    if len(possibleMv) != 0:
        return random.choice(possibleMv)
    else:
        return None


def copy_board(board):
    cpyBrd = []
    for i in board:
        cpyBrd.append(i)
    return cpyBrd


def computer_move(board, compLetter):
    if compLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 10):  # If A.I can win
        copy = copy_board(board)
        if free_space(copy, i):
            turn_move(copy, compLetter, i)
            if is_winner(copy, compLetter):
                return i
    for i in range(1, 10):  # If player can win
        copy = copy_board(board)
        if free_space(copy, i):
            turn_move(copy, playerLetter, i)
            if is_winner(copy, playerLetter):
                return i

    move = random_move(board, [1, 3, 7, 9])
    if move is not None:
        return move
    elif free_space(board, 5):
        return 5
    else:
        return random_move(board, [2, 4, 6, 8])


def full_board(board):
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True


def reset_game():
    inp = input('Do you want to play again? (y or n)\n')
    if inp.lower() == 'y':
        return True
    else:
        return False


def game():
    print('Welcome Human :)')
    while True:
        board = [' '] * 10
        playerSymbol, compSymbol = player_symbol()
        turn = 'Human'
        gameOn = True
        print(f'The {turn} will go first!')

        while gameOn:
            if turn == 'Human':
                print_board(board)
                move = player_move(board)
                turn_move(board, playerSymbol, move)
                if is_winner(board, playerSymbol):
                    print_board(board)
                    print('Oh, I see... You have won.. Human')
                    gameOn = False
                else:
                    if full_board(board):
                        print_board(board)
                        print('Is a tie.. You are not that bad')
                        gameOn = False
                    else:
                        turn = 'Computer'
            else:
                move = computer_move(board, compSymbol)
                turn_move(board, compSymbol, move)
                if is_winner(board, compSymbol):
                    print_board(board)
                    print('Hahaa you lose Human... Pathetic')
                    gameOn = False
                else:
                    if full_board(board):
                        print_board(board)
                        print('Is a tie.. You are not that bad')
                        gameOn = False
                    else:
                        turn = 'Human'
        if not reset_game():
            break


if __name__ == '__main__':
    game()

