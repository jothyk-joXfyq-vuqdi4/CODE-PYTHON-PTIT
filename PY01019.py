import math
def slove(s1):
    s2 = s1[::-1]
    for i in range(1 , len(s1) , 1):
        if abs(ord(s1[i])-ord(s1[i-1])) != abs(ord(s2[i])-ord(s2[i-1])):
            return False
    return True 
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        if slove(input()):
            print("YES")
        else:
            print("NO")