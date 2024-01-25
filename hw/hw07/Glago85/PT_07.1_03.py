#Write a function that calculates the number of characters included in a given string
# - input: "hello"
# - output: {"h":1, "e":1,"l":2,"o":1}

def count_letters(string):
    lett_dict = {}
    for l in string:
        if l in lett_dict:
            lett_dict[l] += 1
        else:
            lett_dict[l] = 1
    return lett_dict