# Write a game controller that runs a game, i.e.
# • it asks the human to select a heap size;
# • it asks the human who should play and lets them select two players;
# • permits the two players (computer or human) to play against each other, printing the
# progress of the game
import random
# THIS FUNCTION WILL GENERATE A RANDOM NUMBER BETWEEN 1 AND MINIMUM OF K AND N
def random_value(n,k):
    return random.randint(1,min(k,n))

    #THE GAME IS IN A FULLY OPTIMIZED STATE WHEN THE COMPUTER PLAYS AGAINST HUMAN AND THE COMPUTER WINS 
def fully_optimized(n,k):
    if n%(k+1)==0:
        return random_value(n)
    else:
        return n%(k+1)
# WHEN COMPUTER PLAYS AGAINST HUMAN THIS FUNCTION WILL BE CALLED
def computer_vs_human(n,k):
    name=input("welcome player ,please enter your name")
    while n>0:
        while True:
                 try:
                        move=int(input(f" {name}, there are {n} numbers of stick make a move\n"))
                        if 1<= move <= min (k,n):
                            n-=move
                            print(f"{name} picked{move}, there are {n} sticks left")
                        else:
                            print(f"wrong move, select from 1 to {min(k,n)}")
                            break

                 except ValueError:
                        print("invalid move")
                        continue
                 if n==0:
                        print(f"{name} wins!!!!!")
                        break
                    # computer choice
                 move=fully_optimized(n,k)
                 n-=move
                 print(f"computer choose {move}, there are {n} sticks left")
                 if n==0:
                        print("computer wins!!")
                        break
#  WHEN HUMAN PLAYS AGAINST HUMAN THIS WILL BE CALLED
def human_vs_human(n,k):
        
        player1=input("enter your name\n")
        player2=input("enter your name")
        
        while n>0:
             while True:
                    try:

                        move=int(input(f"{player1} you have a total of {n} sticks select from 1 or 2 or 3 sticks"))
                        if 1<= move <= min(k,n):
                            n-=move
                            print(f" { player1} picked {move}  sticks\n you have {n} sticks left")
                        else:
                            print(f"invalid move select from 1 to {min(k,n)}")
                            break
                    except ValueError:
                        print("invalid move")
                        continue
                    if n==0:
                        print(f"{player1} wins")
                        break
                    try:
                        move=int(input(f"{player2}you have a total of {n} sticks select from 1 or 2 or 3 sticks"))
                        if 1<= move <= min(k,n):
                            n-=move
                            print(f" { player2} picked {move}  sticks\n you have {n} sticks left")
                        else:
                            print(f"invalid move select from 1 to {min(k,n)}")
                            break
                    except ValueError:
                        print("invalid move")
                        continue
                    if n==0:
                        print(f"{player2} wins")
                        break
# THIS FUNCTION WILL BE CALLED WHEN RANDOM PLAYER IS SELECTED

def random_player(n,k):
        turn=0
        while n >0:
             move=random_value(n,k)
             n-=move
             print(f" you have {n } number of sticks \n player {turn+1}  played :{move}")
                
             turn=1-turn
             print (f" player {turn+ 1 } wins")

    # THIS FUNCTION GIVES AN OPTION FOR THE USER TO SELECT THE MODE OF THE GAME THEY WANT TO PLAY
def nim_play(n,k):
    select=int(input("what mode of the game do you want to play\ncomputer_vs_human select 0 \n for random_player select 1 \n for human_vs_human select 2"))
    if select==0:
        computer_vs_human(n,k)
        
    elif select==1:
        random_player(n,k)
    elif select==2:
        human_vs_human(n,k)
    else:
        print("invalid option")
         
    

nim_play(20,5)