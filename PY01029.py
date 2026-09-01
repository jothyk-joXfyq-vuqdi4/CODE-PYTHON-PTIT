import math
T = int(input())
for t in range(T):
    n1 = int(input())
    s = str(n1)
    n2 = int(s[::-1])
    if math.gcd(n1,n2) == 1:
        print('YES')
    else:
        print('NO')