def printA(h):
    w = 2 * h - 1
    for i in range(h):
        for j in range(w):
            if (i == h // 2) or (i + j == h - 1) or (j - i == h - 1):
                print('*', end="")
            elif (i == (h // 2)-1) or (i + j == h) or (j - i == h - 2):
                print('*', end="")
            else:
                print(' ', end="")
        print()
def printAA():
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

if __name__ == "__main__":
    # h = int(input("height: "))
    # while h < 20:
    #     h = int(input("height >= 20: "))
    # printA(h)
    printAA()