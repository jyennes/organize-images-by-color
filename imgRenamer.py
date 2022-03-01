# organizae image folder by color
# detects dominant color in image 
# and groups it with similar color by renaming file

# import
from colorthief import ColorThief
from matplotlib import colors

# Detect dominant color from image
ct = ColorThief('redcircle.jpg')
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


#TODO rename files based on dominant color
# https://docs.microsoft.com/en-us/windows/python/scripting