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
    if str(board[position-1]).isnumeric():
        return True
    else:
        return False


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

    while not game_over(board):
        print_board(board)
        list = ["x", "o"]
        turn = eval(input("choose a position: "))
        position = turn
        character = str(list[0])
        fill_spot(board, position, character)

        turn2 = eval(input("choose a position: "))
        position2 = turn2
        character2 = str(list[1])
        fill_spot(board, position2, character2)

    ans = 'y'
    while ans[0] == 'y':
        winning_game(board)
        ans = input("play again? ")
        play(build_board())


def main():
    play(build_board())


if __name__ == '__main__':
    main()
