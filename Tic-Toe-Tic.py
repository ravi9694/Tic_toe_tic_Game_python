import random

def PrintBoard(array,arraysize) :
    if arraysize == 3 :
        for x in range(3) :
            print("|-----|-----|-----|")
            print("| ",array[x][0]," | ",array[x][1]," | ",array[x][2]," |")
        print("|-----|-----|-----|")

    if arraysize == 4 :
        for x in range(4) :
            print("|-----|-----|-----|-----|")
            print("| ",array[x][0]," | ",array[x][1]," | ",array[x][2]," | ",array[x][3]," |")
        print("|-----|-----|-----|-----|")

    if arraysize == 5 :
        for x in range(5) :
            print("|-----|-----|-----|-----|-----|")
            print("| ",array[x][0]," | ",array[x][1]," | ",array[x][2]," | ",array[x][3]," | ",array[x][4]," |")
        print("|-----|-----|-----|-----|-----|")

    if arraysize == 6 :
        for x in range(6) :
            print("|-----|-----|-----|-----|-----|-----|")
            print("| ",array[x][0]," | ",array[x][1]," | ",array[x][2]," | ",array[x][3]," | ",array[x][4]," | ",array[x][5]," |")
        print("|-----|-----|-----|-----|-----|-----|")

    if arraysize == 7 :
        for x in range(7) :
            print("|-----|-----|-----|-----|-----|-----|-----|")
            print("| ",array[x][0]," | ",array[x][1]," | ",array[x][2]," | ",array[x][3]," | ",array[x][4]," | ",array[x][5]," | ",array[x][6]," |")
        print("|-----|-----|-----|-----|-----|-----|-----|")

    if arraysize == 8 :
        for x in range(8) :
            print("|-----|-----|-----|-----|-----|-----|-----|-----|")
            print("| ",array[x][0]," | ",array[x][1]," | ",array[x][2]," | ",array[x][3]," | ",array[x][4]," | ",array[x][5]," | ",array[x][6]," | ",array[x][7]," |")
        print("|-----|-----|-----|-----|-----|-----|-----|-----|")

def TakeInput(array,arraysize,symbol) :
    print("Enter number corresponding to box")
    a = int(input())
    while True :
        if a > arraysize*arraysize or a < 1:
            print("Enter a vaild number")
            a = int(input())
        else :
            b = (a-1)%arraysize
            c = int((a-1-b)/arraysize)
            if array[c][b] == " " :
                array[c][b] = symbol
                break
            else :
                print("That box is filled. Please choose another box")
                a = int(input())

def ComputerInput(array,arraysize) :
    a = random.randint(1,arraysize*arraysize)
    while True :
        if a > arraysize*arraysize or a < 1 :
            a = random.randint(1,arraysize*arraysize)
        else :
            b = (a-1)%arraysize
            c = int((a-1-b)/arraysize)
            if array[c][b] == " " :
                array[c][b] = "C"
                break
            else :
                a = random.randint(1,arraysize*arraysize)

def CheckWin(array,arraysize,symbol) :
    a = True
    for x in range(arraysize) :
        a = True
        for y in range(arraysize) :
            if array[x][y] != symbol :
                a = False
                break
        if a == True : return a
        
    for x in range(arraysize) :
        a = True
        for y in range(arraysize) :
            if array[y][x] != symbol :
                a = False
                break
        if a == True : return a
        
    a = True
    for x in range(arraysize) :
        if array[x][x] != symbol :
            a = False
    if a == True : return a

    a = True
    for x in range(arraysize) :
        if array[x][arraysize-1-x] != symbol :
            a = False
    if a == True : return a
            



def Draw(array,arraysize) :
    a = True
    for x in range(arraysize) :
        for y in range(arraysize) :
            if array[x][y] == " " :
                a = False
                break
    return a
        

#For select difficulty level.
print("Please select your difficulty")
print("Enter E for easy, M for medium and H for hard")
dl = input()

#For select board size.
if dl == 'E' :
    print("Aviable board size is 3*3 and 4*4")
    print("Enter 3 for 3*3 board and 4 for 4*4")
    board_size = int(input())
    if board_size != 3 and board_size != 4:
        print("Enter a vaild board size")
        board_size = int(input())

if dl == 'M' :
    print("Aviable board size is 5*5 and 6*6")
    print("Enter 5 for 5*5 board and 6 for 6*6")
    board_size = int(input())
    if board_size != 5 and board_size != 6:
        print("Enter a vaild board size")
        board_size = int(input())

if dl == 'H' :
    print("Aviable board size is 7*7 and 8*8")
    print("Enter 7 for 7*7 board and 8 for 8*8")
    board_size = int(input())
    if board_size != 7 and board_size != 8:
        print("Enter a vaild board size")
        board_size = int(input())
        

#Numbering of boxes
print("Numbering of boxes")
if board_size == 3 :
    for x in range(3) :
        print("|-----|-----|-----|")
        print("| ",3*x+1," | ",3*x+2," | ",3*x+3," |")
    print("|-----|-----|-----|")

