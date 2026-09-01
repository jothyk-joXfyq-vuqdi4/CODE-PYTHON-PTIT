T = int(input())
for t in range(T):
    c1 = [0] * 300
    c2 = [0] * 300
    s1 = input()
    s2 = input()
    for c in s1:
        c1[ord(c)]+=1
    for c in s2:
        c2[ord(c)]+=1
    check = True
    for i in range(0 , 300 , 1):
        if c1[i] != c2[i] : check = False
    if check:
        print('Test '+str(t+1)+': YES')
    else:
        print('Test '+str(t+1)+': NO')
