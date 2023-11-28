import sys

def UCLN(a,b):
    arr = []
    for i in range(1 , max(a,b)):
        if a%i == 0 and b%i == 0:
            arr.append(i)
    return arr[-1]

def get_0_sys():
    while True:
        try:
            a = int(input("nhap so a: "))
            if a <= 0:
                continue
            valid = True
            break
        except ValueError:
            valid = False
            return None , None, valid
    while valid:
        try:
            b = int(input("nhap so b: "))
            if b <= 0:
                continue
            break
        except ValueError:
            valid = False
            return a , None, valid
    return a , b, valid
 
def get_sys():
    while True:
        try:
            a = int(input("nhap so a: "))
            if a <= 0:
                continue
            break
        except ValueError:
            print("Error")
            sys.exit()
    while True:
        try:
            b = int(input("nhap so b: "))
            if b <= 0:
                continue
            break
        except ValueError:
            print("Error")
            sys.exit()

        
    return a , b

def BONUS_2_0_sys():
    x,y,valid = get_0_sys()
    if valid:
        print(UCLN(x,y))
    else:
        print("Error")
       
def BONUS_2_sys():
    x,y = get_sys()
    print(UCLN(x,y))

if __name__=="__main__":
    # BONUS_2_0_sys()
    BONUS_2_sys()
