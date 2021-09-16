# myProjects

## About
A set of console programs automating repeatable tasks such as bulk renaming files in given directory, checking properties of images to determine if they are good enough for print, moving certain files to chosen directory, assigning tasks from excel spreadsheet, etc.

## Examples

### replaceNorwegianLetters.py 

replaces Norwegian letters æ, ø, å, Æ, Ø, Å with ae, o, a, AE, O, A in all files and subfolders in given folder tree.
Open terminal in the same directory as the program. Type `python replaceNorwegianLetters.py`. Follow instruction on your screen.

### checkDpi.py

checks if images in given location are big enough for print (or other purposes).

Open file in your IDE. Scroll down and set variables:

`path`: to location of images, you want to check

`width` and `height`: to how many cm will images have in the target product

`dpi`: to choose dpi value (e.g. 300 for print, 72 for digital publishing)

Uncomment the last line `moveFilesOkForPrint()` if you want to move images matching criteria to the new folder.

Run program in terminal.
