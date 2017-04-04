#-*- coding:utf-8 -*-
#from PIL.Image import core as image
from PIL import Image
import argparse

#\u547d\u4ee4\u884c\u8f93\u5165\u53c2\u6570\u5904\u7406
parser = argparse.ArgumentParser()

parser.add_argument('file')     #\u8f93\u5165\u6587\u4ef6
parser.add_argument('-o', '--output')   #\u8f93\u51fa\u6587\u4ef6
parser.add_argument('--width', type = int, default = 80) #\u8f93\u51fa\u5b57\u7b26\u753b\u5bbd
parser.add_argument('--height', type = int, default = 80) #\u8f93\u51fa\u5b57\u7b26\u753b\u9ad8

#\u83b7\u53d6\u53c2\u6570
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# \u5c06256\u7070\u5ea6\u6620\u5c04\u523070\u4e2a\u5b57\u7b26\u4e0a
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print (txt)
    
    #\u5b57\u7b26\u753b\u8f93\u51fa\u5230\u6587\u4ef6
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)