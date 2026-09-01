if __name__ == '__main__':
    t = int(input())
    for x in range(t):
        s = input()
        dau = int(s[0:2])
        cuoi = int(s[len(s)-2:len(s)])
        if dau == cuoi:
            print('YES')
        else:
            print('NO')