class Dog(object):
    def makeNoise(self):
        print("woof...")

class Duck(object):
    def makeNoise(self):
        print("quack...")

animals = [Dog(), Duck()]

for a in animals:
    a.makeNoise()

'''
This file is an example of how individual objects
might handle a method in different ways
'''