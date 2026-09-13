import random
# def piles():
#     return random.randint(4,30)
    


# def computer_choice():
#     return random.randint(1,min(3,piles()))
    
# # print(f"the computer choose :{computer_choice()}")
# def nim_game ():
#     turn=0
#     while piles ()> 0:
#         move=computer_choice()
#         sticks= piles()
#         sticks-=move
#         print(f"player { turn+1} played: {move } you have {sticks} sticks left")
#         turn=1-turn      
#     print(f"player {turn+ 1 } wins")

# nim_game()
# def random_player(n):
#     return random.randint(1, min(3,n))
# # def nim_play(n):
# #     turn=0
# #     while n >0:
# #         move=random_player(n)
# #         n-=move
# #         print(f" you have {n } number of sticks \n player {turn+1}  played :{move}")
        
# #         turn=1-turn
# #     print (f" player {turn+ 1 } wins")

# # nim_play(10)

# def nim_play_human_vs_computer(n):
#     name=input("what is you name")
#     while n >0:
#         while True:
#             try:
                
#                 move=int(input(f"you have a total of {n} sticks select from 1 or 2 or 3 sticks"))
#                 if 1<= move <= min(3,n): 
#                     n-=move
#                     print(f"you picked {move} numbers of stick\n you have {n} numbers of stick lef")   
#                 else:
#                     print(f"enter a valid number from 1 and a {min(3,n)} sticks")  
#                     break 
#             except ValueError:
#                 print("select a valid number")
#                 continue
#             if n==0:
#                 print(f"{name} wins")
#                 break
                
#             # computers move
            
#             move=random_player(n)
#             n-=move
#             print(f"computer chose {move} ,you have {n} sticks left")
#             if n==0:
#                 print("computer wins")
#                 break
                

# nim_play_human_vs_computer(10)



# def human_vs_human(n):
    
#     player1=input("enter your name\n")
#     player2=input("enter your name")
#     print(f"you have a total of {n} sticks")
#     while n>0:
#         while True:
#             try:

#                 move=int(input(f"{player1} you have a total of {n} sticks select from 1 or 2 or 3 sticks"))
#                 if 1<= move <= min(3,n):
#                     n-=move
#                     print(f" { player1} picked {move}  sticks\n you have {n} sticks left")
#                 else:
#                     print(f"invalid move select from 1 to {min(3,n)}")
#                     break
#             except ValueError:
#                 print("invalid move")
#                 continue
#             if n==0:
#                 print(f"{player1} wins")
#                 break
#             try:
#                 move=int(input(f"{player2}you have a total of {n} sticks select from 1 or 2 or 3 sticks"))
#                 if 1<= move <= min(3,n):
#                     n-=move
#                     print(f" { player2} picked {move}  sticks\n you have {n} sticks left")
#                 else:
#                     print(f"invalid move select from 1 to {min(3,n)}")
#                     break
#             except ValueError:
#                 print("invalid move")
#                 continue
#             if n==0:
#                 print(f"{player2} wins")
#                 break
# human_vs_human(10)
                

def player_1(n):
    name=input("player 1 enter your name")   
    while n>0:
        while True:
            try:
                move=int(input(f"{name} ,there are {n} sticks available make a move"))
                
                if 1<=move<=min(3,n) :
                    n-=move
                    print(f"{name} played {move},{n} sticks left") 
                else:
                    print(f"invalid move choose either 1 or {min(3,n)}") 
                    break           
            except ValueError:
                print("invalid move")
                continue
            if n==0:
                print(f"{name} wins")
                break
        
def player_2(n):
    name=input("player 1 enter your name")   
    while n>0:
        while True:
            try:
                move=int(input(f"{name} ,there are {n} sticks available make a move"))
                
                if 1<=move<=min(3,n) :
                    n-=move
                    print(f"{name} played {move},{n} sticks left") 
                else:
                    print(f"invalid move choose either 1 or {min(3,n)}") 
                    break           
            except ValueError:
                print("invalid move")
                continue
            if n==0:
                print(f"{name} wins")

def human_vs_humann(n):
    turn=0
    if player_1(n)

         player_1(n)
         player_2(n)

human_vs_humann(10)