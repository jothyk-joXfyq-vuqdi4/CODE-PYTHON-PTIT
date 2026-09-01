def summ(s):
    t = 0
    for c in s:
        if c.isdigit():
            t+=int(c)
    tmp = str(t)
    return tmp
if __name__ == '__main__':
    s = input()
    res = ''
    if s[0] == '-':
        res = s[1:]
    else : 
        res = s
    cnt = 0 
    while len(res) != 1:
        res = summ(res)
        cnt+=1
    if(cnt == 0):
        cnt = 1
    print(cnt)