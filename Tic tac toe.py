from shutil import move


print("Tic Tac Toe")
row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
print(row1)
print(row2)
print(row3)
tic_tac=0
def users():
    player1=input("First player's name:")
    player2=input("The second player's name:")
    return player1, player2
def user_choice():
    secim1=input("Please select a number in between 1 and 9.(both included)")
    liste=list(range(1,10))
    while secim1.isdigit() == False:
        print("It's not a digit. Please try a digit between 1 and 9.")    
        secim1=input("Please select a number in between 1 and 9.(both included)")
    secim1=int(secim1)
    while secim1 not in liste:
        print("It's not in between 1-9. Please select a number in between 1 and 9.")
        secim1=int(input("Please select a number in between 1 and 9.(both included)"))
    """secim2=input("Please select what do you want to put on. (X or O)")
    while secim2 not in ["x","X","o","O"]:
        secim2=input("Please select what do you want to put on. (X or O)")
    secim2=secim2.upper() """
    global tic_tac
    tic_tac+=1
    return secim1
def dönüstür(x,y):
    global tic_tac
    if x in range(1,4):
        if row1[x-1]==" ":
            row1[x-1]=y
            print(row1)
            print(row2)
            print(row3)
        else:
            print("This position has already been filled. Please try another position.")
            tic_tac-=1
            print(row1)
            print(row2)
            print(row3)
    elif x in range(4,7):
        x=x-3
        if row2[x-1]==" ":
            row2[x-1]=y
            print(row1)
            print(row2)
            print(row3)
        else:
            print("This position has already been filled. Please try another position.")
            tic_tac-=1
            print(row1)
            print(row2)
            print(row3)
    elif x in range(7,10):
        x=x-6
        if row3[x-1]==" ":
            row3[x-1]=y
            print(row1)
            print(row2)
            print(row3)
        else:
            tic_tac-=1
            print("This position has already been filled. Please try another position.")
            print(row1)
            print(row2)
            print(row3)
    else:
        print("Invalid choice.")
        pass
def check_if_finished(player1,player2):
    if tic_tac%2==0:
        winner=player2
    else:
        winner=player1
    if row1[0]==row2[0]==row3[0]=="X" or row1[0]==row2[0]==row3[0]=="O" or row1[1]==row2[1]==row3[1]=="X" or row1[1]==row2[1]==row3[1]=="O" or row1[2]==row2[2]==row3[2]=="X" or row1[2]==row2[2]==row3[2]=="O" or row1[2]==row2[1]==row3[0]=="X" or row1[2]==row2[1]==row3[0]=="O" or row1[0]==row2[1]==row3[2]=="X" or row1[0]==row2[1]==row3[2]=="O" or row1[0]==row1[1]==row1[2]=="X" or row1[0]==row1[1]==row1[2]=="O" or row2[0]==row2[1]==row2[2]=="X" or row2[0]==row2[1]==row2[2]=="O" or row3[0]==row3[1]==row3[2]=="X" or row3[0]==row3[1]==row3[2]=="O":
        print("Game over! Congratulations, {}!".format(winner))
        return True
    else:
        return False
player1, player2= users()
while check_if_finished(player1,player2)==False:
    what_to_put=""
    if tic_tac%2==0:
        print("It's your turn: {}".format(player1))
        what_to_put="X"
    else:
        print("It's your turn: {}".format(player2))
        what_to_put="O"
    move1=user_choice()
    dönüstür(move1,what_to_put)