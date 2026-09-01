def slove(s):
    t = 0
    res = ''
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            t+=int(s[i])
        else:
            res+=s[i]
    res = ''.join(sorted(res))
    res+=str(t)
    return res
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print(slove(input()))
        