import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    a, K, N = map(int, data)
    b_start = K - (a % K)
    b_max = N - a
    if b_start > b_max:
        print(-1)
        return
    results = range(b_start, b_max + 1, K)
    print(*(results))

if __name__ == '__main__':
    solve()