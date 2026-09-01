def slove(s):
    for c in s:
        if c != '4' and c != '7':
            return False
    return True
            
T = int(input())
for i in range(T):
    s = input()
    if slove(s):
        print('YES')
    else:
        print('NO')
