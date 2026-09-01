def slove(s):
    tu = ''
    so = 0
    for c in s:
        if c<'0' or c>'9':
            tu = c
        else:
            for i in range(int(c)):
                print(tu , end='')
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        slove(input())
        print()