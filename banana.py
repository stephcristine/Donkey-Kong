from caracteres import *

class Banana(Caracteres):
    def __init__(self):
        pass

b = '\033[0;33;40m█\033[m'
a = '\033[0;33;40m▄\033[m'
n = '\033[0;33;40m▀\033[m'

print(" " + a)
print(b)
print(" " + n)

t = '\033[1;33;40m(\033[m'

print(t)