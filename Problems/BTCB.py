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

def cauvar(n,x):
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
    for i in range (1,n+1):
        pro=1
        for j in range(1,i+1):
            pro*=j
        sum+=pro
    print(sum)

def cau13(x,n):
    a=x
    sum=0
    for i in range(1,n+1):
        x=a**i
        sum+=x
    print(sum)

def cau14(x,n):
    a=x
    sum=0
    for i in range(1,n+1):
        x=a**i
        pro=1
        for j in range(1,i+1):
            pro*=j
        sum+=(x/pro)
    print(sum)

def cau15(x,n):
    a=x
    sum=1
    for i in range(1,2*n+1):
        if i%2==0:
            x=a**i
            pro=1
            for j in range(1,i+1):
                pro*=j
            sum+=(x/pro)
    print(sum)

def cau16(x,n):
    a=x
    sum=1
    for i in range(1,2*n+1):
        if i%2==1:
            x=a**i
            pro=1
            for j in range(1,i+1):
                pro*=j
            sum+=(x/pro)
    print(sum)

def cau17(n):
    count = 1
    res = 2
    while count < n:
        res += res**(1/2)
        count += 1
    print(res)

def cau18(n):
    pow=2
    ans=0
    while pow<n+1 :
        ans=(ans+pow)**(1/pow)
        pow+=1
    print(ans)

def cau19(n):
    pow=2
    ans=0
    while pow<n+1 :
        ans=(ans+pow-1)**(1/pow)
        pow+=1
    print(ans)

def cau20(n):
    pow=2
    ans=0
    while pow<n+1 :
        temp=1
        for i in range(1,pow):
            temp*=i
        ans=(ans+temp)**(1/pow)
        pow+=1
    print(ans)

def cau21(x,n):
    ans=0
    for i in range(1,n+1):
        temp=1
        for _ in range(1,i+1):
            temp*=x
        ans=(ans+temp)**(1/2)
    print(ans)

def cau22(n):
    ans=1
    for _ in range(1,n+1):
        ans=1/(1+ans)
    print(ans)

def cau23(x,n):
    sum=0
    for i in range(1,n+1):
        sum+=((-1)**(i+1))*(x**i)
    print(sum)

def cau24(x,n):
    sum=0
    for i in range(1,n+1):
        sum+=((-1)**(i))*x**(2*i)
    print(sum)

def cau25(x,n):
    sum=0
    for i in range(1,n+1):
        sum+=((-1)**(i))*x**(2*i+1)
    print(sum)

def cau26(n):
    sum=0
    for i in range (1,n+1):
        temp=0
        for j in range(1,i+1):
            temp+=j
        sum+=(-1)**(i)*1/(temp)
    print(sum)

def cau27(x,n):
    sum=0
    for i in range(1,n+1):
        fac=1
        for j in range(1,i+1):
            fac*=j
        sum+=((-1)**(i))*(x**i)/fac
    print(sum)
        
def cau28(n):
    k=int((-1 + (1 + 8 * n)**(1/2)) / 2)
    print(k)

def cau29(a,b,c):
    max=max(a, b, c)
    min=min(a, b, c)
    print(max)
    print(min)

def cau30(a,b):
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        print("2 so cung dau")
    else:
        print("2 so khac dau") 

def cau31(a,b):
    while b:
        a, b = b, a % b
    print(a)

def cau32(a,b):
    x=a*b
    while b:
        a, b = b, a % b
    print(x/a)

def cau33(a,b):
    for i in range(a,b+1):
        if isinstance(i**(1/2)):
            print(i, end=" ")

if __name__=="__main__":
    var=int(input())
    var_1=int(input())
    var_2=int(input())
    # cau1(var,var_1,var_2)
    # cau2(var)
    # cau3(var)
    # cau4(var)
    # cau5(var)
    # cau6(var)
    # cau7(var,var_1)
    # cau8(var)
    # cau9(var)
    # cau10(var)
    # cauvar(var,var_1)
    # cau12(var)
    # cau13(var,var_1)
    # cau15(var,var_1)
    # cau16(var,var_1)
    # cau17(var)
    # cau18(var)
    # cau19(var)
    # cau20(var)
    # cau21(var,var_1)
    # cau22(var)
    # cau23(var,var_1)
    # cau24(var,var_1)
    # cau25(var,var_1)
    # cau26(var)
    # cau27(var,var_1)
    # cau28(var)
    # cau29(var,var_1,var_2)
    # cau30(var,var_1)
    # cau31(var,var_1)
    # cau32(var,var_1)
    # cau33(var,var_1)