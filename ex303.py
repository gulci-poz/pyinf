# -*- coding: utf-8 -*-

name = "gulci"
greeting = "Hello, World!"
strip_test = " Hello, World!"
rstrip_test = "Hello, World! "

print(len(name))

print(name[0])

# mamy przedział otwarty, druga liczba minus jeden
print(name[0:3])

# wszystko po tym znaku
print(name[3:])

#ilość znaków
print(name[:3])

print(name * 2)

print(greeting.split(','))

# strip() sprawdza string z obu stron
print("|" + strip_test)
print("|" + strip_test.strip())

# rstrip() sprawdza string tylko z prawej strony
print(rstrip_test + "|")
print(rstrip_test.rstrip() + "|")
