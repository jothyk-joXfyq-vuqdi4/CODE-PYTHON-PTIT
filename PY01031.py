if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        a , b = map(int , input().split())
        if a==0:
            print(0)
        else:
            res = ''
            while a > 0:
                x = int(a%b)
                a = a//b
                if x>=10:
                    x = ord('A')+x-10
                    res+=chr(x)
                else:
                    x = ord('0') + x
                    res+=chr(int(x))
            res = res[::-1]
            print(res)
        # a = 10
        # b = 2
        # x = 0
        # a=5
        # res = 0
        # x=1
        # a=2
        # res = 01
        # x=0
        # a=1
        # res = 010
        # x=1
        # a=0
        # res = 0101
        