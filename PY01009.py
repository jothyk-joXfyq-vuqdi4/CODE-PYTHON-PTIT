if __name__ == '__main__':
    s = input()
    hoa , thuong = 0 , 0
    for c in s:
        if(c.islower()) :
            thuong+=1
        else:
            hoa+=1
    if hoa > thuong:
        print(s.upper())
    else:
        print(s.lower())