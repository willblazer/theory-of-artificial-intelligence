import random
def random_value(n):
    return random.randint(1,min(3,n))
def optimized_move(n):
    if n %4==0:
        # select randomly
        return random_value(n)
    else:
#  select number of sticks in multiply of 4       
        return n%4  
    

    
def nim_play(n):
    name=input("welcome player ,please enter your name")
    while n>0:
        while True:
            try:
                move=int(input(f" {name}, there are {n} numbers of stick make a move\n"))
                if 1<= move <= min (3,n):
                    n-=move
                    print(f"{name} picked{move}, there are {n} sticks left")
                else:
                    print(f"wrong move, select from 1 to {min(3,n)}")
                    break

            except ValueError:
                print("invalid move")
                continue
            if n==0:
                print(f"{name} wins!!!!!")
                break
            # computer choice
            move=optimized_move(n)
            n-=move
            print(f"computer choose {move}, there are {n} sticks left")
            if n==0:
                print("computer wins!!")
                break

nim_play(10)