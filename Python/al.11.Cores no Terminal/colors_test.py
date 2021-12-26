from colors import *

clean = color['clean']
bold = color_bold['white']
underline = color_underline['white']
underline_bold = color_underline_bold['white']

print(f'\n\nNomal Colors\n')
i = 1
for key, value in color.items():
    space = ' ' * (18-len(key)-len(str(i)))
    print(f'{i}-{value}{key}{clean};{space}', end = '')
    if i % 3 == 0:
        print('')
    i += 1

print(f'\n\n\n{bold}Bold Colors{clean}\n')
i = 1
for key, value in color_bold.items():
    space = ' ' * (18-len(key)-len(str(i)))
    print(f'{i}-{value}{key}{clean}{space}', end = '')
    if i % 3 == 0:
        print()
    i += 1

print(f'\n\n\n{underline}Undeline Colors{clean}\n')
i = 1
for key, value in color_underline.items():
    space = ' ' * (18-len(key)-len(str(i)))
    print(f'{i}-{value}{key}{clean};{space}', end = '')
    if i % 3 == 0:
        print()
    i += 1

print(f'\n\n\n{underline_bold}Underline Bold Colors{clean}\n')
i = 1
for key, value in color_underline_bold.items():
    space = ' ' * (18-len(key)-len(str(i)))
    print(f'{i}-{value}{key}{clean};{space}', end = '')
    if i % 3 == 0:
        print()
    i += 1

print('\n')
