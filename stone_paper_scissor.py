from random import randint
def print_menu():
    print('1 for Stone')
    print('2 for Paper')
    print('3 for Scissor')
    print('Enter your choice')

def print_score(a,b):
    print('---Score---')
    print('Player =',a)
    print('Computer =',b)

choice = ['stone','paper','scissor']

a=0
b=0
while(True):
    print_menu()
    ch = int(input())
    if ch==1 :
        player = 'stone'
    elif ch==2 :
        player = 'paper'
    elif ch==3 :
        player = 'scissor'
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
