
philisophy = """Beautiful is better than ugly.
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

better_counter = never_counter = is_counter = 0

for el in philisophy.split():
    if el.startswith('better'):
        better_counter += 1
    elif el.startswith('never'):
        never_counter += 1
    elif el.startswith('is'):
        is_counter += 1

print(f'better = {better_counter}', end='; ')
print(f'never = {never_counter}', end='; ')
print(f'is = {is_counter}', end='\n\n')

print(philisophy.upper(), end='\n\n')

print(philisophy.replace('i', '&'))
