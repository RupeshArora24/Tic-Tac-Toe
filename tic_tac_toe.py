board = ["-","-","-","-","-","-","-","-","-"]
you = "X"
winner = None
gameRunning = True
currentPlayer = "X"

def printBoard():  #1 printing the game board 
    print(board[0] + " | " + board[1]+" | "+board[2])
    print("--|---|---")
    print(board[3] + " | " + board[4]+" | "+board[5])
    print("--|---|---")
    print(board[6] + " | " + board[7]+" | "+board[8])

#step 2 take player input 
def playerInput(board):
    inp = int(input("Enter a number 1-9 : "))
    if inp >=1 and inp<=9 and inp== "-": # here we are checking the entered input is valid or not, and is the place is empty to mae the entry
        board[inp-1]=currentPlayer


# Step 3 - check for win or tie

# Step 4 - switch the player
 
# step 5 - check for win or tie again
while gameRunning:
    printBoard(board) 
    playerInput(board)        