'''replace.py: renames files in given directory. User must specify which character/characters needs to be changed.'''
import os

def showToUser():
    print('(Press Ctrl + C to stop the program.)\nI want to replace following characters:')
    characters = input()
    print('with:')
    newCharacters = input()
    return(characters, newCharacters)

def replace(text):
    return text.replace(characters, newCharacters)

def rename(path, currentName, newName):
    sourceFile = os.path.join(path, currentName)
    renamedFile = os.path.join(path, newName)
    os.rename(sourceFile, renamedFile)
    print('Name: %-28s changed to: %s' % (currentName, newName))

print('I want to make changes in file names in this folder:')
path = input()
characters, newCharacters = showToUser()

try:
    while True:
        for filename in os.listdir(path):
            if characters in filename:
                newName = replace(filename)
                rename(path, filename, newName)
        characters, newCharacters = showToUser()
except FileNotFoundError:
    print('Folder not found. Please try again.')
except KeyboardInterrupt:
    print('Done')
