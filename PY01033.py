import math
def check(a , b , c):
    return math.gcd(a , b) == 1 and math.gcd(b , c) == 1 and math.gcd(a , c) == 1 
if __name__ == "__main__":
    a , b = map(int , input().split())
    for x in range(a , b+1):
        for y in range(x+1 , b+1):
            for z in range(y+1 , b+1):
                if check(x , y , z):
                    print('(' , end = '')
                    print(x , y , z , sep = ', ' , end = ')')
                    print()
    