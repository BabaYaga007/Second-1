#this program is made to code a game of rock-paper-scissors which is a very popular game between the youth and also the old.
#This game has been used from old times to resolve conflicts and have fun.

from random import randint
def print_menu():
    global items
    print('1 for',items[0])
    print('2 for',items[1])
    print('3 for',items[2])
    print('Enter your choice')

def print_score(a,b):
    print('---Score---')
    print('Player =',a)
    print('Computer =',b)

choice = ['stone','paper','scissor']
items = input()
items = items.split()
a=0
b=0
while(True):
    print_menu()
    ch = int(input())
    if ch==1 :
        player = items[0]
    elif ch==2 :
        player = items[1]
    elif ch==3 :
        player = items[2]
    else :
        print('Invalid Choice. Try Again')
        continue
    rand = randint(0,2)
    computer = choice[rand]
    print('You chose',player)
    print('Computer chose',computer)
    if player=='stone' and computer=='paper':
        b += 1
    elif player=='stone' and computer=='scissor':
        a += 1
    elif player=='paper' and computer=='stone':
        a += 1
    elif player=='paper' and computer=='scissor':
        b += 1
    elif player=='scissor' and computer=='stone':
        b += 1
    elif player=='scissor' and computer=='paper':
        a += 1
    else:
        print("It's a Tie!!!")
    print_score(a,b)
    if a==5 or b==5:
        break  
