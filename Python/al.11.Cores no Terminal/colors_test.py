from colors import *

clean = color['clean']
bold = color_bold['white']
underline = color_underline['white']
underline_bold = color_underline_bold['white']

print(f'\n\nNomal Colors\n')
for key, value in color.items():
    print(f'{value}{key}{clean}')

print(f'\n\n{bold}Bold Colors{clean}\n')
for key, value in color_bold.items():
    print(f'{value}{key}{clean}')

print(f'\n\n{underline}Bold Colors{clean}\n')
for key, value in color_underline.items():
    print(f'{value}{key}{clean}')

print(f'\n\n{underline_bold}Bold Colors{clean}\n')
for key, value in color_underline_bold.items():
    print(f'{value}{key}{clean}')