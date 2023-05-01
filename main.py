# Assigns piece variables to numbers 

# Pawn = 1
# Knight = 2
# Bishop = 3
# Queen = 4
# Pope = 5
# Rock = 6
# King = 7

pawns = 0
knights = 0
bishops = 0
queens = 0
popes = 0
rock = 0
king = 0
empty = 0
pieces = [pawns, knights, bishops, queens, popes, rock, king, empty]
pieceidentify = 0
# sets up the board

row0 =    [0,0,0,0,0]
row1 =   [0,0,0,0,0,0]
row2 =  [0,0,0,0,0,0,0]
row3 = [0,0,0,0,0,0,0,0]
row4 =[0,0,0,0,0,0,0,0,0]
row5 = [0,0,0,0,0,0,0,0]
row6 =  [2,0,0,0,0,0,2]
row7 =   [1,3,1,1,3,1]
row8 =    [6,5,7,4,6]
rowcolumn = [row0,row1,row2,row3,row4,row5,row6,row7,row8]
weight = 0
# Prints the board 

def printboard():
    print("      " + str(row0))
    print("     " + str(row1))
    print("   " + str(row2))
    print(" " + str(row3))
    print(str(row4))
    print(" " + str(row5))
    print("   " + str(row6))
    print("     " + str(row7))
    print("      " + str(row8))
    
# Gives Piece value to certain spots on the board of the start

def identifypiece(location):
    if location == 0:
        return "nothing"
    elif  location == 1:
        return "white pawn"
    elif location == 2:
        return "knight"
    elif location == 3:
        return "bishop"
    elif location == 4:
        return "queen"
    elif location == 5:
        return "pope"
    elif location == 6:
        return "Rock"
    elif location == 7:
        return "king"    
    
# Describes how to capture a piece

def capture():
    rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)] = rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]
    rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)] = 0
    
# Decides to move or capture a piece

def move():
    if rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)] == 0:
        print("The " + str(identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)])) + " at " + str(loc1) + " moved to " + str(loc2) + ".")
        rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)],rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)] = rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)],rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]

    else:
        print("The " + identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) + " at " + str(loc1) + " captured the " + identifypiece(rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)]) + " at " + str(loc2))
        capture()

# Counts how many of each type of piece there are

def count(x, y):
    match identifypiece(rowcolumn[x][y]):
        case "nothing":
            return 7
        case "white pawn":
            return 0
        case "knight":
            return 1
        case "bishop":
            return 2
        case "queen":
            return 3
        case "pope":
            return 4
        case "Rock":
            return 5
        case "king":
            return 6

# Prints the number of each piece there is

def printpieces():
    print("Pawns: " + str(pieces[0]))
    print("Knights: " + str(pieces[1]))
    print("Bishops: " + str(pieces[2]))
    print("Queens: " + str(pieces[3]))
    print("Popes: " + str(pieces[4]))
    print("Rocks: " + str(pieces[5]))
    print("Kings: " + str(pieces[6]))

# Reset the count of the number of pieces

def zeropieces():
    for u in range(len(pieces)):
        pieces[u] = 0
    global weight
    weight = 0
# Gets the total weight of all the pieces

def weights(x, y):
    match identifypiece(rowcolumn[x][y]):
        case "nothing":
            return 0
        case "white pawn":
            return 1
        case "knight":
            return 3
        case "bishop":
            return 3
        case "queen":
            return 7
        case "pope":
            return 9
        case "Rock":
            return 0
        case "king":
            return 5
        
# Prints out the game review

def gamereview():
    global weight
    global pieceidentify
    global pieces
    for i in range(len(rowcolumn)):
        for j in range(len(rowcolumn[i])):
            weight = weight + weights(i, j)
            pieceidentify = count(i,j)
            pieces[pieceidentify] = pieces[pieceidentify] + 1
    print("Total weight: " + str(weight))
    printpieces()
    zeropieces()
# Defines the conditions for knight moves

