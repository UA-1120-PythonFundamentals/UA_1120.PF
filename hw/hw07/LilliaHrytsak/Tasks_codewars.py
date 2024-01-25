
# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# II. Find The Distance Between Two Points
from math import sqrt


def distance(x1, y1, x2, y2):
    res = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(res, 2)


# III. No yelling!
def filter_words(st):
    st = ' '.join(st.capitalize().split())
    return st


# IV. Convert a Number to a String
def number_to_string(num):
    res = f'{num}'
    return res

# V. Reversing Words in a String
def reverse(st):
    word_list = st.split()
    word_list.reverse()
    res_str = ' '.join(word_list)
    return res_str


# VI. Reverse List Order
def reverse_list(l):
    l.reverse()
    return l


# VII. Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    l = []
    for i in range(3,number):
        if i not in [] and (i%3==0 or i%5==0):
            l.append(i)
    return sum(l)


# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left*mpg<distance_to_pump:
        return False
    return True


# IX. Are You Playing Banjo?
def play_bondgo():
    name = input()
    if name[0].lower()=='r':
        return f'{name} plays banjo'
    return f'{name} does not play banjo'


# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(b):
    return "Yes" if b else "No"


# XI. Counting sheep
def count_sheeps(sheep):
    return sum(sheep)


# XII. Is this my tail?
def correct_tail(body, tail):
    sub = body[-len(tail):]
    if sub == tail:
        return True
    return False
