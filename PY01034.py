def slove(s):
    res = list(s)
    n = len(s)
    i = n - 1
    
    # 1. Tìm vị trí i đầu tiên từ dưới lên mà s[i] < s[i-1]
    while i > 0 and s[i] >= s[i-1]:
        i -= 1
        
    if i <= 0: 
        return '-1'
        
    j = i - 1 # Vị trí cần đổi chỗ (s[j] > s[i])
    
    # 2. Tìm vị trí t thuộc [i, n-1] sao cho s[t] < s[j] và s[t] là LỚN NHẤT
    # Nếu bằng nhau thì ưu tiên lấy chỉ số x lớn hơn (xuất hiện sau)
    t = -1
    for x in range(i, n):
        if s[x] < s[j]:
            if t == -1 or s[x] >= s[t]:
                t = x
                
    # Nếu không tìm thấy t hợp lệ hoặc đổi số '0' lên đầu tiên (j == 0)
    if t == -1 or (j == 0 and s[t] == '0'):
        return '-1'
        
    # 3. Đổi chỗ s[j] và s[t]
    res[j], res[t] = res[t], res[j]
    
    return ''.join(res)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(slove(input().strip()))