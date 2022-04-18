"""
Name: Logan Segal
lab 9.py
"""


def build_board():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return list


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    position_index = position - 1
    return str(board[position_index]).isnumeric()


def fill_spot(board, position, character):
    board[position - 1] = character.strip().lower()


def winning_game(board):
    possibilities = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 6], [3, 5, 7]]
    for i in possibilities:
        acc = 0
        for position in i:
            if board[position - 1] == 'x':
                acc = acc + 1
            if acc == 3:
                return True
    for i in possibilities:
        acc = 0
        for position in i:
            if board[position - 1] == 'o':
                acc = acc + 1
            if acc == 3:
                return True
    return False


def game_over(board):
    if winning_game(board):
        return True
    for i in board:
        if str(i).isnumeric():
            return False
    return True


def get_winner(board):
    possibilities = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 6], [3, 5, 7]]
    for i in possibilities:
        acc = 0
        for position in i:
            if board[position - 1] == 'x':
                acc = acc + 1
            if acc == 3:
                return "x"
    for i in possibilities:
        acc = 0
        for position in i:
            if board[position - 1] == 'o':
                acc = acc + 1
            if acc == 3:
                return "o"
    return None


def play(board):
    print("Tik Tak Toe!")
    print("Instructions: player 'x' will go first by typing a number 1-9 depending on where they would like to go. "
          "Then player 'o' will do the same, this will be repeated" "\n" "until there is a winner or the game is tied. "
          "After the game is complete type a word beginning with the letter 'y' to play again, if not type anything "
          "else. :)")
    playing = "y"
    character_string = 'xo'
    index = 0
    while playing[0] == 'y' or playing[0] == "Y":
        while not game_over(board):
            print_board(board)
            position = eval(input("{}'s, choose a position: ".format(character_string[index])))
            while not is_legal(board, position):
                position = input("that position is already filled...please choose a new position:")
            else:
                character = character_string[index]
                fill_spot(board, position, character)
            if winning_game(board):
                print_board(board)
                print(get_winner(board), "'s win!")
                playing = input("play again: ")
                board = build_board()
                index = 1
            if game_over(board) and not winning_game(board):
                print("tie")
                playing = input("play again: ")
                board = build_board()
                index = 1
            index += 1
            index = index % 2


def main():
    board = build_board()
    play(board)


if __name__ == '__main__':
    main()
