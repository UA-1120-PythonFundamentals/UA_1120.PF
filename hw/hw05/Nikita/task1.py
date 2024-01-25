def changeType(a):
    
    for i in range(len(a)):
        a[i] = float(a[i])
    
    return a

    
f_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(changeType(f_i)) 