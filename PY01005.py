s = input()
cnt = 0
for char in s:
    if char == '4' or char == '7':
        cnt = cnt + 1
if(cnt == 4 or cnt == 7):
    print('YES')
else:
    print('NO')