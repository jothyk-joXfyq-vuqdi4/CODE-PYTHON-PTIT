from functools import cmp_to_key
def tong(n):
    res = 0
    st = str(n)
    for c in st:
        res += int(c)
    return res
def cmp(a , b):
    return a[1] - b[1]
a = [1 , 22 , 3 , 2, 9 , 4 , 43 , 24 , 53]
a.sort(key = lambda x :(tong(x) , x))
print(a)