import sys

def is_palindromic_in_base(n, k):
    digits = []
    temp = n
    while temp > 0:
        digits.append(temp % k)
        temp //= k
    
    left, right = 0, len(digits) - 1
    while left < right:
        if digits[left] != digits[right]:
            return False
        left += 1
        right -= 1
    return True 

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a = int(input_data[0])
    b = int(input_data[1])
    m = int(input_data[2])
    
    # Bắt đầu duyệt từ max(2, a) nếu đề bài yêu cầu x >= 2
    start = max(2, a) 
    
    cnt = 0
    for x in range(start, b + 1):
        k_max = min(x - 2, m)
        ok = True
        for k in range(2, k_max + 1):
            if not is_palindromic_in_base(x, k):
                ok = False
                break
        if ok:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    solve()