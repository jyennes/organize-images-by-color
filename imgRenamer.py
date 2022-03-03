# organizae image folder by color
# detects dominant color in image 
# and groups it with similar color by renaming file

# import
from colorthief import ColorThief
from matplotlib import colors
import os

def clrDetect(image):
    # Detect dominant color from image
    ct = ColorThief(image)
    dominant_color = ct.get_color(quality=10)
    print ("Dominant color: ", dominant_color)

    ## convert RGB to HSV
    # scale RGB format from 255 to 1
    rgb = list()
    for x in range(len(dominant_color)):
        rgb.append(dominant_color[x] / 255)  
    print ("RGB: ", rgb)

    hsv = colors.rgb_to_hsv(rgb)
    # scale hue value to 360
    hsv[0] = hsv[0] * 360
    print ("HSV: ", hsv)

# test output
# image = 'blue.jpg'
# clrDetect(image)

# Create groups by hue range
def getColor(hue):
    # Red
    if hue >= 0 and hue <= 60: 
        domColor = 'red'
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

#TODO rename files based on dominant color
# prepend to file names instead of replace
# os.rename('red.jpg', 'blue.jpg')


