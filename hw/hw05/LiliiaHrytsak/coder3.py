def is_isogram(word):
    for i in word.lower():
        if word.lower().count(i)>1:
            return False
    return True

print(is_isogram('wWord'))