import random

class Ghost:
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        
        self.color = random.choice(colors)

ghost = Ghost()