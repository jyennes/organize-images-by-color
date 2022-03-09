# Organize Images by Color
Detects dominant color of images and renames them to fit color group

Every image file in your selected directory will have their names prepended with a number corresponding to their color group

Red: 0
Yellow: 1
Green: 2
Cyan: 3
Blue: 4
Magenta: 5

# Usage
Run executable file

select directory of images you want to organize

# Warning 

Can only be reversed manually or by using undoChanges.exe

## undoChanges.exe
All this does is delete the first character in a filename if it is a digit between 0-5.

This does not check for any change history, it will simply delete the first character.

