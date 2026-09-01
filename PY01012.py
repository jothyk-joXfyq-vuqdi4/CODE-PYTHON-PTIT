if __name__ == '__main__':
    s1 = input()
    s2 = input()
    index = int(input())
    res = ''
    for i in range(0,index-1,1):
        res+=s1[i]
    res+=s2
    for i in range(index-1 , len(s1) , 1):
        res+=s1[i]
    print(res)