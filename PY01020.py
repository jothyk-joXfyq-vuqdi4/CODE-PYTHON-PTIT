def slove(s):
    return int(s[len(s)-2:]) == 86
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        if(slove(input())):
            print('YES')
        else:
            print('NO')
