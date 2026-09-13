import random
def random_value(n,k):
    return random.randint(1,min(k,n))

    
def fully_optimized(n,k):
    if n%(k+1)==0:
        return random_value(n)
    else:
        return n%(k+1)
    
def nim_play(n,k):
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

nim_play(20,5)