p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
def slove(s , k):
    res = ''
    for i in range(0 , len(s) , 1):
        res+=p[(p.find(s[i])+k)%28]
    return res
if __name__ == '__main__':
    while True:
        a = input().split()
        k = int(a[0])
        if k==0:
            break
        else:
            s = a[1]
            res = slove(s,k)
            print(res[::-1])