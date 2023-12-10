def printA():
    print(" "*15 + "A"*3 + " "*15)
    for i in range(4):
        print(" "*(14-i)+ "A" + ":"*(3+2*i)+ "A"+" "*(14-i))
    print(" "*10 + "A" + ":"*5 + "A" + ":"*5 + "A" + " "*10)
    for i in range(3):
        print(" "*(9-i)+ "A" + ":"*5 + "A" + " "*(1+2*i) + "A" + ":"*5 + "A" + " "*(9-i))
    print(" "*6 +"A" + ":"*5 + "A"*9 + ":"*5 + "A" + " "*6)
    print(" "*5 +"A" + ":"*21 + "A" + " "*6)
    print(" "*4 +"A" + ":"*5 + "A"*13 + ":"*5 + "A" + " "*4)
    for i in range(3):
        print(" "*(3-i)+ "A" + ":"*5 + "A" + " "*(13+2*i) + "A" + ":"*5 + "A" + " "*(3-i))
    print("A"*7+ " "*19 +"A"*7)
    print("\n")

def printB():
    print("B"*23)
    print("B" + ":"*5 + ":"*12 + ":"*5 + "B")
    print("B" + ":"*5 + "B"*12 + ":"*6 + "B")
    for i in range(4):
        print("B" + ":"*5 + "B" + " "*11 + "B" + ":"*5 + "B")
    print("B" + ":"*5 + "B"*12 + ":"*5 + "B")
    print("B" + ":"*5 + ":"*11 + ":"*5 + "B")
    print("B" + ":"*5 + "B"*12 + ":"*5 + "B")
    for i in range(4):
        print("B" + ":"*5 + "B" + " "*11 + "B" + ":"*5 + "B")
    print("B" + ":"*5 + "B"*12 + ":"*6 + "B")
    print("B" + ":"*5 + ":"*12 + ":"*5 + "B")
    print("B"*23)
    print("\n")

def printC():
    print(" "*8+"C"*13)
    print(" "*5+"C"*3+":"*13+"C"*3)
    print(" "*2+"C"*3+":"*19+"C"*3)
    print(" "+"C"+":"*5+"C"*15+":"*5+"C")
    for i in range(2):
        print("C"+":"*5+"C"+" "*15+"C"+":"*5+"C")
    print("C"+":"*5+"C"+" "*15+"C"+"C"*5+"C")
    for i in range(4):
        print("C"+":"*5+"C")
    print("C"+":"*5+"C"+" "*15+"C"+"C"*5+"C")
    for i in range(2):
        print("C"+":"*5+"C"+" "*15+"C"+":"*5+"C")
    print(" "+"C"+":"*5+"C"*15+":"*5+"C")
    print(" "*2+"C"*3+":"*19+"C"*3)
    print(" "*5+"C"*3+":"*13+"C"*3)
    print(" "*8+"C"*13)
    print("\n")

def printD():
    print("D"*23)
    print("D" + ":"*5 + ":"*12 + ":"*5 + "D")
    print("D" + ":"*5 + "D"*12 + ":"*6 + "D")
    for i in range(10):
        print("D" + ":"*5 + "D" + " " * 12 + "D" + ":"*5 + "D")
    print("D" + ":"*5 + "D"*12 + ":"*6 + "D")
    print("D" + ":"*5 + ":"*12 + ":"*5 + "D")
    print("D"*23)
    print("\n")

def printE():
    print("E"*23)
    print("E" + ":"*6+":"*9+":"*6+"E")
    print("E" + ":"*5 + "E"+"E"*9+"E"+ "E"*5+"E")
    for i in range(4):
        print("E" + ":"*5 + "E")
    print("E" + ":"*5 + "E"+"E"*9+"E"+ "E"*5+"E")
    print("E" + ":"*6+":"*9+":"*6+"E")
    print("E" + ":"*5 + "E"+"E"*9+"E"+ "E"*5+"E")
    for i in range(4):
        print("E" + ":"*5 + "E")
    print("E" + ":"*5 + "E"+"E"*9+"E"+ "E"*5+"E")
    print("E" + ":"*6+":"*9+":"*6+"E")
    print("E"*23)
    print("\n")

