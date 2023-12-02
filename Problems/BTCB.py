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
        print("2 n cung dau")
    else:
        print("2 n khac dau") 

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

def cau34(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    print(sum)

def cau35(n):
    pro = 0
    for i in range(1, n + 1):
        if n % i == 0:
            pro *= i
    print(pro)

def cau36(n):
    count = 0
    div = []
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            div.append(i)
    print(count)
    for i in div:
        print(i, end=" ")

def cau37(n):
    count = 0
    div = []
    for i in range(1, n + 1):
        if n % i == 0 & i%2==1:
            count += 1
            div.append(i)
    print(count)
    for i in div:
        print(i, end=" ")

def cau38(n):
    count = 0
    div = []
    for i in range(1, n + 1):
        if n % i == 0 & i%2==0:
            count += 1
            div.append(i)
    print(count)
    for i in div:
        print(i, end=" ")

def cau39(n):
    count = 0
    pro=1
    for i in range(1, n + 1):
        if n % i == 0 & i%2==1:
            count += 1
            pro*=i
    print(count)
    print(pro)

def cau40(n):
    count = 0
    div = []
    for i in range(1, n + 1):
        if n % i == 0 & i%2==0:
            count += 1
            div.append(i)
    print(count)
    for i in div:
        print(i, end=" ")

def cau41(n):
    max = 1
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0 and i > max:
            max = i
    print(max)

def cau42(n):
    max=0
    for x in range(n-1, 1, -1):
        if n % x == 0:
            max=x
    if max==n or max==1:
        return -1
    else:
        print(max)

def cau43(a, b):
    for x in range(a, b + 1):
        if x % 2 == 0:
            print(x, end=" ")

def cau44(a,b,c):
    for x in range(a, b + 1):
        if c % x == 0:
            print(x, end=" ")

def cau45(a,b,c):
    for x in range(a, b + 1):
        if c % x == 0 and x%2==0:
            print(x, end=" ")

def cau46(a,b,c):
    count=0
    for x in range(a, b + 1):
        if c % x == 0 and x%2==0:
            count+=1
    print(count)
 
def cau47(h):
    w=h
    for i in range(h):
        print(" " * (h - i - 1) + "*" * (2 * i + 1))
    print("\n")

    for i in range(h):
        if i==0:
            print(" " * (h - i - 1) + "*" + " " * (2 * i - 1))
        elif i==h-1:
            print("*" * (h - i - 1) + "*" + "*" * (2 * i ))
        else:
            print(" " * (h - i - 1) + "*" + " " * (2 * i - 1) + "*")
    print("\n")

    for i in range(h):
        print("* " * (i + 1))
    print("\n")

    for i in range(h):
        if i == 0 or i == h - 1:
            print("* " * (i + 1))
        else:
            print("* " + "  " * (i - 1) + "* ")

def cau48(m,n):
    for _ in range(m):
        for _ in range(n-1):
            print("*",  end="")
        print("*")
    print("\n")

    print("*"*m)
    for _ in range(m-2):
        print("*", end="")
        for _ in range(n-2):
            print(" ",  end="")
        print("*")
    print("*"*m)
    print("\n")

def cau49(n):
    count = 0
    div = []
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            div.append(i)
    for i in div:
        print(i, end=" ")

def cau50(n):
    count = 0
    div = []
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            div.append(i)
    print(count)

def cau51(n):
    for i in range(2,n-1):
        if n%i==0:
            print("n khong la n nguyen to")
            return
    print("n la n nguyen to")
    return

def cau52(n):
    valid=1
    prime=False
    for k in range(n+1):
        for i in range(2,k-1):
            if k%i==0:
                prime=True
                break
            if k>valid:
                valid=k
    print(valid)
def cau53(n):
    valid=2
    k=2
    while True:
        prime=True
        for i in range(2,k-1):
            if k%i==0:
                prime=False
        if prime==True:
            valid=k
            if valid>n:
                print(k)
                break
        k+=1
    
def cau54(a,b):
    for i in range (a,b+1):
        prime=True
        for j in range(2,i-1):
            if i%j==0:
                prime=False
        if prime:
            print(i)

def cau55(n):
    a=int(n**(1/2))
    if a**2==n:
        print("n là n chinh phuong")
    else:
        print("n khong phai n chinh phuong")

def cau56(n):
    arr=[int(x) for x in str(n)]
    print(len(arr)-1)

def cau57(n):
    arr=[int(x) for x in str(n)]
    sum=0
    pro=1
    for i in arr:
        sum+=i
    print(sum)
    for i in arr:
        if i!=0:
            pro*=i
    print(pro)

def cau58(n):
    arr=[int(x) for x in str(n)]
    even=0
    odd=0
    for i in arr:
        if i!=0 and i%2==0:
            even+=1
    for i in arr:
        if i!=0 and i%2==1:
            odd+=1
    print(even)
    print(odd)

def cau59(n):
    arr=[int(x) for x in str(n)]
    even_sum=0
    odd_pro=1
    for i in arr:
        if i!=0 and i%2==0:
            even_sum+=i
    for i in arr:
        if i!=0 and i%2==1:
            odd_pro*=i
    print(even_sum)
    print(odd_pro)

def cau60(n):
    arr=[int(x) for x in str(n)]
    max=0
    for i in arr:
        if i!=0 and i>max:
            max=i
    print(max)

def cau61(n):
    arr=[int(x) for x in str(n)]
    max=0
    sum=0
    for i in arr:
        if i!=0 and i>max:
            max=i
    for i in arr:
        if i!=max:
            sum+=i
    print(sum)
    
def cau62(n):
    arr=[int(x) for x in str(n)]
    print(arr[-2])

def cau63(n):
    arr=[int(x) for x in str(n)]
    for _ in arr:
        count+=1
    if count%2==0:
        print(arr[int(count/2)])
    if count%2==1:
        print(arr[int((count-1)/2)])

def cau64(n,k):
    arr=[int(x) for x in str(n)]
    for i in arr:
        if i%k==0:
            print(i)
            break

def cau65(n,k):
    arr=[int(x) for x in str(n)]
    for i in arr:
        if i%k==0:
            print(i)
            break

def cau66(n):
    arr=[int(x) for x in str(n)]
    for i in arr:
        print(round(i), end="")

def cau67(n):
    arr=[int(x) for x in str(n)]
    num=0
    pow=1

    for i in arr:
        num+=i*10**pow
        pow+=1
    print(n+num)

def cau68a(n):
    arr=[int(x) for x in str(n)]
    max=0
    for i in arr:
        if i!=0 and i>max:
            max=i
    print(max)

def cau68b(n):
    arr=[int(x) for x in str(n)]
    min=9
    for i in arr:
        if i!=0 and i<min:
            min=i
    print(min)

def cau68c(n):
    cau68a(n)
    cau68b(n)

def cau68d(n):
    arr=[int(x) for x in str(n)]
    max=0
    count=0
    for i in arr:
        if i!=0 and i>max:
            max=i
    for i in arr:
        if i==max:
            count+=1

def cau68e(n):
    arr=[int(x) for x in str(n)]
    min=9
    count=0
    for i in arr:
        if i!=0 and i<min:
            min=i
    for i in arr:
        if i==min:
            count+=1

def cau68f(n):
    cau68d(n)
    cau68e(n)

def cau68g(n):
    cau68c(n)
    cau68f(n)

def cau69(n):
    arr=[int(x) for x in str(n)]
    arr.reverse()
    valid=False
    for i in arr:
        if i%2==0:
            print("n co n chan")
            break
        else:
            valid=True
    if valid:
        print("n toan n le")

def cau70(n):
    arr=[int(x) for x in str(n)]
    arr.reverse()
    valid=False
    for i in arr:
        if i%2==1:
            print("n co n le")
            break
        else:
            valid=True
    if valid:
        print("n toan n chan")

def cau71(n,k):
    arr=[int(x) for x in str(n)]
    for i in range(int(len(arr)-1)):
        a=arr[i]*10+arr[i+1]
        if a%k==0:
            print(arr[i], arr[i+1])

def cau72(n):
    m=n
    arr=[int(x) for x in str(n)]
    num=0
    pow=1
    for i in arr:
        num+=i*10**pow
        pow+=1
    num=num/10
    if(m-num==0):
        print("n la n doi xung")
    else:
        print("n khong phai n doi xung")

def cau73(n):
    arr=[int(x) for x in str(n)]
    for i in range(int(len(arr)-1)):
        if arr[i] <= arr[i+1]:
            valid=True
        else:
            valid=False
            break
    if valid:
        print("chu n cua n tang dan")
    else:
        print("chu n cua n khong tang dan")

def cau74(a,b):
    if a == 0:
        if b == 0:
            print("phuong trinh vo n nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        x = -b / a
        print(f"phuong trinh co nghiem x = {x}")

def cau75(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("phuong trinh co 2 nghiem x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"phuong trinh co nghiem kep x = {x}")
    else:
        print(f"phuong trinh vo nghiem")

def cau76(a,b,c,d,e,f):
    mtx = a * e - b * d
    if mtx == 0:
        if a * f - c * d == 0 and b * f - c * e == 0:
            print("he co vo n nghiem")
        else:
            print("he khong co nghiem")
    else:
        x = (c * e - b * f) / mtx
        y = (a * f - c * d) / mtx
        print(f"he co nghiem x = {x}, y = {y}")

def cau77(n):
    if n <= 0 or n%2!= 0:
        print("no nlution")
        return
    k = 0
    no_nl=False
    while n > 1:
        n /= 2
        if n-int(n)==0:
            k += 1
        else:
            print("no nlution")
            no_nl=True
            break
    if not no_nl:
        print(k)

def cau78(n):
    if n <= 0 or n%3!= 0:
        print("no nlution")
        return
    k = 0
    no_nl=False
    while n > 1:
        n /= 3
        if n-int(n)==0:
            k += 1
        else:
            print("no nlution")
            no_nl=True
            break
    if  not no_nl:
        print(k)

def cau79(n):
    not_found=True
    while not_found:
        a=n
        if n <= 0 or n%2!= 0:
            not_found=True
        k = 0
        no_nl=False
        while n > 1:
            n /= 2
            if n-int(n)==0:
                k += 1
            else:
                no_nl=True
                not_found=True
        if not no_nl:
            not_found=False
            print(2**k)
        n=a-1

def cau80(n):
    not_found=True
    while not_found:
        a=n
        if n <= 0 or n%3!= 0:
            not_found=True
        k = 0
        no_nl=False
        while n > 1:
            n /= 3
            if n-int(n)==0:
                k += 1
            else:
                no_nl=True
                not_found=True
        if not no_nl:
            not_found=False
            print(3**k)
        n=a+1
        
def cau81():
    n=0
    while n <= 10**7:
        arr=[]
        sum=0
        for i in range(1,n):
            if n%i==0:
                arr.append(i)
        for i in arr:
            sum+=i
        if n==sum:
            print(n)
        n+=1

def cau82(n):
    arr=[]
    sum=0
    for i in range(1,n):
        if n%i==0:
            arr.append(i)
    for i in arr:
        sum+=i
    if n==sum:
        print("n la n hoan thien")
    else:
        print("n khong phai n hoan thien")

def cau83(n):
    can=["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quí"]
    chi=["Tí", "Sửu", "Dần", "Mẹo", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", 'Dậu', "Tuất", "Hợi"]
    can_index = (n - 1) % 10
    chi_index = (n - 1) % 12
    print(f"{can[can_index]} {chi[chi_index]}")
 
def cau84(a,b,c):
    leap=(c%4==0 and c%100!=0) or (c%400==0)
    print(f"{'nam nhuan' if leap else 'khong phai nam nhuan'}")

    if b in [1, 3, 5, 7, 8, 10, 12]:
        print("31")
        n=31
    elif b in [4, 6, 9, 11]:
        print("30")
        n=30
    elif b == 2:
        print(f"{29 if leap else 28}")
        if leap:
            n=29
        else:
            n=28
    else:
        return

    if a<n:
        print(a+1, b, c)
    elif b<12:
        print(1, b+1, c)
    else:
        print(1, 1, c+1)

    if a > 1:
        print( a - 1, b, c )
    elif b > 1:
        print( n-1, b - 1, c )
    else:
        print( 31, 12, c - 1 )

    total = a

    for i in range(1, b):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            m=31
        elif i in [4, 6, 9, 11]:
            m=30
        elif i==2:
            if leap:
                m=29
            else: 
                m=28
        total += m

    print( total )

def cau85(n,k):
    count=0
    arr=[int(x) for x in str(n)]
    arr.reversed()
    for i in arr:
        if i%k==0:
            count+=1
    print(count)

def cau86(n):
    if 10 <= n <= 99:
        n_chuc = n // 10
        n_don_vi = n % 10
        chuc = {
            0: "",
            1: "Mười",
            2: "Hai Mươi",
            3: "Ba Mươi",
            4: "Bốn Mươi",
            5: "Năm Mươi",
            6: "Sáu Mươi",
            7: "Bảy Mươi",
            8: "Tám Mươi",
            9: "Chín Mươi",
        }
        don_vi = {
            0: "",
            1: "Một",
            2: "Hai",
            3: "Ba",
            4: "Bốn",
            5: "Năm",
            6: "Sáu",
            7: "Bảy",
            8: "Tám",
            9: "Chín",
        }   
        print(f"{chuc[n_chuc]} {don_vi[n_don_vi]}")

def cau87(n):
    if 0 <= n <= 99999:
        chuc_nghin = {
            0: "",
            1: "Mười",
            2: "Hai Mươi",
            3: "Ba Mươi",
            4: "Bốn Mươi",
            5: "Năm Mươi",
            6: "Sáu Mươi",
            7: "Bảy Mươi",
            8: "Tám Mươi",
            9: "Chín Mươi",
        }
        nghin = {
            0: "Nghìn",
            1: "Một Nghìn",
            2: "Hai Nghìn",
            3: "Ba Nghìn",
            4: "Bốn Nghìn",
            5: "Năm Nghìn",
            6: "Sáu Nghìn",
            7: "Bảy Nghìn",
            8: "Tám Nghìn",
            9: "Chín Nghìn",
            10: "Mười Nghìn"
        }

        tram = {
            0: "",
            1: "Một Trăm",
            2: "Hai Trăm",
            3: "Ba Trăm",
            4: "Bốn Trăm",
            5: "Năm Trăm",
            6: "Sáu Trăm",
            7: "Bảy Trăm",
            8: "Tám Trăm",
            9: "Chín Trăm",
        }

        chuc = {
            0: "",
            1: "Mười",
            2: "Hai Mươi",
            3: "Ba Mươi",
            4: "Bốn Mươi",
            5: "Năm Mươi",
            6: "Sáu Mươi",
            7: "Bảy Mươi",
            8: "Tám Mươi",
            9: "Chín Mươi",
        }

        don_vi = {
            0: "",
            1: "Một",
            2: "Hai",
            3: "Ba",
            4: "Bốn",
            5: "Năm",
            6: "Sáu",
            7: "Bảy",
            8: "Tám",
            9: "Chín",
        }
        n_chuc_nghin = n // 10000
        n_nghin = (n % 10000) // 1000
        n_tram = (n % 1000) // 100
        n_chuc = (n % 100) // 10
        n_don_vi = n % 10
        start=True
        while start:
            if  n_don_vi!=0 and n_chuc!=0 and n_tram!=0 and n_nghin!=0 and n_chuc_nghin!=0:
                print(f"{chuc_nghin[n_chuc_nghin]} {nghin[n_nghin]} {tram[n_tram]} {chuc[n_chuc]} {don_vi[n_don_vi]}")
                break
            elif  n_don_vi==0 and n_chuc==0 and n_tram==0 and n_nghin==0 :
                print(f"{chuc_nghin[n_chuc_nghin]} {nghin[n_nghin]} {tram[n_tram]} {chuc[n_chuc]} {don_vi[n_don_vi]}")
                break
            start=False
        while not start:
            if n_nghin==0:
                nghin[0]="Nghìn"
            if n_tram==0:
                tram[0]="Không Trăm"
            if n_chuc==0:
                chuc[0]="Lẻ"
            print(f"{chuc_nghin[n_chuc_nghin]} {nghin[n_nghin]} {tram[n_tram]} {chuc[n_chuc]} {don_vi[n_don_vi]}")
            start=True

def cau88(n):
    arr=[]
    for i in range(2,n):
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
        if prime:
            arr.append(i)
    for i in range(int(len(arr))):
        print(arr[i])

def cau89(a,b):
    arr=[]
    for i in range(a,b+1):
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
        if prime:
            arr.append(i)
    for i in range(int(len(arr))):
        print(arr[i])

def cau90(a,b,n):
    count=0
    for i in range(a+b,n+1):
        if i>0:
            count+=1
    print(count)

def cau91(a,b,n):
    count=0
    for i in range(n,a**b):
        if i>0:
            count+=1
    print(count)

def cau92(n):
    if n == 0:
        print( "0" )
    arr=[]
    while n > 0:
        x = n % 2
        n //= 2
        arr.append(x)
    arr.reverse()
    for i in range(int(len(arr))):
        print( arr[i], end="" ) 

def cau93(n):
    if n == 0:
        print( "0" )
    arr=[]
    while n > 0:
        x = n % 2
        n //= 2
        arr.append(x)
    arr.reverse()
    count=0
    for i in arr:
        if i==1:
            count+=1
    print(count)

def cau94(a,b):
    n = str(a)+str(b)
    print(int(n)**2)

def cau95(a,b):
    x = str(a)+str(b)
    n=int(x)
    if n == 0:
        print( "0" )
    arr=[]
    while n > 0:
        x = n % 2
        n //= 2
        arr.append(x)
    arr.reverse()
    for i in range(int(len(arr))):
        print( arr[i], end="" ) 

def cau96(a,b,c):
    if 0 < a <= 1000 and 0 < b <= 1000 and 0 < c <= 1000:
        print(len(str(a)))
        print(len(str(b)))
        print(len(str(c)))

def cau97(a,b,c):
    num=[str(a),str(b),str(c)]
    arr=[]
    for i in num:
        for j in num:
            for k in num:
                if i!=j and i!=k and j!=k :
                    arr.append(i+j+k)
    for i in range(int(len(arr))):    
        print(arr[i])

def cau98(a,b,c):
    num=[str(a),str(b),str(c)]
    arr=[]
    sum=0
    for i in num:
        for j in num:
            for k in num:
                if i!=j and i!=k and j!=k :
                    arr.append(i+j+k)
    for i in range(int(len(arr))):    
        sum+=int(arr[i])
    print(sum)

def cau99(a,b,c):
    num=[str(a),str(b),str(c)]
    arr=[]
    max=0
    for i in num:
        for j in num:
            for k in num:
                if i!=j and i!=k and j!=k :
                    arr.append(i+j+k)
    for i in range(int(len(arr))):    
        if int(arr[i])>max:
            max=int(arr[i])
    print(max)

def cau100(a,b,c):
    num=[str(a),str(b),str(c)]
    arr=[]
    max=0
    for i in num:
        for j in num:
            for k in num:
                if i!=j and i!=k and j!=k :
                    arr.append(i+j+k)
    for i in range(int(len(arr))):    
        if int(arr[i])>max:
            max=int(arr[i])
    min=max
    for i in range(int(len(arr))):    
        if int(arr[i])<min:
            min=int(arr[i])
    print(min, max)

def cau101(a,b,c):
    num=[str(a),str(b),str(c)]
    arr=[]
    max=0
    for i in num:
        for j in num:
            for k in num:
                if i!=j and i!=k and j!=k :
                    arr.append(i+j+k)
    for i in range(int(len(arr))):    
        if int(arr[i])>max:
            max=int(arr[i])
    min=max
    for i in range(int(len(arr))):    
        if int(arr[i])<min:
            min=int(arr[i])
    arr_max=[int(x) for x in str(max)]
    arr_min=[int(x) for x in str(min)]
    valid=True
    max_max=max
    min_min=min
    for i in range(int(len(arr_max))-1):
        if arr_max[i]==arr_max[i+1]:
            valid=False
            break
    if valid:
        print(max_max)
    if not valid:
        valid=True
        for i in range(int(len(arr_min))-1):
            if arr_min[i]==arr_min[i+1]:
                valid=False
                break
    if valid:
        print(min_min)
    else:
        print(-1)

def cau102(n):
    arr=[int(x) for x in str(n)]
    arr[0], arr[-1] = arr[-1], arr[0]
    for i in arr:
        print(round(i), end="")

def cau103(n):
    arr=[int(x) for x in str(n)]
    for i in arr:
        if i>max:
            max=i
    min=max
    for i in arr:
        if i<min:
            min=i
    for i in range(int(len(arr))):
        if arr[i]==max:
            arr[i]="swapped"
            print(arr[i])
    for i in range(int(len(arr))):
        if arr[i]==min:
            arr[i]=max
    for i in range(int(len(arr))):
        if arr[i]=="swapped":
            arr[i]=min
    for i in arr:
        print(round(i), end="")

def cau104(p,k,q):
    res = p / q
    dec = str(res).split('.')[1]
    print(dec)

    if k <= len(dec):
        kth = int(dec[k - 1])
        print(f"Chữ số thứ {k} sau dấu thập phân của {p}/{q} là {kth}.")
    else:
        print(f"Không có chữ số thứ {k} sau dấu thập phân của {p}/{q}.")

def cau105(n):
    arr = [int(x) for x in str(n)]
    x=arr[-1]
    arr.pop()
    for i in arr:
        print(f"{i}*", end="")
    print(x)

def cau106(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False 
    p = 2
    while (p * p <= n):
        if primes[p] == True:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    print( [x for x in range(n+1) if primes[x]] )

def cau107(m,n):
    arr_m=[int(x) for x in str(m)]
    arr_n=[int(x) for x in str(n)]
    if int(len(arr_m))==int(len(arr_n)):
        print("m, n la 2 so gia tuong duong")
    else:
        print("m, n khong phai 2 so gia tuong duong")

def cau108(m,n):
    arr_m=[int(x) for x in str(m)]
    arr_n=[int(x) for x in str(n)]
    valid=False
    for i in arr_m:
        for j in arr_n:
            if i==j:
                print("m, n la 2 so tuong duong")
                valid=True
                break
    if not valid:
        print("m, n khong phai 2 so tuong duong")
    print(arr_m, arr_n)
    
def cau109(m,n):
    fre_m={}
    fre_n={}
    arr_m=[int(x) for x in str(m)]
    arr_n=[int(x) for x in str(n)]
    for i in arr_m:
        if i in fre_m:
            fre_m[i]+=1
        else:
            fre_m[i]=1
    for i in arr_n:
        if i in fre_n:
            fre_n[i]+=1
        else:
            fre_n[i]=1
    if fre_m==fre_n and int(len(arr_m))==int(len(arr_n)):
        print("m, n la 2 so tuong duong")
    else:
        print("m, n khong phai 2 so tuong duong")

def cau110(a,b):
    div_a=0
    div_b=0
    for i in range(1,a):
        if a%i==0:
            div_a+=1
    for i in range(1,b):
        if b%i==0:
            div_b+=1
    if div_a>div_b:
        print(a)
    elif div_a<div_b:
        print(b)
    else:
        if a>b:
            print(b)
        else:
            print(b)

if __name__=="__main__":
    var  =int(input())
    var_1=int(input())
    var_2=int(input())
    # var_3=int(input())
    # var_4=int(input())
    # var_5=int(input())

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
    # cau34(var)
    # cau35(var)
    # cau36(var)
    # cau37(var)
    # cau38(var)
    # cau39(var)
    # cau40(var)
    # cau41(var)
    # cau42(var)
    # cau43(var, var_1)
    # cau44(var, var_1, var_2)
    # cau45(var, var_1, var_2)
    # cau46(var, var_1, var_2)
    # cau47(var)
    # cau48(var, var_1)
    # cau49(var)
    # cau50(var)
    # cau51(var)
    # cau52(var)
    # cau53(var)
    # cau54(var, var_1)
    # cau55(var)
    # cau56(var)
    # cau57(var)
    # cau58(var)
    # cau59(var)
    # cau60(var)
    # cau61(var)
    # cau63(var)
    # cau64(var, var_1)
    # cau65(var, var_1)
    # cau66(var)
    # cau67(var)
    # cau68a(var)
    # cau68b(var)
    # cau68c(var)
    # cau68d(var)
    # cau68e(var)
    # cau68f(var)
    # cau68g(var)
    # cau69(var)
    # cau70(var)
    # cau71(var, var_1)
    # cau72(var)
    # cau73(var)
    # cau74(var, var_1)
    # cau75(var, var_1, var_2)
    # cau76(var, var_1, var_2, var_3, var_4, var_5)
    # cau77(var)
    # cau78(var)
    # cau79(var)
    # cau80(var)
    # cau81()
    # cau82(var)
    # cau83(var)
    # cau84(var, var_1, var_2)
    # cau85(var, var_1)
    # cau86(var)
    # cau87(var)
    # cau88(var)
    # cau89(var, var_1)
    # cau90(var, var_1, var_2)
    # cau91(var, var_1, var_2)
    # cau92(var)
    # cau93(var)
    # cau94(var, var_1)
    # cau95(var, var_1)
    # cau96(var, var_1, var_2)
    # cau97(var, var_1, var_2)
    # cau98(var, var_1, var_2)
    # cau99(var, var_1, var_2)
    # cau100(var, var_1, var_2)
    # cau101(var, var_1, var_2)
    # cau102(var)
    # cau103(var)
    # cau104(var, var_1, var_2)
    # cau105(var)
    # cau106(var)
    # cau107(var, var_1)
    # cau108(var, var_1)
    # cau109(var, var_1)
    cau110(var, var_1)



