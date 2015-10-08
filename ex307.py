# -*- coding: utf-8 -*-

grades = ['Raymond', 92, 'Cynthia', 83, 'Terrill', 64, 'Jennifer', 75, 'Clayton', 88, 'David', 91, 'Bryan', 100, 'Danny', 99]

print(grades)

# nie można konkatenować stringów i intów, trzeba użyć str()
print(grades[0] + ' ' + str(grades[1]))

# takie dane lepiej do dictionary
# kolejność danych w dict nie ma znaczenia

grades_dict = {'Raymond':92, 'Cynthia':83, 'Terrill':64, 'Jennifer':75, 'Clayton':88, 'David':91, 'Bryan':100, 'Danny':99}

# zwracają listę
print(grades_dict.keys())
print(grades_dict.values())

print(grades_dict['Bryan'])