def printF():
    print("F"*23)
    print("F" + ":"*6 + ":"*9 + ":"*6 + "F")
    print("F" + ":"*5 + "F" + "F"*9 + "F" + "F"*5 + "F")
    for i in range(4):
        print("F" + ":"*5 + "F")
    print("F" + ":"*5 + "F" + "F"*9 + "F" + "F"*5 + "F")
    print("F" + ":"*6 + ":"*9 + ":"*6 + "F")
    print("F" + ":"*5 + "F" + "F"*9 + "F" + "F"*5 + "F")
    for i in range(6):
        print("F" + ":"*5 + "F")
    print("F" + "F"*5 + "F")
    print("\n")

def printG():
    print(" "*8+"G"*13)
    print(" "*5+"G"*3+":"*13+"G"*3)
    print(" "*2+"G"*3+":"*19+"G"*3)
    print(" "+"G"+":"*5+"G"*15+":"*5+"G")
    for i in range(2):
        print("G"+":"*5+"G"+" "*15+"G"+":"*5+"G")
    print("G"+":"*5+"G"+" "*15+"G"+"G"*5+"G")
    for i in range(3):
        print("G"+":"*5+"G"+" "*7)
    print("G"+":"*5+"G"+" "*15+"G"+"G"*5+"G")
    for i in range(2):
        print("G"+":"*5+"G"+" "*12+"G"*2+":"*9+"G"*2)
    print("G"+":"*5+"G"+" "*15+"G"+":"*5+"G")
    print(" "+"G"+":"*5+"G"*15+":"*6+"G")
    print(" "*2+"G"*3+":"*23+"G")
    print(" "*5+"G"*3+":"*13+"G"*2+":"*5+"G")
    print(" "*8+"G"*13+" "+"G"*7)
    print("\n")
    
def printH():
    print("H"*7+" "*12+"H"*7)
    for i in range(6):
        print("H"+":"*5+"H"+" "*12+"H"+":"*5+"H")
    print("H"+":"*5+"H"+"H"*12+"H"+":"*5+"H")
    print("H"+":"*5+":"+":"*12+":"+":"*5+"H")
    print("H"+":"*5+"H"+"H"*12+"H"+":"*5+"H")
    for i in range(6):
        print("H"+":"*5+"H"+" "*12+"H"+":"*5+"H")
    print("H"*7+" "*12+"H"*7)
    print("\n")

def printI():
    print("I"*22)
    print("I" + ":"*6 + ":"*8 + ":"*6 + "I")
    print("I"*8 + ":"*5 + "I" + "I"*8)
    for i in range(8):
        print(" "*8+"I" + ":"*5 + "I")
    print("I"*8 + ":"*5 + "I" + "I"*8)
    print("I" + ":"*6 + ":"*8 + ":"*6 + "I")
    print("I"*22)
    print("\n")

def printJ():
    print("J"*22)
    print("J" + ":"*6 + ":"*8 + ":"*6 + "J")
    print("J"*8 + ":"*5 + "J" + "J"*8)
    for i in range(8):
        print(" "*8+"J" + ":"*5 + "J")
    print("J"*8 + ":"*5 + "J")
    print("J" + ":"*6 + ":"*5 +"J")
    print("J"*12)
    print("\n")

def printK():
    print("K"*7+" "*13+"K"*7)
    for i in range(6,0,-1):
        print("K" + ":"*5 + "K" + " "*(2*i+1) + "K" + ":"*5 + "K")
    print("K" + ":"*5 + "K" + " " + "K" + ":"*5 + "K")
    for i in range(7):
        print("K" + ":"*5 + "K" + " "*(2*i+1) + "K" + ":"*5 + "K")
    print("K"*7+" "*13+"K"*7)
    print("\n")

def printL():
    print("L"*7)
    for i in range(10):
        print("L" + ":"*5 + "L")
    print("L" + ":"*5 + "L" + "L"*9 + "L" + "L"*5 + "L")
    print("L" + ":"*6 + ":"*9 + ":"*6 + "L")
    print("L" + "L"*5 + "L" + "L"*9 + "L" + "L"*5 + "L")
    print("\n")

