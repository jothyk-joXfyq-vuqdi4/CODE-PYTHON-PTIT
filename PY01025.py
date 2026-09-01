s = input()
res = ''
cnt = 0
for i in range(len(s)-1 , -1 , -1):
    res += s[i]
    cnt+=1
    if i!= 0 and cnt%3==0 :
        res+=','
    
print(res[::-1])
