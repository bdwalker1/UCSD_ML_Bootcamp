from collections import namedtuple

ColorRGB = namedtuple('ColorRGB',['red', 'green', 'blue'])
color = ColorRGB(red=55, green=255, blue=155)

print(color.red)
print(color.green)
print(color.blue)