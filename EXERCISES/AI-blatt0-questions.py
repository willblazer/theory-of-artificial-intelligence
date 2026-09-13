# # quuestion 0.1
# # a program that prints hello world
print("hello world")
# # using variables to perform same task
s="hello world"
print(s)
# # assignment 0.2
# # . Consider the following code:
i = 1
print(i)
# #1. What is the content of variable i after running it? the content of the variable of i is 1

# # 2. What is the type of the variable i? How to find this out?
print(type(i))
# # 3. What happens if, after the line from Assignment 0.2.1, you run
i+=3
print(i)
# # the new value of i becomes 4

# # Assignment 0.3
# # Let a list mylist be given as follows:
mylist = [1, 2, 3, 4, 5]
# # 1. how do you return the 1st element of the list?
print(mylist[0])
# # 2. how do you return the 4th element of the list?
print(mylist[3])
# # 3. Show three different ways of deleting the entry ’3’ from mylist. Each time, check that it worked and reset mylist to its original state.
mylist.remove(3)
print (mylist)
# # 2nd way
mylist = [1, 2, 3, 4, 5]
mylist.pop(2)
print(mylist)
# # 3rd approach
mylist = [1, 2, 3, 4, 5]
del mylist[3]
print(mylist)

# # Assignment 0.4
# # 1. Write a Python script to print all numbers from 3 to 10 inclusive.
i=3
while i <=10:
    print(i)
    i+=1
# # # 2. Write a Python script to print all even numbers until, but not including 12
i=0
for i in range(16):
    if i%2==0:
        if i==12:
            continue
        print (i)
        i+=1
# # another approach to solving the question
for i in range(0, 14, 2):
    print(i)
        
# # 3. Write a Python script that prints all entries of a given list. Say, the list is given by
mylist = [1, "jack", 5.0, 6, 9, 13]
print(mylist[:])
for entry in mylist:
    print(entry)
# # 4. Do the same as in Assignment 0.4.3, but print the number of the entry, starting with 0, in front of each item.
for i ,entry in enumerate(mylist):
    print(i,entry)

# # 5. We want to write a Python script that takes a list and throws away all entries except those
# # with value 3 or 3.0.
mylist = [2, 3, 5, 3.0, 7, 3, 9, 3.0]
for i, value in enumerate (mylist):
    if value!=3 or value!=3.0:
        mylist.remove(value)
        print(i,mylist)
# # What’s wrong or risky about the following (possibly multiple things), and how to fix it?
# # the block was not properly indented

mylist = [2, 3, 5, 3.0, 7, 3, 9, 3.0]
for val in mylist:
    if not val == 3:
        mylist.remove(val)

# Assignment 0.5
# 1. Write a list comprehension in Python that collects all even numbers, starting with 2 and ending
# with 20.
mylist=[i for i in range (2,22,2)]
print(mylist)
mylist=[i for i in range(2,22)if i%2==0]
print(mylist)
# a programme that prints the boolean expression
mylist=[i%2==0 for i in range(2,22) ]
print(mylist)
# 2. Write a list comprehension in Python that collects all numbers from 1 to 10 with their squares,
# combined as tuples, e.g. (5, 25).
mylist=[(i,i*i )for i in range(1,11)]
print(mylist)
# 3. Write a list comprehension that collects all the numbers that divide 36 (you can use brute
# force).
mylist=[num for num in range(1,37) if 36%num==0]
print (mylist)
mylist=[num for num in range(1,36+1) if 36%num==0]
print (mylist)
# 4. List comprehensions can combine multiple enumerations and conditions.
# Write a list comprehension that collects all the pairs (i,j), each between 1 and 10 (including)
# such that the sum of i and j is no larger than 50 and one of them divides the other.
mylist=[(i,j )for i in range(1,10+1) for j in range (1,10+1) if i+j<=50 and i%j==0 or  j%i==0]
print(mylist)
# 5. Finally, try to write a list comprehension that executes the task from Assignment 0.4.5, namely
# collecting only the values 3 and 3.0 from a given list.
mylist = [2, 3, 5, 3.0, 7, 3, 9, 3.0]
my_newlist=[i for i in mylist if i==3 or i==3.0]
print(my_newlist)

# Assignment 0.6

# The current assignments look at functions a bit more in detail.
# 1. Write a function sqr(x) that returns the square of its argument x, a number.
# def square(x):
#     return (x**2) 
# print(square(10))
# print(square(1))


