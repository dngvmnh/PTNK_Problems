def caua():
    a = int(input("so hang: "))
    b = int(input("so cot: "))
    n = 0
    for _ in range(a):
        if n%2 == 0:
            t = 0
            while t < b:
                    print("*", end = "")
                    t += 1
                    if t >= b: 
                        break
                    print(".", end = "")
                    t += 1
        else:
            t = 0
            while t < b:
                    print(".", end = "")
                    t += 1
                    if t >= b: 
                        break
                    print("*", end = "")
                    t += 1
        print("\n")
        n += 1
def caub():
    a = int(input("so hang: "))
    b = int(input("so cot: "))
    print("*"*b+"\n")
    for _ in range(a-2):
        print("*", end = "")
        for _ in range(b-2):
            print(".", end = "")
        print("*", end = "")
        print("\n")
    print("*"*b+"\n")
def cauc():
    a = int(input("so hang: "))
    b = int(input("so cot: "))

    for _ in range(a):
        print("*"*(b*3+1) +"\n")
        
        for _ in range(2):
            print("*", end = "")
            for _ in range(b):
                print("..*", end = "")
            print("\n")
    print("*"*(b*3+1))
def caud():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))
    for _ in range(a):
        print("*"*(b*(d+1)+1) +"\n")
        for _ in range(c):
            print("*", end = "")
            for _ in range(b):
                print("."*d + "*", end = "")
            print("\n")
    print("*"*(b*(d+1)+1))
if __name__=="__main__":
    # caua()
    # caub()
    cauc()
    # caud()