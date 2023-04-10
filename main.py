import tkinter as tk
// Assigns piece variables to numbers //
# Pawn = 1
# Kight = 2
# Bishop = 3
# Queen = 4
# Chancellor = 5
# Camel1 = 6
# Camel2 = 8
# King = 7
// sets up the board //
row0 =    [0,0,0,0,0]
row1 =   [0,0,0,0,0,0]
row2 =  [0,0,0,0,0,0,0]
row3 = [0,0,0,0,0,0,0,0]
row4 =[0,0,0,0,0,0,0,0,0]
row5 = [0,0,0,0,0,0,0,0]
row6 =  [2,0,0,0,0,0,2]
row7 =   [1,3,1,1,3,1]
row8 =    [6,5,7,4,8]
rowcolumn = [row0,row1,row2,row3,row4,row5,row6,row7,row8]
// Prints the board //
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
// Gives Piece value to certain spots on the board of the start //
def identifypiece(location):
    if  location == 1:
        return "pawn"
    elif location == 2:
        return "knight"
    elif location == 3:
        return "bishop"
    elif location == 4:
        return "queen"
    elif location == 5:
        return "THE POPE"
    elif location == 6:
        return "camel"
    elif location == 7:
        return "king"
    elif location == 8:
        return "camel"    
// Describes the conditions for capture //
def capture():
    rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)] = rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]
    rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)] = 0
// Describes the conditions for moving pieces //
def move():
    if rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)] == 0:
        print("The " + str(identifypiece(rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)])) + " at " + str(loc1) + " moved to " + str(loc2) + ".")
        rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)],rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)] = rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)],rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]

    else:
        print("The " + identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) + " at " + str(loc1) + " captured the " + identifypiece(rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)]) + " at " + str(loc2))
        capture()
// Gives knight pieces the ability to move //        
def knightmove(loc1a, loc1b, loc2a, loc2b):
    if loc1a == 4 and loc2a == 6:
        if int(loc1a) - int(loc2a) == -2:
            if int(loc1b) - (int(loc2b)) == -2:
                move()
            else:
                print("The knight can't move there!")
        elif int(loc1a) - int(loc2a) == -1:
            if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == 1:
                move()
            else:
                print("The knight can't move there!")
        elif int(loc1a) - int(loc2a) == 1:
            if int(loc1b) - int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 2:
                move()
            else:
                print("The knight can't move there!")
        elif int(loc1a) - int(loc2a) == 2:
            if int(loc1b) - (int(loc2b)) == 0:
                move()
            else:
                print("The knight can't move there!")
        else:
            print("The knight can't move there!")        
    elif loc1a == 6 and loc2a == 4:
        if int(loc1a) - int(loc2a) == -2:
            if int(loc1b) - (int(loc2b)) == 0:
                move()
            else:
                print("The knight can't move there!")
        elif int(loc1a) - int(loc2a) == -1:
            if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 2:
                move()
            else:
                print("The knight can't move there!")
        elif int(loc1a) - int(loc2a) == 1:
            if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == 1:
                move()
            else:
                print("The knight can't move there!")
        elif int(loc1a) - int(loc2a) == 2:
            if int(loc1b) - (int(loc2b)) == -2:
                move()
            else:
                print("The knight can't move there!")
        else:
            print("The knight can't move there!")
    else:
        if int(loc1a) - int(loc2a) == -2:
            if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                move()
            else:
                print("The knight can't move there!")
        elif int(loc1a) - int(loc2a) == -1:
            if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1 or int(loc1b) - (int(loc2b)) == 2:
                move()
            else:
                print("The knight can't move there!")
        elif int(loc1a) - int(loc2a) == 1:
            if int(loc1b) - (int(loc2b)) == -2 or int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1 or int(loc1b) - (int(loc2b)) == 2:
                move()
            else:
                print("The knight can't move there!")
        elif int(loc1a) - int(loc2a) == 2:
            if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                move()
            else:
                print("The knight can't move there!")
        else:
            print("The knight can't move there!")
// Defines the king move //
def kingmove(loc1a, loc1b, loc2a, loc2b):
    if loc1a < 5:
        if int(loc1a) - int(loc2a) == -1:
            if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 0:
                move()
            else:
                print("The king can't move there!")
        if int(loc1a) - int(loc2a) == 0:
            if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                move()
            else:
                print("The king can't move there!")
        if int(loc1a) - int(loc2a) == +1:
            if int(loc1b) - (int(loc2b)) == 0 or int(loc1b) - (int(loc2b)) == 1:
                move()
            else:
                print("The king can't move there!")
    elif loc1a > 5:
        if int(loc1a) - int(loc2a) == -1:
            if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 0:
                move()
            else:
                print("The king can't move there!")
        if int(loc1a) - int(loc2a) == 0:
            if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                move()
            else:
                print("The king can't move there!")
        if int(loc1a) - int(loc2a) == +1:
            if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 0:
                move()
            else:
                print("The king can't move there!")
    else:
        if int(loc1a) - int(loc2a) == -1:
            if int(loc1b) - (int(loc2b)) == 0 or int(loc1b) - (int(loc2b)) == 1:
                move()
            else:
                print("The king can't move there!")
        if int(loc1a) - int(loc2a) == 0:
            if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 1:
                move()
            else:
                print("The king can't move there!")
        if int(loc1a) - int(loc2a) == +1:
            if int(loc1b) - (int(loc2b)) == -1 or int(loc1b) - (int(loc2b)) == 0:
                move()
            else:
                print("The king can't move there!")
