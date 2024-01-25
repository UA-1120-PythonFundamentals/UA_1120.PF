#!/usr/bin/env python


import random


class Ghost(object):

    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


if __name__ == "__main__":
    ghost = Ghost()
    print(ghost.color)  #=> "white" or "yellow" or "purple" or "red"
