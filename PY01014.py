if __name__ == '__main__':
    a , k , n = map(int , input().split())
    res = []
    moc = -1
    for b in range(1 , n-a+1 , 1):
        if(a+b)%k==0:
            moc = b 
            break
    
    if(moc==-1):
        print(-1)
    else:
        for b in range(moc , n-a+1 , k):
            res.append(b)
        for x in res:
            print(x , end = ' ')