def binary(a):
    arr=[]
    while a!=0:
        temp=int(a%2)
        arr.append(temp)
        a/=2
    return arr

def doi_nghich():
    a=int(input("a="))
    b=int(input("b="))
    arr_a=binary(a)
    arr_b=binary(b)
    sum_a=0
    sum_b=0
    for i in arr_a:
        sum_a+=i
    for i in arr_b:
        sum_b+=i
    if sum_a==sum_b:
        print("a va b khong phai la cap so doi nghich")
    else:
        print("a va b la cap so doi nghich")
    
if __name__ == "__main__":
    doi_nghich()