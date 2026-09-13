def doll_open(size):
    # base case
    if size==1:
        print ("the is the last doll")
        return size
    # the recursive function
    else:
        print(f"openning doll of size: {size}")
        doll_open(size-1)
        print(f"closing doll of size {size}")
doll_open(10)

def russian_doll(size):
    # base case
    if size ==0:
        print(f" you have reached the smallest doll of size {size}")
        return
    # recursive case
    print(f" openning doll : {size}")
    russian_doll(size -1)
    print(f"closing doll : {size}")
    

russian_doll(4)


def count_dolls(n):
    if n == 0:
        return 0
    return 1 + count_dolls(n - 1) 
print(count_dolls(4))       