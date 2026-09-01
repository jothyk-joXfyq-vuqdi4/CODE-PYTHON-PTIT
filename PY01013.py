import math
def summ(str):
    s = 0
    for c in str:
        s += int(c)
    return s
def prime(a):
    if a<2:
        return False
    for i in range(2 , int(math.sqrt(a)+1) , 1):
        if a%i==0:
            return False
    return True
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        a , b = map(int , input().split())
        if prime(summ(str(math.gcd(a,b)))):
            print('YES')
        else:
            print('NO')
