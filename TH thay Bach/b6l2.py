import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    digits = ['0', '2', '4', '6', '8']
    for i in range(1, t + 1):
        n = int(input_data[i])
        results = []
        queue = ['2', '4', '6', '8']
        while queue:
            half = queue.pop(0)
            full_num = int(half + half[::-1])
            if full_num >= n:
                break
            results.append(str(full_num))
            if len(half) < 3:
                for d in digits:
                    queue.append(half + d)
                    
        print(*(results))

if __name__ == '__main__':
    solve()