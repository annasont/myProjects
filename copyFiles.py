'''copyFiles.py - copy all files from choosen foldertree with choosen extension to choosen destination.'''

import os, shutil

def copyFiles(folder, extension, destination):
    #Function that copies all files with choosen extension. 
    #First argument is a folder we want to search through
    #Second argument is extension of the files we want to copy
    #Third argument is a destination folder that we want to copy files to
    
    for foldername, subfolders, files in os.walk(folder):
        for filename in files:
            if filename.endswith(extension.lower()) or filename.endswith(extension.upper()):
                currentPath = os.path.abspath(os.path.join(foldername, filename))
                copyToPath = os.path.join(destination, filename)
                if not os.path.exists(copyToPath):
                    shutil.copyfile(currentPath, copyToPath)
                    print('File %s copied succesfully' % filename) 

if __name__ == '__main__':
    print('Enter path to the folder you want to search through:')
    folder = input()
    print('Enter extension you want to search for (including dot):')
    extension = input()
    print('Enter path to the destination folder:')
    destination = input()
    copyFiles(folder, extension, destination)



# check: dlaczego kilka razy przechodzi przez te same pliki? 
