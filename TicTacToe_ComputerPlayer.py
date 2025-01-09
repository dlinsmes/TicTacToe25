#don't need to code in a function to run

#variables don't need to be declared with types

#global variables - same as class variables
#can be used by any function in the file
board = []
piece = "o"
moveRow = -1
moveCol = -1

def main():
    setupBoard()
    printBoard()

    while not winner() and not tie():
        changePiece()
        makeMove()
        printBoard()

    if winner():
        print(piece + " won!")
    else:
        print("tie game!")

def setupBoard():
    #i iterates 0-1-2
    for i in range (3):
        row = []
        for j in range(3):
            row.append("_")
        board.append(row)

def printBoard():
    #for-each loop
    for row in board:
        # print(row)
        line = ""
        for spot in row:
            line += spot + "  "
        print(line)
    print()

def winner():

    rowCount = 0
    colCount = 0
    d1Count = 0
    d2Count = 0

    for i in range(len(board)):
        if board[moveRow][i] == piece:
            rowCount += 1
        if board[i][moveCol] == piece:
            colCount += 1
        if board[i][i] == piece:
            d1Count += 1
        if board[i][len(board)-1-i] == piece:
            d2Count += 1

    if rowCount == 3 or colCount == 3 or d1Count == 3 or d2Count == 3:
        return True

    return False

def tie():
    #if there are any blank spots, there can't be a tie game
    for row in board:
        for spot in row:
            if spot == "_":
                return False
    return True

def changePiece():
    #if a function needs to check or change a global (class) var, use this:
    global piece

    if piece == "o":
        piece = "x"
    else:
        piece = "o"

def makeMove():
    global moveRow
    global moveCol

    #only need the global line if the function is changing or checking the value of the var??
    print(piece + "'s turn")

    #human player is x
    if piece == "x":

        moveRow = int(input("Enter row: "))
        moveCol = int(input("Enter col: "))

        #len(list) is list length
        while(moveRow < 0 or moveRow > 2 or moveCol < 0 or moveCol >= len(board)
               or board[moveRow][moveCol] != "_"):
            print("invalid coordinate")
            moveRow = int(input("Enter row: "))
            moveCol = int(input("Enter col: "))

    else:
        moveRow, moveCol = ai_turn()

    board[moveRow][moveCol] = piece

def ai_turn():
    row = -1
    col = -1

    #your logic goes here

    #python functions can return multiple values
    return row, col

main()