def knightmove(loc1a, loc1b, loc2a, loc2b):
    for i in range(1):
        if loc1a == 4 and loc2a == 6:
            if int(loc1a) - int(loc2a) == -2:
                if int(loc1b) - (int(loc2b)) == -2:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == -1:
                if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 2:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 2:
                if int(loc1b) - (int(loc2b)) == 0:
                    move()
                    break    
        elif loc1a == 6 and loc2a == 4:
            if int(loc1a) - int(loc2a) == -2:
                if int(loc1b) - (int(loc2b)) == 0:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == -1:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 2:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 2:
                if int(loc1b) - (int(loc2b)) == -2:
                    move()
                    break
        else:
            if int(loc1a) - int(loc2a) == -2:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == -1:
                if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1 or int(loc1b) - (int(loc2b)) == 2:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1 or int(loc1b) - (int(loc2b)) == 2:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 2:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
        print("The knight can't move there!")
            
# Defines the conditions for king moves

def kingmove(loc1a, loc1b, loc2a, loc2b):
    for i in range(1):
        if loc1a < 5:
            if int(loc1a) - int(loc2a) == -1:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 0:
                    move()
                    break
            if int(loc1a) - int(loc2a) == 0:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
            if int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - (int(loc2b)) == 0 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
        elif loc1a > 5:
            if int(loc1a) - int(loc2a) == -1:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 0:
                    move()
                    break
            if int(loc1a) - int(loc2a) == 0:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
            if int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 0:
                    move()
                    break
        else:
            if int(loc1a) - int(loc2a) == -1:
                if int(loc1b) - (int(loc2b)) == 0 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
            if int(loc1a) - int(loc2a) == 0:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
            if int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 0:
                    move()
                    break
        print("The king can't move there!")
                
# Defines the conditions for queen moves

