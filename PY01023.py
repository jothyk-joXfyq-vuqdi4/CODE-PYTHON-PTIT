import math
T = int(input())
for t in range(T):
    res = ''
    res += '1 * '
    n = int(input())
    for i in range(2 , int(math.sqrt(n)+1) , 1):
        cnt = 0
        if n%i==0:
            while n%i==0:
                cnt+=1 
                n/=i
            res+= str(i) + '^' + str(cnt) + ' * '
    if n>1 :
        res += str(int(n)) + '^1'
    if res[len(res)-1] == ' ' and  res[len(res)-2] == '*':
        res = res[:len(res)-2]
    print(res)

        