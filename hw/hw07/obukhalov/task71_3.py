#!/usr/bin/env python


def character_numbers(word):
    char_dict = {}
    for c in word:
        if char_dict.get(c):
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict


if __name__ == "__main__":
    word = input("Input any string: ")
    d = character_numbers(word)
    print(d)
