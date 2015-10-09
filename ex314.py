# -*- coding: utf-8 -*-

# counter zerujemy, dzięki temu na starcie while możemy iterować i sprawdzać
# unikamy podwójnego pisania iteracji

counter = 0
sum = 0

while counter <= 100:
    counter += 1

    if counter % 2 == 1:
        continue

    sum += counter

print("Even sum: %d" % sum)
