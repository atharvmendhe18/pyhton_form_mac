from pyfiglet import Figlet
import sys
import random

print('hello')

figlet = Figlet()
fonts = figlet.getFonts()
print(len(sys.argv))
if len(sys.argv) == 3 and sys.argv[2] in fonts and sys.argv[1] == '-f' or sys.argv[1] == '--font':
    figlet.setFont(font=sys.argv[2])
    name = input('Input: ')
    print(figlet.renderText(name))
elif len(sys.argv) == 1:
    font_ = random.choice(fonts)
    figlet.setFont(font=font_)
    name_ = input('Input: ')
    print(figlet.renderText(name_))
    print('122')
else:
    sys.exit()

print('hello')
