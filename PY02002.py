a = []
a.append(1)
a.append(1)
for i in range(2 , 93 , 1):
    a.append(a[i-1] + a[i-2])
if __name__ == '__main__':
    t = int(input())
    for x in range(t):
        start , end = map(int , input().split())
        for i in range(start-1 , end , 1):
            print(a[i] , end = ' ')
        print()