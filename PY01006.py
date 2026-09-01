def check(s):
    for char in s:
        if char != '4' and char != '7': 
            return False 
    return True

t = int(input())
for i in range(0 , t , 1):
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')
