#learning how to use *args

def add(*args):
    sum = 0
    for number in args:
        sum += number
    return sum

class Car:
    def __init__(self, **kw):
        self.color = kw.get("color")
        self.speed = kw.get("speed")
#the *kw helps users get key word arguments rather than use regular arguments that are preset.
#use kw.get to make sure that if the key word is not specified you don't get screwed