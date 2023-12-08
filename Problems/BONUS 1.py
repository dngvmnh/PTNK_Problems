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

def printR():
    print("R"*25)
    for i in range(5):
        print("R" + ":"*5 + "R" + " "*11 + "R" + ":"*5 + "R")
    print("R" + ":"*5 + "R" + " "*3 + " " + " "*3 + "R" + ":"*5 + "R")
    for i in range(7):
        print("R" + ":"*5 + "R" + " "*(2*i+1) + "R" + ":"*5 + "R")
    print("R"*7+" "*13+"R"*7)
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
    # printI()
    # printJ()
    # printK()
    # printL()
    # printM()
    # printN()
    # printO()
    # printP()
    # printQ()
    printR()
    # printS()
    # printT()
    # printU()
    # printV()
    # printW()
    # printX()
    # printY()
    # printZ()