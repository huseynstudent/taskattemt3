gameboard=[0,0,0,0,0,0,0,0,0]

def goster():
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
    sira=0
    played_moves=[]
    while sira<9:
        if sira%2==0:
            player="birinci oyuncu"
            marker=1
        else:
            player="ikinci oyuncu"
            marker=2
        print(f"{player}nun sırasıdır.")
        print("damalar:\n1 2 3\n4 5 6\n7 8 9")
        move=int(input("Haraya oynamaq istiyirsiniz?: "))
        if move in played_moves or move<1 or move>9:
            print("Yanlış hərəkət. Təkrar yoxlayın.")
        else:
            played_moves.append(move)
            gameboard[move-1]=marker
            goster()
            if check_winner()==True:
                print(f"{player} qazandı! 🥳🎆🎉🎉🎉")
                break
            sira+=1
    if sira==9:
        print("Bərabərlik (￣_,￣ )")
play()