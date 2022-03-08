# organizae image folder by color
# detects dominant color in image 
# and groups it with similar color by renaming file

# import
from colorthief import ColorThief
from matplotlib import colors
import os
from tkinter import *

def clrDetect(image):
    # Detect dominant color from image
    ct = ColorThief(image)
    dominant_color = ct.get_color(quality=1)
    # print ("Dominant color: ", dominant_color)

    ## convert RGB to HSV
    # scale RGB format from 255 to 1
    rgb = list()
    for x in range(len(dominant_color)):
        rgb.append(dominant_color[x] / 255)  
    # print ("RGB: ", rgb)

    hsv = colors.rgb_to_hsv(rgb)
    # scale hue value to 360
    hsv[0] = hsv[0] * 360
    # print ("HSV: ", hsv)

    # return hue value
    return hsv[0]

# test output
# image = 'blue.jpg'
# clrDetect(image)

# Create groups by hue range
def getColor(hue):
    # Red
    if hue >= 0 and hue <= 60: 
        domColor = 'Red'
    # Yellow
    elif hue >= 61 and hue <= 120: 
        domColor = 'Yellow'
    # Green
    elif hue >= 121 and hue <= 180: 
        domColor = 'Green'
    # Cyan
    elif hue >= 181 and hue <= 240: 
        domColor = 'Cyan'
    # Blue
    elif hue >= 241 and hue <= 300: 
        domColor = 'Blue'
    # Magenta
    elif hue >= 301 and hue <= 360: 
        domColor = 'Magenta'

    return domColor

## rename files based on dominant color
def fileNamer(path, name, color):
    os.chdir(path)
    os.rename(name, (color + name))
# prepend to file names instead of replace
# os.rename('red.jpg', 'blue.jpg')

## select directory
# dir = input("Enter directory: ")
# root = Tk()
# root.withdraw()
# path = filedialog.askdirectory()
# print (path)

#temp path
path = r"G:\Pictures\1080p"
absp = os.path.abspath(path)
tempImg = os.listdir(path)[1]
# fullPath = absp + "\\" + tempImg
# print (fullPath)
# print (clrDetect(fullPath))

# loop through directory
n = 0
while n < len(os.listdir(path))+1:
    img = os.listdir(path)[n]
    fullPath = absp + "\\" + img
    hue = clrDetect(fullPath)
    color = getColor(hue)
    fileNamer(path, img, color)
    n+=1


###
#TODO select directory
#TODO adjust file order used by os.listdir
#TODO more accurate colorthief
###