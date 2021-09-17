'''checkDpi.py checks if images in given location are big enough for print (or other purposes).'''

import os, shutil
from PIL import Image

def readWidthAndHeight(path, filename):
    # Checks images with and height in pixels
    imagePath = os.path.join(path, filename)
    image = Image.open(imagePath)
    sourceImageWidth, sourceImageHeight = image.size
    return sourceImageWidth, sourceImageHeight

def checkFiles(path, widthInPrint, heightInPrint, dpi):
    # path: location of images you want to check
    # widthInPrint: expected width of an image in printed material (in centimeters)
    # heightInPrint: expected height of an image in printed material (in centimeters)
    # dpi: expected value of dpi (use 300 dpi for printed matierials)
    okForPrint = []
    notOkForPrint = []  
    for filename in os.listdir(path):
        # checking only files in .jpg and .png format:
        if filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.png') or filename.endswith('.PNG'):
            sourceImageWidth, sourceImageHeight = readWidthAndHeight(path, filename)
            # calculating minimum width and height (in pixels) for given size of image in printed material: 
            minWidth = round(widthInPrint / 2.54 * dpi)
            minHeight = round(heightInPrint / 2.54 * dpi)
            # checking if image file is big enough to print it in given quality and given size:
            if sourceImageWidth >= minWidth and sourceImageHeight >= minHeight:
                okForPrint.append(filename)
            else:
                # if image not big enough, calculating maximum size of an image in print, in order to maintain given quality.
                maxWidth = round(sourceImageWidth / dpi * 2.54)
                maxHeight = round(sourceImageHeight / dpi * 2.54)
                text = f'{filename}: max width of {maxWidth} cm; max height of {maxHeight} cm'
                notOkForPrint.append(text)
    
    if notOkForPrint != []:
        print(f'\nIn order to print following images in {dpi} dpi use following maximum sizes:')
        for item in notOkForPrint:
            print(item)
    
    if okForPrint != []:
        print('\nFiles ok for print:')
        for filename in okForPrint:
            print(filename)

    return okForPrint

def moveFilesOkForPrint():
    # Creates folder "OkForPrint" and moves files that match requirements to this folder 
    okForPrint = checkFiles(path, width, height, dpi)
    newFolder = os.path.join(path, "OkForPrint")
    os.makedirs(newFolder, exist_ok=True)
    
    for filename in okForPrint:
        source = os.path.join(path, filename)
        destination = os.path.join(newFolder, filename)
        shutil.move(source, destination)

    print('\nFiles big enough for print moved to the new folder "OkForPrint".')


# moveFilesOkForPrint()

if __name__ == "__main__":
    print('Path to the folder with images:')
    path = input()
    print('Width of an image in cm in a target place:')
    width = int(input())
    print('Height of an image in cm in a target place:')
    height = int(input())
    print('Dpi value (e.g. 300 for printed materials):')
    dpi = int(input())
    okForPrint = checkFiles(path, width, height, dpi)

    if okForPrint != []:
        print('Do you want to move OK images to the new folder? Type "Yes" or "No":')
        answer = input().lower()
        if answer == 'yes':
            moveFilesOkForPrint()
            print('Files moved successfully')
        elif answer == 'no':
            print("Ok, we're done!")
        else:
            print('Something went wrong. Try again.')