def printM():
    print("M"*7+" "*15+"M"*7)
    for i in range(6):
        print("M"+":"*(5+i)+"M"+" "*(15-2*i)+"M"+":"*(5+i)+"M")
    print("M"+":"*(5)+"M"+":"*5+"M"*4+" "*(15-2*8)+"M"+":"*5+"M"+":"*5+"M")
    for i in range(2,7):
        print("M"+":"*5+"M"+" "*(i-2)+"M"+":"*(17-2*i)+"M"+" "*(i-2)+"M"+":"*5+"M")
    print("M"+"M"*(5)+"M"+" "*5+"M"*4+" "*(15-2*8)+"M"+" "*5+"M"+"M"*5+"M")
    print("\n")

def printN():
    print("N"*7+" "*15+"N"*7)
    for i in range(7):
        print("N"+":"*(5+i)+"N"+" "*(15-i)+"N"+":"*5+"N")
    for i in range(9):
        print("N"+":"*(5)+"N"+" "*i+"N"+":"*5+"N"+" "*(8-i)+"N"+":"*5+"N")
    print("N"*7+" "*8+"N"*14)
    print("\n")

def printO():
    print(" "*12+"O"*5)
    for i in range(2):
        print(" "*(10-2*i)+"O"*2+":"*(5+4*i)+"O"*2)
    print(" "*(10-2*2)+"O"*2+":"*5+"O"*3+":"*5+"O"*2)
    for i in range(3):
        print(" "*(4-2*i)+"O"*2+":"*(5)+"O"*2+" "*(3+i*4)+"O"*2+":"*(5)+"O"*2)
    for i in range(2):
        print("O"*2+":"*5+"O"*2+" "*11+"O"*2+":"*5+"O"*2)
    for i in range(3):
        print(" "*(2*i)+"O"*2+":"*(5)+"O"*2+" "*(11-i*4)+"O"*2+":"*(5)+"O"*2)
    print(" "*(10-2*2)+"O"*2+":"*5+"O"*3+":"*5+"O"*2)
    for i in range(2):
        print(" "*(8+2*i)+"O"*2+":"*(9-4*i)+"O"*2)
    print(" "*12+"O"*5)
    print("\n")

def printP():
    print("P"*23)
    print("P"+":"*21+"P")
    print("P"+":"*5+"P"+"P"*9+"P"+":"*5+"P")
    for i in range(2):
        print("P" + ":"*5 + "P" + " "*(9) + "P" + ":"*5 + "P")
    for i in range(5):
        print("P" + ":"*5 + "P" + " "*(9-2*i) + "P" + ":"*5 + "P")
    for i in range(3):
        print("P"+":"*(10-2*i)+"P")
    for i in range(5):
        print("P"+":"*5+"P")
    print("P"*7)
    print("\n")

def printQ():
    print(" "*12+"Q"*5)
    for i in range(2):
        print(" "*(10-2*i)+"Q"*2+":"*(5+4*i)+"Q"*2)
    print(" "*(10-2*2)+"Q"*2+":"*5+"Q"*3+":"*5+"Q"*2)
    for i in range(3):
        print(" "*(4-2*i)+"Q"*2+":"*(5)+"Q"*2+" "*(3+i*4)+"Q"*2+":"*(5)+"Q"*2)
    for i in range(2):
        print("Q"*2+":"*5+"Q"*2+" "*11+"Q"*2+":"*5+"Q"*2)
    for i in range(3):
        print(" "*(2*i)+"Q"*2+":"*(5)+"Q"*2+" "*(11-i*4)+"Q"*2+":"*(5)+"Q"*2)
    print(" "*(10-2*2)+"Q"*2+":"*5+"Q"*3+":"*5+"Q"*2+":"*2+"Q"*2)
    for i in range(2):
        print(" "*(8+2*i)+"Q"*2+":"*(9-4*i)+"Q"*2+" "*2*(2*i+1)+"Q"*2+":"*2+"Q"*2)
    print(" "*12+"Q"*5+" "*10+"Q"*6)
    print("\n")


def printR():
    print("R"*25)
    print("R"+":"*23+"R")
    print("R"+":"*5+"R"+"R"*11+"R"+":"*5+"R")
    for i in range(5):
        print("R" + ":"*5 + "R" + " "*11 + "R" + ":"*5 + "R")
    print("R" + ":"*5 + "R" + " "*3 + " " + " "*3 + "R" + ":"*5 + "R")
    for i in range(7):
        print("R" + ":"*5 + "R" + " "*(2*i+1) + "R" + ":"*5 + "R")
    print("R"*7+" "*13+"R"*7)
    print("\n")
    
