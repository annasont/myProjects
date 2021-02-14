import os, shutil
from PIL import Image

def readWidthAndHeight(path, filename):
    imagePath = os.path.join(path, filename)
    image = Image.open(imagePath)
    sourceImageWidth, sourceImageHeight = image.size
    return sourceImageWidth, sourceImageHeight

def checkFiles(path, widthInPrint, heightInPrint, dpi):
    okForPrint = []
    notOkForPrint = []  
    for filename in os.listdir(path):
        if filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.png') or filename.endswith('.PNG'):
            sourceImageWidth, sourceImageHeight = readWidthAndHeight(path, filename)
            minWidth = round(widthInPrint / 2.54 * dpi)
            minHeight = round(heightInPrint / 2.54 * dpi)
            if sourceImageWidth >= minWidth and sourceImageHeight >= minHeight:
                okForPrint.append(filename)
            else:
                maxWidth = round(sourceImageWidth / dpi * 2.54)
                maxHeight = round(sourceImageHeight / dpi * 2.54)
                text = '%s: max width of %s cm; max height of %s cm' % (filename, maxWidth, maxHeight)
                notOkForPrint.append(text)
    print('\nFiles ok for print:')
    for filename in okForPrint:
        print(filename)
    print('\nNot ok for print. In order to print in %s dpi use following maximum sizes:' % dpi)
    for item in notOkForPrint:
        print(item)

    return okForPrint

def moveFilesOkForPrint():
    okForPrint = checkFiles(path, widthInPrint, heightInPrint, dpi)
    newFolder = os.path.join(path, "OkForPrint")
    os.makedirs(newFolder, exist_ok=True)
    
    for filename in okForPrint:
        source = os.path.join(path, filename)
        destination = os.path.join(newFolder, filename)
        shutil.move(source, destination)

    print('\nFiles big enough for print moved to the new folder "OkForPrint".')

path = r'C:\Users\annaso\Desktop\aktualne\test\focie'
path2 = r''
widthInPrint = 10
heightInPrint = 10
dpi = 300

checkFiles(path, widthInPrint, heightInPrint, dpi)

#moveFilesOkForPrint()
