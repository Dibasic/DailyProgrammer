import string
import random
import time

String = 'shakespeare'
monkeyOutput = ''
monkeyOutputchar = ''
a=time.time()
while monkeyOutput != String:
    monkeyOutput = ''
    while len(monkeyOutput) < len(String):
        monkeyOutput += random.choice(string.printable)
b=time.time()
c = b - a
print ('solved ' + String + ' in ' + str(c) + ' seconds')
input()
