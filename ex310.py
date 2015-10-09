# -*- coding: utf-8 -*-

import sys

# w ten sposób print drukuje na standardowe wyjście
sys.stdout.write('hello\n')

# możemy przedefiniować standardowe wyjście
sys.stdout = open('text.dat', 'a')

# drukujemy na inne wyjście
# w tej sesji wszystkie wywołania print będą pisały do innego wyjścia
print('hello')
