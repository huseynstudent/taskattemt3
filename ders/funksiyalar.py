gameboard=[0,0,0,0,0,0,0,0,0]

def display_board():
    for i in range(9):
        if gameboard[i]==0:
            print("🟥",end="")
        elif gameboard[i]==1:
            print("❌",end="")
        elif gameboard[i]==2:
            print("⭕",end="")
        if (i+1)%3==0:
            print()

def check_winner():
    for i in range(0, 9, 3):
        if gameboard[i]==gameboard[i+1]==gameboard[i+2] and gameboard[i]!=0:
            return True
    for i in range(3):
        if gameboard[i]==gameboard[i+3]==gameboard[i+6] and gameboard[i]!=0:
            return True
    if gameboard[0]==gameboard[4]==gameboard[8] and gameboard[0]!=0:
        return True
    if gameboard[2]==gameboard[4]==gameboard[6] and gameboard[2]!=0:
        return True
    return False

def play():
    turn=0
    played_moves=[]
    while turn<9:
        if turn%2==0:
            player="birinci oyuncu"
            marker=1
        else:
            player="ikinci oyuncu"
            marker=2
        print(f"{player} sırasıdır.")
        move=int(input("Haraya oynamak istiyorsunuz? (1-9): "))
        if move in played_moves or move<1 or move>9:
            print("Yanlış bir hareket yapıldı. Tekrar deneyin.")
        else:
            played_moves.append(move)
            gameboard[move-1]=marker
            display_board()
            if check_winner():
                print(f"{player} kazandı!")
                break
            turn+=1
    if turn==9:
        print("Berabere!")

play()