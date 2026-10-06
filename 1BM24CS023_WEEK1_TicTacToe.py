board=[" "]*9
def winner(player):
    combinations=[(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8)]
    for a,b,c in combinations:
        if board[a]==player and board[b]==player and board[c]==player:
            return True
    return False
def display():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("--+---+--")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("--+---+--")
    print(board[6]+" | "+board[7]+" | "+board[8])
def computer_move():
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            if winner("O"):
                return
            board[i]=" "
    for i in range(9):
        if board[i]==" ":
            board[i]="X"
            if winner("X"):
                board[i]="O"
                return
            board[i]=" "
    for i in [4,0,2,6,8,1,3,5,7]:
        if board[i]==" ":
            board[i]="O"
            return
for turn in range(9):
    position=int(input("Enter position: "))-1
    if position<0 or position>8 or board[position]!=" ":
        print("Invalid position")
        continue
    board[position]="X"
    display()
    if winner("X"):
        print("You win!")
        break
    if " " not in board:
        print("Draw!")
        break
    computer_move()
    print("computer played")
    display()
    if winner("O"):
        print("Computer wins!")
        break
    if " " not in board:
        print("Draw!")
        break