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

if __name__ == "__main__":
    h = int(input("height: "))
    while h < 20:
        h = int(input("height >= 20: "))
    printA(h)