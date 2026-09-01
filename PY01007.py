t = int(input())
for i in range(t):
    n , x , m = map(float , input().split())
    cnt = 0 
    while n < m:
        n*=(1+x/100) 
        cnt=cnt+1
    print(cnt)