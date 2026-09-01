def slove(s):
    for i in range(1 , len(s) , 1):
        if s[i] < s[i-1]:
            return False
    return True
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        if slove(input()):
            print('YES')
        else:
            print('NO')
    