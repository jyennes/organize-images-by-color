# All this does is delete the first character in a filename if it is a digit between 0-5.
# WARNING: This does not check for any change history, it will simply just delete the character.

import os
from tkinter import *
from tkinter import filedialog
from tqdm import tqdm

# delete first character
def fileNamer(path, name):
    os.chdir(path)
    os.rename(name, name[1:])

# select directory
root = Tk()
root.withdraw()
path = filedialog.askdirectory()
print (path)

# main
for n in tqdm(range(len(os.listdir(path)))):
    img = os.listdir(path)[n]
    if img.endswith((r'.png', r'.jpg', r'.bmp')) == False:
        continue
    if img.startswith(('0', '1', '2', '3', '4', '5')) == True:
        fileNamer(path, img)
