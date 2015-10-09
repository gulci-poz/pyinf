# -*- coding: utf-8 -*-

textfile = open('text.dat', 'a')

# przekierowujemy strumień za pomocą print, bez zmiany sys.stdout
# zwykłe print działa tylko w py2
print >> textfile, 'karolcia'

# dzięki temu zachowujemy możliwość standardowego drukowania na ekran
print('goodbye')
