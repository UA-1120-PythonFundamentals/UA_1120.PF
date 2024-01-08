#/usr/bin/env python

#Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        name += " plays banjo"
    else:
        name += " does not play banjo"
    return name
