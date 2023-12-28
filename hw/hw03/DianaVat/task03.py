philosophy = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""

def countWords(word):
   return str(philosophy.count(word))
print("Better is " + countWords("better"))
print("Is is " + countWords("is"))
print("Never is " + countWords("never"))

print(philosophy.upper())

def findWords ():
   return philosophy.replace("i","&")
print (findWords())


numberFour = 5674
one = int( numberFour / 1000)
two = int(numberFour / 100 % 10)
three = int(numberFour / 10 % 10)
four = int (numberFour  % 10)
print(one*two*three*four)
print(str(numberFour)[::-1])
print (sorted([one,two,three,four]))

first = 1
second = 2

first, second = second, first
print(first, second)