# # 2. Write a function modify(li) which takes a list and changes its last entry to "modified". Test
# # the function.
li=[i for i in range(1,10+1)]
def modify(li):
    li[-1]="modified"
    return li
print(modify(li))

# # 3. Consider the following example.
# a = 3
# def fun(a):
#     print(a)
# print(a)
# print(fun(2))
# # What will this print? it will print 3 first and then prints 2

# 4. Consider the following code:
def fun(x):
    return 2*x
f = fun
print(f)
# What does f contain after running this code?  f contains  the function fun

# What will f(3) do? it will print 6
print(f(3))
# 5. Write two functions, left() and right(). The function left() does nothing else but printing
# left, and analogously, right().
def left():
    print("left")
 
def right():
    print("right")

# # Write function walk(), for ten steps, alternatingly prints left and right, using above func-
# tions.
# Can you write it so that each iteration only prints once?
def walk():
    for i in range(1,10+1):
        right()
        left()
    
walk()
# Assignment 0.7
# Consider the following code:
def triple_fun():
    return 1
    return 2
    return 3
print(triple_fun())
print(triple_fun())
print(triple_fun())
# What will it print? it wil print 1

# What about this one? it will print , it will print 1,2,3
# #! /usr/bin/python3
def triple_yield():
    yield 1
    yield 2
    yield 3
print(triple_yield())
for i in triple_yield():
    print(i)

# Assignment 0.8
# You have four numbers (integers or floats) x,y,z,u.
    
   
# Write a function sort4(.) that takes 4 numerical arguments and returns a sorted tuple of these
def sort4(x,y,z,u):
    if x> y:
        x,y=y,x
    elif x> z:
        x,z=z,x
    elif x>u:
        x,u=u,x
    else:
        x=x

    if y>z:
        y,z=z,y
    elif y>u:
        y,u=u,y
    else:
        y=y
    if z>u:
        z,u=u,z
    else:
        z=z
    return(x,y,z,u)
print(sort4(10,5,6,2))
# ANOTHER WAY
def sort4(x,y,z,u):
    # sort 2 pairs each first
    if x>y:
        x,y=y,x
    if z>u:
        z,u=u,z
    # making x the smallest number
    if x>z:
        x,z=z,x
    # making u the largest number
    if y>u:
        y,u=u,y
    # sorting the middle pair
    if y>z:
        y,z=z,y
    return(x,y,z,u)
print(sort4(10,5,6,2))
# sorting 5 numbers
def sort5(a,b,c,d,e):
    # sorting the pairs
    if a>b:
        a,b=b,a
    if c>d:
        c,d=d,c
   
    # making e the largest number
    if b>d:
        b,d=d,b
    if d>e:
        d,e=e,d
    # making a the lowest
    if a>c:
        a,c=c,a
    # sorting the middle
    if b>c:
        b,c=c,b
    return(a,b,c,d,e)
print(sort5(10,4,3,5,9 ))
# sorting 6 numbers
def sort6(a,b,c,d,e,f):
#     sorting the pair
    if a>b:
        a,b=b,a
    if c> d:
        c,d=d,c
    if e>f:
        e,f=f,e
    # making f the largest number
    if b>d:
        b,d=d,b
    if d> f:
        d,f=f,d
    # making a the lowest number
    if a>c:
        a,c=c,a
    if a> e:
        a,e=e,a
    # sorting the middle
    if b>c:
        b,c=c,b
    # if b> e:
    #     b,e=e,b
    if d>e:
        d,e=e,d
    if c>e:
         c,e=e,c
    return(a,b,c,d,e,f)
print(sort6(10,3,5,1,11,1))
     
# arguments. Do not use the list’s sort() method.
# Assignment 0.9
# Test your sorting algorithm with the permutation generator from the lecture.
# Assignment 0.10∗
# Extend the Tower of Hanoi program to four pins.

# def count_leaves(list,a):

# c=0
# def count_leaves(list):
#     c= len(list[0])+len(list[1])+len(list[2])
#     print(c)
   
# #print(count_leaves([[1,2,3,3,3],[0,0,0,0],[]]))
# count_leaves([[1,2,3,3,3],[0,0,0,0],[]])

def count_leaves(list):
    for i in list.index:
        i+=len(list.index)
        print(i)
count_leaves([[1,2,3,3,3],[0,0,0,0],[]])