# każda zmiana tuple tworzy nową kopię
empty = ()

# tuple nie można zmieniać
# można mieć tuple z elementami do zmiany, np. z listą

singleton = '1',

print(singleton)

numbers = (1, 2, 3, 4)

print(numbers[0])

print(len(numbers))

print(numbers[0:2])

num1 = (1, 2)
num2 = (3, 4)
num3 = num1 + num2

print(num3)

sentence = ('now', 'is', 'the', 'time')
print(sentence * 3)
