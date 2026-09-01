def check(s):
    for i in range(0 , len(s) , 1):
        if s[i]!='6' and s[i]!='8' : return False
        if s[i] == '8':
            if i-1 < 0 :
                return False
            if s[i-1] == '8':
                if i-2 < 0:
                    return False
                if s[i-2] == '8':
                    return False
        

    return True 
if __name__ == '__main__':
    if check(input()):
        print('YES')
    else:
        print('NO')
        