def printS():
    print(" "*7+"S"*9)
    print(" "*4+"S"*3+":"*9+"S"*3)
    print(" "+"S"*3+":"*15+"S"*3)
    print("S"+":"*6+"S"+"S"*7+"S"+":"*6+"S")
    for i in range(2):
        print("S"+":"*5+"S"+" "*9+"S"+":"*5+"S")
    print("S"+":"*5+"S"+" "*9+"S"+"S"*5+"S")
    for i in range(9):
        print(" "*(2*i)+"S"+":"*5+"S")
    print("S"+"S"*5+"S"+" "*9+"S"+":"*5+"S")
    for i in range(2):
        print("S"+":"*5+"S"+" "*9+"S"+":"*5+"S")
    print("S"+":"*6+"S"+"S"*7+"S"+":"*6+"S")
    print(" "+"S"*3+":"*15+"S"*3)
    print(" "*4+"S"*3+":"*9+"S"*3)
    print(" "*7+"S"*9)
    print("\n")

def printT():
    print("T"*24)
    print("T"+":"*22+"T")
    print("T"*9+":"*6+"T"*9)
    for i in range(10):
        print(" "*8 + "T" + ":"*6 + "T")
    print(" "*8+"T"*8)
    print("\n")


def printU():
    print("U"*7 + " " *12 + "U"*7)
    for i in range(10):
        print("U" + ":"*5 + "U" + " " * 12 + "U" + ":"*5 + "U")
    print("U" + ":"*5 + "U" + "U" * 12 + "U" + ":"*5 + "U")
    print("U" + ":"*5 + "U" + ":" * 12 + "U" + ":"*5 + "U")
    print("U" + "U"*5 + "U" + "U" * 12 + "U" + "U"*5 + "U")
    print("\n")

def printV():
    print("V"*7+" "*16+"V"*7)
    for i in range (9):
        print(" "*i+"V"+":"*5+"V"+" "*(16-i*2)+"V"+":"*5+"V")
    for i in range(4):
        print(" "*(9+i)+"V"+":"*(10-2*i)+"V")
    print(" "*12+"V"*6)
    print("\n")

def printW():
    print("W"*7 + " " * 10 + "W"*14+ " " * 10 + "W"*7)
    for i in range(6):
        print(" "*i+ "W" + ":"*5 + "W" + " " * (10-2*i) + "W" + ":"*5 + "W"+" "*2*i+ "W" + ":"*5 + "W" + " " * (10-2*i) + "W" + ":"*5 + "W")
    print(" "*5+"W"*14+" "*10+"W"*14)
    print("\n")

def printX():
    print("X"*7 + " " * 10 + "X"*7)
    for i in range(6):
        print(" "*i+ "X" + ":"*5 + "X" + " " * (10-2*i) + "X" + ":"*5 + "X")
    for i in range(5):
        print(" "*(5-i)+"X"+":"*5+"X"+" "*2*i+"X"+":"*5+"X")
    print("X"*7 + " " * 10 + "X"*7)
    print("\n")

def printY():
    print("Y"*7 + " " * 16 + "Y"*7)
    for i in range (9):
        print(" "*i + "Y" + ":"*5 + "Y" + " " * (16-i*2) + "Y" + ":"*5 + "Y")
    for i in range(4):
        print(" "*(9+i)+"Y"+":"*(10-2*i)+"Y")
    for i in range(6):
        print(" "*12+"Y"+":"*4+"Y")
    print(" "*12+"Y"*6)
    print("\n")

def printZ():
    print("Z"*30)
    print("Z"+":"*28+"Z")
    print("Z"+":"*5+"Z"*24)
    for i in range(12):
        print(" "*(i*2)+"Z"+":"*5+"Z")
    print("Z"+"Z"*5+"Z"*18+":"*5+"Z")
    print("Z"+":"*28+"Z")
    print("Z"*30)
    print("\n")

if __name__ == "__main__":
    printA()
    printB()
    printC()
    printD()
    printE()
    printF()
    printG()
    printH()
    printI()
    printJ()
    printK()
    printL()
    printM()
    printN()
    printO()
    printP()
    printQ()
    printR()
    printS()
    printT()
    printU()
    printV()
    printW()
    printX()
    printY()
    printZ()