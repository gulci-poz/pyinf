# -*- coding: utf-8 -*-

number = 0.0
total = 0.0
average = 0.0
count = 0

while True:
    # w py3 mamy input zamiast raw_input()
    number = float(input('enter a number to add (-1 exit) > '))
    if number == -1:
        break
    total += number
    count += 1

average = total / count
print ('Average: %.3f' % average)
