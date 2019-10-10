def triple(dice):
    c,x = 0,0
    for i in dice:
        for j in dice:
            if j == i:
                c += 1
        if c==3:
            x = i
        if c > 3:
            x = i
        c = 0
    print(x)
    return x
def score(dice):
    score = 0
    x = triple(dice)
    if x!=0:
        if x==1:
            score += 1000
            print('Here at 1')
        elif x==6:
            score += 600
        elif x==5:
            score += 500
        elif x==4:
            score += 400
            print('Here at 4')
        elif x==3:
            score += 300
        elif x==2:
            score += 200
        else:
            score += 0
    for i in dice:
        if i==1:
            score += 100
        elif i==5:
            score += 50
        else:
            score += 0
    return score

n = int(input())
print('9 to exit')
print('any to continue')
if n != 9:
    print(score([5,1,3,4,1]))
    print(score([1,1,1,3,1]))
    print(score([2,4,4,5,4]))
    
