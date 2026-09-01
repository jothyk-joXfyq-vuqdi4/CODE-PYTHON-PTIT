if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    cnt = 0 
    for u in range(0 , n , 1):
        for v in range(u+1 , n , 1):
            if(a[u] > a[v]):
                cnt+=1
    print(cnt)