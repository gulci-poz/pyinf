# -*- coding: utf-8 -*-

outFile = open('text.txt', 'w')

outFile.write('first line\n')
outFile.write('second line\n')

# funkcja write() zapisuje dane do bufora
# konieczne jest wywołanie close(), żeby dane zostały zapisane do pliku

# nie pokrywa się to z rzeczywistościa
# dane są zapisane do pliku, mimo braku wywołania close()

outFile.close()