if board_size == 4 :
    for x in range(2) :
        print("|------|------|------|------|")
        print("| ",4*x+1,"  | ",4*x+2,"  | ",4*x+3,"  | ",4*x+4,"  |")
    print("|------|------|------|------|")
    print("| ",9,"  | ",10," | ",11," | ",12," |")
    print("|------|------|------|------|")
    print("| ",13," | ",14," | ",15," | ",16," |")
    print("|------|------|------|------|")

if board_size == 5 :
    print("|------|------|------|------|------|")
    print("| ",1,"  | ",2,"  | ",3,"  | ",4,"  | ",5,"  |")
    print("|------|------|------|------|------|")
    print("| ",6,"  | ",7,"  | ",8,"  | ",9,"  | ",10," |")
    for x in range(2,5) :
        print("|------|------|------|------|------|")
        print("| ",5*x+1," | ",5*x+2," | ",5*x+3," | ",5*x+4," | ",5*x+5," |")
    print("|------|------|------|------|------|")

if board_size == 6 :
    print("|------|------|------|------|------|------|")
    print("| ",1,"  | ",2,"  | ",3,"  | ",4,"  | ",5,"  | ",6,"  |")
    print("|------|------|------|------|------|------|")
    print("| ",7,"  | ",8,"  | ",9,"  | ",10," | ",11," | ",12," |")
    for x in range(2,6) :
        print("|------|------|------|------|------|------|")
        print("| ",6*x+1," | ",6*x+2," | ",6*x+3," | ",6*x+4," | ",6*x+5," | ",6*x+6," |")
    print("|------|------|------|------|------|------|")

if board_size == 7 :
    print("|------|------|------|------|------|------|------|")
    print("| ",1,"  | ",2,"  | ",3,"  | ",4,"  | ",5,"  | ",6,"  | ",7,"  |")
    print("|------|------|------|------|------|------|------|")
    print("| ",8,"  | ",9,"  | ",10," | ",11," | ",12," | ",13," | ",14," |")
    for x in range(2,7) :
        print("|------|------|------|------|------|------|------|")
        print("| ",7*x+1," | ",7*x+2," | ",7*x+3," | ",7*x+4," | ",7*x+5," | ",7*x+6," | ",7*x+7," |")
    print("|------|------|------|------|------|------|------|")

if board_size == 8 :
    print("|------|------|------|------|------|------|-----|------|")
    print("| ",1,"  | ",2,"  | ",3,"  | ",4,"  | ",5," | ",6,"  | ",7,"  | ",+8,"  |")
    print("|------|------|------|------|------|------|-----|------|")
    print("| ",9,"  | ",8+2," | ",8+3," | ",8+4," | ",8+5," | ",8+6," | ",8+7," | ",8+8," |")
    for x in range(2,8) :
        print("|------|------|------|------|------|------|------|------|")
        print("| ",8*x+1," | ",8*x+2," | ",8*x+3," | ",8*x+4," | ",8*x+5," | ",8*x+6," | ",8*x+7," | ",8*x+8," |")
    print("|------|------|------|------|------|------|------|------|")

print("You can play with friend or computer")
print("Enter F for friend and C for computer")
mode = input()

if mode == "C" :
    print("Symbol for computer is 'C'")
    print("Select your symbol to fill box")
    symbol = input()
    Comp_symbol = "C"

if mode == "F" :
    print("Enter symbol for first player")
    P1_symbol = input()
    print("Enter symbol for second player")
    P2_symbol = input()

Board = [[" " for x in range(board_size)] for y in range(board_size)]
print("Good Luck")
print("Board is ready")
PrintBoard(Board,board_size)

#With Computer
if mode == "C" :
    while True :
        print("Player turn")
        TakeInput(Board,board_size,symbol)
        PrintBoard(Board,board_size)
        if CheckWin(Board,board_size,symbol) :
            print("Congratulations! You win the match")
            break
        if Draw(Board,board_size) :
            print("Match is draw")
            break
        print("Computer turn")
        ComputerInput(Board,board_size)
        PrintBoard(Board,board_size)
        if CheckWin(Board,board_size,Comp_symbol) :
            print("Congratulations! Computer win the match")
            break
        if Draw(Board,board_size) :
            print("Match is draw")
            break
        
#With Player
if mode == "F" :
    while True :
        print("Player 1 turn")
        TakeInput(Board,board_size,P1_symbol)
        PrintBoard(Board,board_size)
        if CheckWin(Board,board_size,P1_symbol) :
            print("Congratulations! Player 1 win the match")
            break
        if Draw(Board,board_size) :
            print("Match is draw")
            break
        print("Player 2 turn")
        TakeInput(Board,board_size,P2_symbol)
        PrintBoard(Board,board_size)
        if CheckWin(Board,board_size,P2_symbol) :
            print("Congratulations! Player 2 win the match")
            break
        if Draw(Board,board_size) :
            print("Match is draw")
            break
        



        
        
