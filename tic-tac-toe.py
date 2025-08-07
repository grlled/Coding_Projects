import random
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
gameRunning = True
currentPlayer = "X"
winner = None

choice = input("Type PVP for Player vs Player Tic-Tac-Toe\nType PVC for Player vs Computer Tic-Tac-Toe\n").lower()

while choice not in ["pvp", "pvc"]:
    choice = input("Invalid choice. Please type PVP or PVC: ").lower()


#printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    
#take player input
def playerInput(board):
    inp = int(input("\nPick a number 1-9!\n"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oh no! That spot is taken. (Or is beyond given range)")
#checking for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        printBoard(board)
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        printBoard(board)
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        printBoard(board)
        return True
        
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        printBoard(board)
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        printBoard(board)
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        printBoard(board)
        return True
        
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        printBoard(board)
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        printBoard(board)
        return True
        
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("\nThis game is a Tie!")
        gameRunning = False
        
def checkWin():
    global gameRunning
    if checkHorizontal(board) or checkRow(board) or checkDiagonal(board):
        print(f"The winner is {winner} !!!")
        gameRunning = False
        
#switch players
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
        
# THE computer
def computer(board):
    global currentPlayer
    if currentPlayer == "O":
        position = random.randint(0, 8)
        while board[position] != "-":
            position = random.randint(0, 8)
        board[position] = "O"
        switchPlayer()
    

#check for win or tie again
while gameRunning:
    if choice == "pvc":
        printBoard(board)
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()
        computer(board)
        checkWin()
        checkTie(board)
    else:
        printBoard(board)
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()