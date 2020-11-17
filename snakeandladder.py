import random

def rollDice() :
    return random.randint(1,6)

def above100(playerpos):
    tempPos = 0
    tempPos = playerpos - 100
    playerpos = 100 - tempPos
    return playerpos

def randomingLadder(snl) :
    i = 0
    while i < 7:
        boxindex1 = random.randint(5,90)
        boxindex2 = random.randint(5,90)
        if boxindex1 > boxindex2 :
            while boxindex2 > (boxindex1 / 10) * 10 :
                boxindex2 = random.randint(5,90)
            if not boxindex1 in snl :
                snl[boxindex2] = boxindex1
                print("The bottom of the ladder is at :", boxindex2, "And the top of the ladder is at :", snl[boxindex2])
                i = i + 1
        elif boxindex2 > boxindex1 :
            while boxindex1 > (boxindex2 / 10) * 10 :
                boxindex1 = random.randint(5,90)
            if not boxindex2 in snl :
                snl[boxindex1] = boxindex2
                print("The bottom of the ladder is at :", boxindex1, "And the top of the ladder is at :", snl[boxindex1])
                i = i + 1
        else :
            boxindex1 = random.randint(5,90)
            boxindex2 = random.randint(5,90)
    print("\n")
    return snl

def randomingSnake(snl) :
    i = 0
    while i < 10 :
        boxindex1 = random.randint(10,95)
        boxindex2 = random.randint(10,95)
        if boxindex1 > boxindex2 :
            while boxindex2 > (boxindex1 / 10) * 10 :
                boxindex2 = random.randint(10,95)
            if not boxindex1 in snl :
                snl[boxindex1] = boxindex2
                print("The head of the snake is at :", boxindex1, "And the tail of the snake is at :", snl[boxindex1])
                i = i + 1
        elif boxindex2 > boxindex1 :
            while boxindex1 > (boxindex2 / 10) * 10 :
                boxindex1 = random.randint(10,95)
            if not boxindex2 in snl :
                snl[boxindex2] = boxindex1
                print("The head of the snake is at :", boxindex2, "And the tail of the snake is at :", snl[boxindex2])
                i = i + 1
        else :
            boxindex1 = random.randint(10,95)
            boxindex2 = random.randint(10,95)
    print("\n")
    return snl




def checkingLadderSnake(snl, playerpos) :
    if playerpos in snl:
        if playerpos < snl[playerpos] :
            print("You hit a ladder at", playerpos ,", your position now :", snl[playerpos])
            playerpos = snl[playerpos]
        elif playerpos > snl[playerpos] :
            print("You hit a snake at", playerpos, ", your position now :", snl[playerpos])
            playerpos = snl[playerpos]
    return playerpos

def singleplayer() :


def twoplayer() :


def start() :
    welcomingmessage()
    gamemode = input()
    


snl = {}
randomingLadder(snl)
randomingSnake(snl)

print(snl)
playerpos = 0
playerpos = 0
play = input()
while playerpos < 100 and play != 'QUIT':
    dice = rollDice()
    print('Your dice is', dice)
    playerpos += dice
    if playerpos > 100 :
        playerpos = above100(playerpos)
    playerpos = checkingLadderSnake(snl, playerpos)
    print(playerpos)
    if playerpos == 100 :
        print('You win!')
    else :
        play = input()


if __name__ == "__main__":
    start()