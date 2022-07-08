#tic tac toe example
#authored by Sloan Kelly
#writted by Chris Blicharz 7-7-2022

board = ['1','2','3','4','5','6','7','8','9']
current_token = 'X'
winning_token = ''
tokens_placed = 0

print("Tic - Tac - Toe Example \nBy Sloan Kelly")
print("X starts")

while winning_token == '' and tokens_placed < 9:
    print("\n")
    print("%s|%s|%s" % (board[0], board[1], board[2]))
    print("-+-+-")
    print("%s|%s|%s" % (board[3], board[4], board[5]))
    print("-+-+-")
    print("%s|%s|%s" % (board[6], board[7], board[8]))
    pos = -1
    while (pos == -1):
        pos = int(input("\n%s's turn! Where to? : " %current_token))
        if pos < 1 or pos > 9:
            pos = -1
            print ("This selection is invalid, please pick again!")
        pos = pos - 1
        if board[pos] == 'X' or board[pos] == 'O':
            pos = -1
            print("Sorry! That spot has been taken by %s!"%board[pos])
        board[pos] = current_token
        tokens_placed = tokens_placed+1

        #determine the winner using boolean logic
        row1 = board[0] == board[1] == board[2]
        row2 = board[3] == board[4] == board[5]
        row3 = board[6] == board[7] == board[8]

        col1 = board[0] == board[3] == board[6]
        col2 = board[1] == board[4] == board[7]
        col3 = board[2] == board[5] == board[8]

        diag1 = board[0] == board[4] == board[8]
        diag2 = board[6] == board[4] == board[8]

        row = row1 or row2 or row3
        col = col1 or col2 or col3
        diag = diag1 or diag2

        if row or col or diag:
            winning_token = current_token
if winning_token != 'X' and winning_token != 'O':
    print("\nThe game is a tie! ")
else:
    print("%s is the winner!"%winning_token)

print("\n")
print("%s|%s|%s" % (board[0], board[1], board[2]))
print("-+-+-")
print("%s|%s|%s" % (board[3], board[4], board[5]))
print("-+-+-")
print("%s|%s|%s" % (board[6], board[7], board[8]))



