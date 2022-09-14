board = """
123
456
789
"""

print("Here's the board:" + board)

while 1 > 0: 
        player_input = input("Enter a # to place an x: ")
        board = board.replace(str(player_input), "x")
        print(board)
        if board[1] == board[2] == board[3] or board[5] == board[6] == board[7] or board[9] == board[10] == board[11] or board[1] == board[5] == board[9] or board[2] == board[6] == board[10] or board[3] == board[7] == board[11] or board[1] == board[6] == board[11] or board[9] == board[6] == board[3]:
            print("PLAYER X WON")
            break

        player2_input = input("Enter a # to place a o: ")
        board = board.replace(str(player2_input), "o")
        print(board)
        if (
            (board[1] == board[2] == board[3]) or 
            (board[5] == board[6] == board[7]) or 
            (board[9] == board[10] == board[11]) or 
            board[1] == board[5] == board[9] or 
            board[2] == board[6] == board[10] or board[3] == board[7] == board[11] or board[1] == board[6] == board[11] or board[9] == board[6] == board[3]):
            print("PLAYER O WON")
            break
