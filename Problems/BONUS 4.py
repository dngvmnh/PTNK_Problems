def binary(a):
    arr=[]
    while a!=0:
        temp=int(a%2)
        arr.append(temp)
        a/=2
    return arr
def check(a,b):
    arr_a=binary(a)
    arr_b=binary(b)
    sum_a=0
    sum_b=0
    for i in arr_a:
        sum_a+=i
    for i in arr_b:
        sum_b+=i
    if sum_a==sum_b:
        return True
    else:
        return False
    
def get():
    while True:
        try:
            x=int(input("x="))
            if x <= 0:
                continue
            break
        except ValueError:
            pass
    while True:
        try:
            y=int(input("y="))
            if y<x:
                continue
            break
        except ValueError:
            pass
    return x,y

def check_doi_nghich():
    x,y=get()
    total=0
    for i in range(x,y):
        for j in range(x,y):
            valid=check(i,j)
            if valid:
                total+=1
    return total

if __name__ == "__main__":
    total=check_doi_nghich()
    print(f'co {total} cap doi nghich')