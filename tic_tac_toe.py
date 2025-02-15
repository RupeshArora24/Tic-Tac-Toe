board = ["-","-","-","-","-","-","-","-","-"]
you = "X"
winner = None
gameRunning = True

def printBoard():  #1 printing the game board 
    print(board[0] + " | " + board[1]+" | "+board[2])
    print("--|---|---")
    print(board[3] + " | " + board[4]+" | "+board[5])
    print("--|---|---")
    print(board[6] + " | " + board[7]+" | "+board[8])

if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0]  #2 Lists  
    OState = [0,0,0,0,0,0,0,0]
    turn = 1 # 1 for x and 0 for o
    print("Welcome to Tic Tac Toe")
    print("X's Chance")
    printBoard()