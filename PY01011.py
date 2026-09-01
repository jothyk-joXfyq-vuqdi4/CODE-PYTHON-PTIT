def slove(s):
    if(int(s) != int(s[::-1])):
        return False
    for c in s:
        if c!='0' and c!='2' and c!='4' and c!='6' and c!='8':
            return False 
    if(len(s) %2 == 1):
        return False
    return True 
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = int(input())
        for i in range(22 , n):
            if slove(str(i)):
                print(i , end = ' ')
        print()