def queenmove(loc1a, loc1b, loc2a, loc2b):
    for i in range(1):
        if loc2a == loc1a:
            move()
            break
        if loc1a == 1:
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if loc2a - 5 == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 2:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 3:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 4:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 5:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > loc1a:
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
        if loc1a == 6:
            if loc2a > loc1a:
                if (loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        if loc1a == 7:
            if loc2a > loc1a:
                if (loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        if loc1a == 8:
            if loc2a > loc1a:
                if (loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        if loc1a == 9:
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        print("The queen can't move there!")

# Defines the conditions for pope moves

def popemove(loc1a, loc1b, loc2a, loc2b):
    for i in range(1):
        if loc1a == 4 and loc2a == 6:
            if int(loc1a) - int(loc2a) == -2:
                if int(loc1b) - (int(loc2b)) == -2:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == -1:
                if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 2:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 2:
                if int(loc1b) - (int(loc2b)) == 0:
                    move()
                    break    
        elif loc1a == 6 and loc2a == 4:
            if int(loc1a) - int(loc2a) == -2:
                if int(loc1b) - (int(loc2b)) == 0:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == -1:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 2:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 2:
                if int(loc1b) - (int(loc2b)) == -2:
                    move()
                    break
        else:
            if int(loc1a) - int(loc2a) == -2:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == -1:
                if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1 or int(loc1b) - (int(loc2b)) == 2:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1 or int(loc1b) - (int(loc2b)) == 2:
                    move()
                    break
            elif int(loc1a) - int(loc2a) == 2:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
        if loc2a == loc1a:
            move()
            break
        if loc1a == 1:
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if loc2a - 5 == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 2:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 3:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 4:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 5:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > loc1a:
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
        if loc1a == 6:
            if loc2a > loc1a:
                if (loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        if loc1a == 7:
            if loc2a > loc1a:
                if (loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        if loc1a == 8:
            if loc2a > loc1a:
                if (loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        if loc1a == 9:
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        print("His Majesty, The Pope, can't move there!")

# Defines the conditions for bishop moves
def bishopmove(loc1a, loc1b, loc2a, loc2b):
    for i in range(1):
        if loc2a == loc1a:
            break
        if loc1a == 1:
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if loc2a - 5 == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 2:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 3:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 4:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a > loc1a) and (loc2a < 6):
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (5 - loc1a)) == loc1b:
                        move()
                        break
        if loc1a == 5:
            if loc2a < loc1a:
                if (loc1a - loc2a) == (loc1b - loc2b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a > loc1a:
                if (loc2a - loc1a) == (loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
        if loc1a == 6:
            if loc2a > loc1a:
                if (loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        if loc1a == 7:
            if loc2a > loc1a:
                if (loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        if loc1a == 8:
            if loc2a > loc1a:
                if (loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        if loc1a == 9:
            if (loc2a < loc1a) and (loc2a > 4):
                if abs(loc2a - loc1a) == abs(loc2b - loc1b):
                    move()
                    break
                if loc1b == loc2b:
                    move()
                    break
            if loc2a < 5:
                if loc2b < loc1b:
                    if abs(loc2a - 5) == abs(loc1b - loc2b):
                        move()
                        break
                if loc2b > loc1b:
                    if (loc2b - (loc1a - 5)) == loc1b:
                        move()
                        break
        print("The bishop can't move there!")

# Defines the conditions for white pawn moves

def whitepawnmove(loc1a, loc1b, loc2a, loc2b):
    for i in range(1):
        if int(loc1a) - int(loc2a) == 0:
            if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                if rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)] != 0:
                    move()
                    break
                else:
                    print("There is no piece to capture there!")
            else:
                print("The pawn can't move there!")
        if loc1a < 5:
            if int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 0:
                    move()
                    break
                else:
                    print("The pawn can't move there!")
        elif loc1a > 5:
            if int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 0:
                    move()
                    break
                else:
                    print("The pawn can't move there!")
        else:
            if int(loc1a) - int(loc2a) == 1:
                if int(loc1b) - (int(loc2b)) == 0 or int(loc1b) - (int(loc2b)) == 1:
                    move()
                    break
                else:
                    print("The pawn can't move there!")
# Plays through the game

while True:

    loc1 = str(input("What original location? "))
    if loc1 == "Print Board":
        printboard()
    elif loc1 == "Game Review":
        gamereview()
    else:
        loc1 = loc1.split(",")

        if (int(loc1[0])) > 9 or (int(loc1[0])) < 1 or (int(loc1[1])) < 1 or len(rowcolumn[(int(loc1[0])-1)]) < (int(loc1[1])-1):
            print("The coordinate " + str(loc1) + " is off the board!")
            printboard()
        elif rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)] == 0:
            print("There is no piece there!")
            printboard()
        
        else:
            loc2 = str(input("What new location? "))
            loc2 = loc2.split(",")
            
            if (int(loc2[0])) > 9 or (int(loc2[0])) < 1 or (int(loc2[1])) < 1 or len(rowcolumn[(int(loc2[0])-1)]) < (int(loc2[1])-1):
                print("The coordinate " + str(loc2) + " is off the board!")
                printboard()

            if identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) == "knight":
                knightmove(int(loc1[0]), int(loc1[1]), int(loc2[0]), int(loc2[1]))
            elif identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) == "king":
                kingmove(int(loc1[0]), int(loc1[1]), int(loc2[0]), int(loc2[1]))
            elif identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) == "queen":
                queenmove(int(loc1[0]), int(loc1[1]), int(loc2[0]), int(loc2[1]))
            elif identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) == "pope":
                popemove(int(loc1[0]), int(loc1[1]), int(loc2[0]), int(loc2[1]))
            elif identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) == "bishop":
                bishopmove(int(loc1[0]), int(loc1[1]), int(loc2[0]), int(loc2[1]))
            elif identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) == "white pawn":
                whitepawnmove(int(loc1[0]), int(loc1[1]), int(loc2[0]), int(loc2[1]))
            elif identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) == "Rock":
                print("That's a rock. It can't move.")
            elif identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) == "nothing":
                print("There is no piece there!")
            printboard()
