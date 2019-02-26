from math import log
n = input('Number to use: ')
print('Challenge:', ''.join([str(int(c) + 1) for c in str(n)]))
# Create list of new digits, i.e. [10, 10, 9]
digits = [int(int(n) % 10 ** i / 10 ** (i - 1)) + 1 for i in reversed(range(1, int(log(int(n), 10) + 1) + 1))]
# Set p to the length of our new number, i.e. 5
p = sum([max(x - 8, 1) for x in digits])
# Sum each digit taken to the correct power
x = 0
i = 0
while i < len(digits):
    d = digits[i]
    p = p - 2 if d > 9 else p - 1
    x = x + (10 ** p) * d
    i = i + 1
print('Bonus', x)
