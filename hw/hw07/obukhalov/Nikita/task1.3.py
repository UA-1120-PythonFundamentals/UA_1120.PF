def func(word):
    d = {}
    for i in word:
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1
    return d

word = str(input('Enter your word: '))
a = func(word)
print(a)


