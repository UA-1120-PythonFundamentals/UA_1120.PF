def count_vowels(word):
    vovel_list = ['a', 'e', 'i', 'o', 'u']
    k = 0
    for i in word.lower():
        if i in vovel_list:
            k += 1
    return k

print(count_vowels('woooooard'))