def cau1(a,b,c):
    if ((a < b + c) & (b < c + a) & (c < a + b)):
        print("Day la ba canh cua tam giac")
        if (a**2 == b**2 + c**2)|(b**2 == c**2 + a**2)|(c**2 == a**2 + b**2):
            if (a == b)|(b == c)|(c==a):
                print ("Day la ba canh cua tam giac vuong can ")
            else:
                print ("Day la ba canh cua tam giac vuong ")
        elif (a == b)|(b == c)|(c==a):
            if (a == b)&(b == c):
                print ("Day la ba canh cua tam giac deu ")
            else:
                print ("Day la ba canh cua tam giac can ")
        else: 
            print ("Day la tam giac thuong ")  
    else:
        print ("Day khong phai la ba canh cua tam giac ")

def cau2(n):
    i=1
    sum=0
    while i<n:
        sum=sum + i
        i+=1
    print(sum)

def cau3(n):
    i=1
    sum=0
    while i<n:
        sum=sum + i**2
        i+=1
    print(sum)

def cau4(n):
    i=1
    sum=0
    while i<=n:
        sum=sum + 1/i
        i+=1
    print(sum)

def cau5(n):
    i=1
    sum=0
    while i<=n:
        sum=sum + 1/(2*i)
        i+=1
    print(sum)

def cau6(n):
    i=1
    sum=0
    while i<=(n+1):
        sum=sum + 1/(2*i - 1)
        i+=1
    print(sum)

def cau7(n,x):
    i=1
    sum=0
    while i<=n:
        sum=sum + 1/(i*x**(i+1))
        i+=1
    print(sum)

def cau8(n):
    i=1
    sum=0
    while i<=n:
        sum=sum + i/(i+1)
        i+=1
    print(sum)

def cau8(n):
    i=1
    sum=0
    while i<=n:
        sum=sum + i/(i+1)
        i+=1
    print(sum)

def cau9(n):
    i=0
    sum=0
    while i<=n:
        sum=sum + (2*i+1)/(2*i+2)
        i+=1
    print(sum)

def cau10(n):
    i=1
    pro=1
    while i<=n:
        pro*=i
        i+=1
    print(pro)

def cau11(n,x):
    i=1
    pro=1
    while i<=n:
        pro*=x
        i+=1
    print(pro)

def cau12(n):
    i=1
    j=1
    sum=0
    pro=1
    for i in range (1,n+1):
        for j in range(1,i+1):
            pro*=j
            print(pro)
            print(" ")

        sum+=pro
    print(sum)


if __name__=="__main__":
    # cau1(99,99,99)
    # cau2(99)
    # cau3(99)
    # cau4(99)
    # cau5(99)
    # cau6(99)
    # cau7(99,99)
    # cau8(99)
    # cau9(99)
    # cau10(99)
    # cau11(99,99)
    cau12(3)
