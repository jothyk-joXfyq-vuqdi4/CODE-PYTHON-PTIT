s = input()
a = s.split()
if(a[1] == '+'):
    if(int(a[0]) + int(a[2]) == int(a[4])):
        print("YES")
    else:
        print("NO")
elif(a[1] == '-'):
    if(int(a[0]) - int(a[2]) == int(a[4])):
        print("YES")
    else:
        print("NO")
elif(a[1] == '*'):
    if(int(a[0]) * int(a[2]) == int(a[4])):
        print("YES")
    else:
        print("NO")
else:
    if(int(a[0]) / int(a[2]) == int(a[4])):
        print("YES")
    else:
        print("NO")