// Defines the conditions for queen moves //
def queenmove(loc1a, loc1b, loc2a, loc2b):
    if loc1a == 1:
        if loc2a == loc1a:
            move()
        if loc2a == (loc1a + 1):
            if (loc2b == loc2a) or (loc2b == (loc2a + 1)):
                move()
        if (loc2a > loc1a) and (loc2a < 6):
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
    if loc1a == 2:
        if loc2a == loc1a:
            move()
        if loc2a == (loc1a + 1):
            if (loc2b == loc2a) or (loc2b == (loc2a + 1)):
                move()
        if loc2a == (loc1a - 1):
            if (loc2b == (loc2a - 1)) or (loc2b == loc2a):
                move()
        if loc2a < loc1a:
            if (loc1a - loc2a) == (loc1b - loc2b):
                move()
            if loc1b == loc2b:
                move()
        if (loc2a > loc1a) and (loc2a < 6):
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
    if loc1a == 3:
        if loc2a == loc1a:
            move()
        if loc2a == (loc1a + 1):
            if (loc2b == loc2a) or (loc2b == (loc2a + 1)):
                move()
        if loc2a == (loc1a - 1):
            if (loc2b == (loc2a - 1)) or (loc2b == loc2a):
                move()
        if loc2a < loc1a:
            if (loc1a - loc2a) == (loc1b - loc2b):
                move()
            if loc1b == loc2b:
                move()
        if (loc2a > loc1a) and (loc2a < 6):
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
    if loc1a == 4:
        if loc2a == loc1a:
            move()
        if loc2a == (loc1a + 1):
            if (loc2b == loc2a) or (loc2b == (loc2a + 1)):
                move()
        if loc2a == (loc1a - 1):
            if (loc2b == (loc2a - 1)) or (loc2b == loc2a):
                move()
        if loc2a < loc1a:
            if (loc1a - loc2a) == (loc1b - loc2b):
                move()
            if loc1b == loc2b:
                move()
        if (loc2a > loc1a) and (loc2a < 6):
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
    if loc1a == 5:
        if loc2a == loc1a:
            move()
        if loc2a == (loc1a - 1):
            if (loc2b == (loc2a - 1)) or (loc2b == loc2a):
                move()
        if loc2a == (loc1a + 1):
            if (loc2b == (loc2a - 1)) or (loc2b == loc2a):
                move()
        if loc2a < loc1a:
            if (loc1a - loc2a) == (loc1b - loc2b):
                move()
            if loc1b == loc2b:
                move()
        if loc2a > loc1a:
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
    if loc1a == 6:
        if loc2a == loc1a:
            move()
        if loc2a == (loc1a - 1):
            if (loc2b == loc2a) or (loc2b == (loc2a + 1)):
                move()
        if loc2a == (loc1a + 1):
            if (loc2b == (loc2a - 1)) or (loc2b == loc2a):
                move()
        if loc2a > loc1a:
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
        if (loc2a < loc1a) and (loc2a > 4):
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
    if loc1a == 7:
        if loc2a == loc1a:
            move()
        if loc2a == (loc1a - 1):
            if (loc2b == loc2a) or (loc2b == (loc2a + 1)):
                move()
        if loc2a == (loc1a + 1):
            if (loc2b == (loc2a - 1)) or (loc2b == loc2a):
                move()
        if loc2a > loc1a:
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
        if (loc2a < loc1a) and (loc2a > 4):
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
    if loc1a == 8:
        if loc2a == loc1a:
            move()
        if loc2a == (loc1a - 1):
            if (loc2b == loc2a) or (loc2b == (loc2a + 1)):
                move()
        if loc2a == (loc1a + 1):
            if (loc2b == (loc2a - 1)) or (loc2b == loc2a):
                move()
        if loc2a > loc1a:
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
        if (loc2a < loc1a) and (loc2a > 4):
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
    if loc1a == 9:
        if loc2a == loc1a:
            move()
        if loc2a == (loc1a - 1):
            if (loc2b == loc2a) or (loc2b == (loc2a + 1)):
                move()
        if loc2a == (loc1a + 1):
            if (loc2b == (loc2a - 1)) or (loc2b == loc2a):
                move()
        if (loc2a < loc1a) and (loc2a > 4):
            if (loc2a - loc1a) == (loc2b - loc1b):
                move()
            if loc1b == loc2b:
                move()
    
// Plays through the game //
while True:

    loc1 = str(input("What original location? "))
    loc1 = loc1.split(",")

    if (int(loc1[0])) > 9 or (int(loc1[0])) < 1 or (int(loc1[1])) < 1 or len(rowcolumn[(int(loc1[0])-1)]) < (int(loc1[1])-1):
        print("The coordinate " + str(loc1) + " is off the board!")
        printboard()
    elif rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)] == 0:
        print("There is no piece there!")
        printboard()
    
    else:
        print("There is a " + identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) + " there.")

        loc2 = str(input("What new location? "))
        loc2 = loc2.split(",")
        
        if identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) == "knight":
            knightmove(loc1[0], loc1[1], loc2[0], loc2[1])
        if identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]) == "king":
            kingmove(loc1[0], loc1[1], loc2[0], loc2[1])
        printboard()

        #Hehehehaw
