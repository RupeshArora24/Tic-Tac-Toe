board = ["-","-","-","-","-","-","-","-","-"]
you = "X"
winner = None
gameRunning = True
currentPlayer = "X"

def printBoard(board):  #1 printing the game board 
    print(board[0] + " | " + board[1]+" | "+board[2])
    print("--|---|---")
    print(board[3] + " | " + board[4]+" | "+board[5])
    print("--|---|---")
    print(board[6] + " | " + board[7]+" | "+board[8])

#step 2 take player input 
def playerInput(board):
    inp = int(input("Enter a number 1-9 : "))
    if inp >=1 and inp<=9 and board[inp-1]== "-": # here we are checking the entered input is valid or not, and is the place is empty to mae the entry
        board[inp-1]=currentPlayer # here we are updating the value of board list by adding the X or O into the space
    else :
        print("Oops player is alredy in the spot ! ")




# Step 3 - check for win or losse
def chekHrizontal(board):
    global winner # whenever we changes the value here then it occour in whole file as in python methods if make changes they are for that method, by adding global it will make the changes to variable all over the file.
    if board[0] == board[1] == board[2] and board[1]!="-":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[3]!="-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[8]!="-":
        winner = board[6]
        return True
    
def checkVerticle(board) :
      global winner # whenever we changes the value here then it occour in whole file as in python methods if make changes they are for that method, by adding global it will make the changes to variable all over the file.
      if board[0] == board[3] == board[6] and board[0]!="-":
        winner = board[3]
        return True
      elif board[1] == board[4] == board[7] and board[1]!="-":
        winner = board[4]
        return True
      elif board[2] == board[5] == board[8] and board[8]!="-":
        winner = board[5]
        return True 

def checkSideways(board) :
      global winner # whenever we changes the value here then it occour in whole file as in python methods if make changes they are for that method, by adding global it will make the changes to variable all over the file.
      if board[0] == board[4] == board[8] and board[0]!="-":
        winner = board[4]
        return True
      elif board[2] == board[4] == board[6] and board[2]!="-":
        winner = board[4]
        return True
               
# Step 4 - check for a  tie 
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It is a tie")
        gameRunning = False


# Step 5 - switch the player
def switchPlayer(board):
    if currentPlayer =="X":
        currentPlayer=="Y"
    else :
        currentPlayer="X"    

# step 5 - check for win or tie again
while gameRunning:
    printBoard(board) 
    playerInput(board)        