import random
class Ghost:
    def init (self):
        self.color = random.choice(["white","yellow","purple","red"])
ghost = Ghost()
ghost.color