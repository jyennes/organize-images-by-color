# organizae image folder by color
# detects dominant color in image 
# and groups it with similar color by renaming file

# import
from colorthief import ColorThief
from matplotlib import colors
import os
from tkinter import *
from tkinter import filedialog
from tqdm import tqdm

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
        domColor = '0'
    # Yellow
    elif hue >= 61 and hue <= 120: 
        domColor = '1'
    # Green
    elif hue >= 121 and hue <= 180: 
        domColor = '2'
    # Cyan
    elif hue >= 181 and hue <= 240: 
        domColor = '3'
    # Blue
    elif hue >= 241 and hue <= 300: 
        domColor = '4'
    # Magenta
    elif hue >= 301 and hue <= 360: 
        domColor = '5'

    return domColor

## rename files based on dominant color
def fileNamer(path, name, color):
    os.chdir(path)
    os.rename(name, (color + name))
# prepend to file names instead of replace
# os.rename('red.jpg', 'blue.jpg')

# select directory
root = Tk()
root.withdraw()
path = filedialog.askdirectory()
print (path)

# path = r"G:\Pictures\1080p"
absp = os.path.abspath(path)
tempImg = os.listdir(path)[1]
# fullPath = absp + "\\" + tempImg

# loop through directory
#n = 0
for n in tqdm(range(len(os.listdir(path)))):
    img = os.listdir(path)[n]
    fullPath = absp + "\\" + img
    hue = clrDetect(fullPath)
    color = getColor(hue)
    fileNamer(path, img, color)
    n+=1

###
#TODO more accurate colorthief
#TODO a way to undo changes
#TODO utilise hsv better: white/black, use othwr 2 parameters
###