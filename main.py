# -------- Global Variables -----------

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
gameStillGoing = True
winner = None
currentPlayer = "X"

def displayBoard():
    print(board[0], " | ", board[1], " | ", board[2])
    print(board[3], " | ", board[4], " | ", board[5])
    print(board[6], " | ", board[7], " | ", board[8])


def playGame():
    global gameStillGoing
    while gameStillGoing:
        displayBoard()
        placePlay(currentPlayer)
        decideWinner()	
        flipPlayer()

    if winner == "X" or winner == "O":
        displayBoard()
        print(winner, " won!")
    else:
        displayBoard()
        print("Tie!")


def placePlay(currentPlayer):
    print(currentPlayer + "'s turn")
    print("Choose a position from 1-9:")
    position = input()
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        displayBoard()
        print("Invaild Option, choose a different position from 1-9:")
        position = input()
    
    position = int(position) - 1

    while board[position] != "-":
        displayBoard()
        print("Invaild Option, choose a different position from 1-9:")
        position = input()

    board[position] = currentPlayer

def decideWinner():
    checkIfWin()
    checkIfTie()

def flipPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    return

def checkIfWin():
	global winner
    # Check rows
	rowWinner = checkRows()
    # Check columns
	columnWinner = checkColumns()
    # Check diagonals
	diagonalWinner = checkDiagonals()

	if rowWinner:
		winner = rowWinner
	elif columnWinner:
		winner = columnWinner
	elif diagonalWinner:
		winner = diagonalWinner
	else:
		return
	
def checkRows():
	global gameStillGoing
	row1 = board[0] == board[1] == board[2] != "-"
	row2 = board[3] == board[4] == board[5] != "-"
	row3 = board[6] == board[7] == board[8] != "-"	

	if row1 or row2 or row3:
		gameStillGoing = False
	if row1:
		return board[0]
	if row2:
		return board[3]
	if row3:
		return board[6]
	return



def checkColumns():
	global gameStillGoing
	columns1 = board[0] == board[3] == board[6] != "-"
	columns2 = board[1] == board[4] == board[7] != "-"
	columns3 = board[2] == board[5] == board[8] != "-"	

	if columns1 or columns2 or columns3:
		gameStillGoing = False
	if columns1:
		return board[0]
	if columns2:
		return board[1]
	if columns3:
		return board[2]
	return

def checkDiagonals():
	global gameStillGoing
	diagonals1 = board[0] == board[4] == board[8] != "-"
	diagonals2 = board[2] == board[4] == board[6] != "-"	

	if diagonals1 or diagonals2:
		gameStillGoing = False
	if diagonals1:
		return board[0]
	if diagonals2:
		return board[6]
	return


def checkIfTie():
    global gameStillGoing
    if "-" not in board:
        gameStillGoing = False

playGame()
