def sum(a,b,c):
    return a+b+c
def printboard(xstate,zstate):
    zero = 'X' if xstate[0] else ('O' if zstate[0] else 0)
    one = 'X' if xstate[1] else ('O' if zstate[1] else 0)
    two = 'X' if xstate[2] else ('O' if zstate[2] else 0)
    three = 'X' if xstate[3] else ('O' if zstate[3] else 0)
    four = 'X' if xstate[4] else ('O' if zstate[4] else 0)
    five = 'X' if xstate[5] else ('O' if zstate[5] else 0)
    six = 'X' if xstate[6] else ('O' if zstate[6] else 0)
    seven = 'X' if xstate[7] else ('O' if zstate[7] else 0)
    eight = 'X' if xstate[8] else ('O' if zstate[8] else 0)

    print(f" {zero} | {one} | {two} ")
    print(f"-- |-- |--")
    print(f" {three} | {four} | {five} ")
    print(f"-- |-- |--")
    print(f" {six} | {seven} | {eight} ")
    
def checkwin(xstate,zstate):
    wins = [[0,1,2],[0,3,6],[1,4,7],[2,5,8],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("X Won the match")
            return 1
        if(sum(zstate[win[0]],xstate[win[1]],zstate[2])==3):
            print("O won the match")
            return 0 
    return -1

xstate = [0]*9
zstate = [0]*9
turn = 1
print("welcome to the game")
while(True):
    printboard(xstate,zstate)
    if(turn == 1):
        print("X's chance")
        value = int(input("enther the number"))
        xstate[value]= 1

        
    else:
        print("O's chance")
        value = int(input("enther the number"))
        zstate[value]=1
    cwin = checkwin(xstate,zstate)
    if(cwin != -1 ):
        print("match over")
        break
    turn = 1 - turn
