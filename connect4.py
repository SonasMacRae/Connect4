# This works
def CreateBoard():
    board = []
    for x in range(10):
        board.append(['0','0','0','0','0','0','0','0','0','0'])
    return board


# This works
def PrintBoard(board):
    for x in range(len(board)-1, -1, -1):
        print(board[x])


# Need to check if the counter can be placed in the column
def PlaceCounter(board, player, position):
    for x in range(len(board)):
        if board[x][position] == '0':
            board[x][position] = player
            return board


def CheckBoard(board):
    # Check for horizontal win
    for x in board:
        for y in range(len(board) - 3):
            counter = 0
            for z in range(4):
                if x[y + z] == x[y] and x[y + z] != '0':
                    counter += 1
                else:
                    continue
            if counter == 4:
                return True

    # Check for vertical win
    for x in range(len(board) - 3):
        


def App():
    board = CreateBoard()
    player = 'y'

    counter = 1
    flag = True

    while flag:
        PrintBoard(board)
        if counter % 2 == 0:
            player = 'y'
        else:
            player = 'x'

        print("Enter a number")
        temp = int(input())
        board = PlaceCounter(board, player, temp)
        if CheckBoard(board):
            PrintBoard(board)
            print("game over")
            return
        counter += 1

App()
