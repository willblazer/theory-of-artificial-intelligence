import random
# NIM GAME HUMAN VS COMPUTER
print(" WELCOME TO NIM GAME\n GAME DESCRIPTION:THE GAME IS BETWEEN 2 PLAYERS,EACH PLAYER IS TO SELECT 1,2 OR 3 STICKS FROM THE PILES OF STICK THE PLAYER THAT SELECTS THE LAST STICK WINS\n ")
# to determine the number of sticks to start the game
sticks=random.randint(4,50)
print(f"total number of initial sticks is : {sticks}")
# players turn
current_player=0
while True:
    player_2= random.randint(1,3)
    player_1=int(input(" select your number of sticks it can either be 1,2 or 3 : "))
    
    while True:
        if player_1 in [1,2,3]and player_1< sticks:
            break
        print("wrong move, pick another number")

    print(f"you selected :{player_1} sticks, computer picked: {player_2} sticks ")
# TO UPDATE THE STICK
    sticks=sticks-(player_1+player_2)
    print(f"the total number of sticks left is: {sticks} sticks ")
# to collect the win value
    if sticks<=3:
        print(f"you win {current_player}")
    # to swap players
    if current_player==player_1:
        current_player=player_2
    else:
        current_player=player_1
    print (f"player {current_player } wins")



