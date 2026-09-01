import math
def gcd(a , b):
    while b!=0:
        tmp = b
        b = a%b
        a = tmp
    return a
def prime(a):
    if a<2: return False 
    for i in range(2 , int(math.sqrt(a)) + 1 , 1):
        if a%i==0 : return False
    return True
t = int(input())
for i in range(0 , t , 1):
    n = int(input())
    cnt = 0 
    for j in range(1 , n , 1):
        if gcd(n , j) ==1 :
            cnt = cnt + 1 
    if prime(cnt) :
        print("YES")
    else :
        print("NO")
