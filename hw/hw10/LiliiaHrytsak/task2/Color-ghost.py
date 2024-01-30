import random
class Ghost(object):
    def __init__(self):
        list_colors =['white','yellow','purple','red']
        self.color = random.choice(list_colors)

a = Ghost()
print(a.color)