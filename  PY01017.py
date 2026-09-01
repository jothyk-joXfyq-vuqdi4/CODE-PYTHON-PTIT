def slove(s):
    res = ''
    cnt = 1
    char = s[0]
    for i in range(1 , len(s) , 1):
        if s[i] == s[i-1]:
            cnt+=1
        else:
            res += str(cnt) + char
            char =s[i]
            cnt = 1
    res += str(cnt) + s[len(s)-1]
    return res
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print(slove(input()))

