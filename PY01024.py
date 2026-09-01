def check(s):
    t = 0
    for c in s:
        t+=int(c)
    if t%10 != 0: return False
    for i in range(1 , len(s) , 1):
        if abs(ord(s[i]) - ord(s[i-1])) != 2: return False
    return True 
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        if check(input()):
            print('YES')
        else:
            print('NO')

        
