'''replaceNorwegianLetters.py replaces Norwegian letters æ, ø, å, Æ, Ø, Å with ae, o, a, AE, O, A
in all files and subfolders in given folder tree. '''
import os

def replaceLowerØ(text):
    return text.replace('ø', 'o')

def replaceUpperØ(text):
    return text.replace('Ø', 'O')

def replaceLowerÆ(text):
    return text.replace('æ', 'ae')

def replaceUpperÆ(text):
    return text.replace('Æ', 'AE')

def replaceLowerÅ(text):
    return text.replace('å', 'a')

def replaceUpperÅ(text):
    return text.replace('Å', 'A')

def replaceNorwegianLetters(text):
    return replaceUpperÅ(replaceUpperÆ(replaceUpperØ(replaceLowerÅ(replaceLowerÆ(replaceLowerØ(text))))))

def replaceSubfoldername(foldername, subfolder, newName):
    sourceFile = os.path.join(foldername, subfolder)
    renamedFile = os.path.join(foldername, newName)
    os.rename(sourceFile, renamedFile)
    print('Foldername: %-28s changed to: %s' % (subfolder, newName))

def replaceFilename(foldername, filename, newName):
    sourceFile = os.path.join(foldername, filename)
    renamedFile = os.path.join(foldername, newName)
    os.rename(sourceFile, renamedFile)
    print('Filename: %-30s changed to: %s' % (filename, newName))  

def renameFolders(folderTree):
    for foldername, subfolders, files in os.walk(folderTree, topdown=False):
        for subfolder in subfolders:
            if 'ø' in subfolder or 'æ' in subfolder or 'å' in subfolder or 'Ø' in subfolder or 'Æ' in subfolder or 'Å' in subfolder:
                newName = replaceNorwegianLetters(subfolder)
                replaceSubfoldername(foldername, subfolder, newName)

def renameFiles(folderTree, topdown=False):
    for foldername, subfolders, files in os.walk(folderTree):
        for filename in files:
            if 'ø' in filename or 'æ' in filename or 'å' in filename or 'Ø' in filename or 'Æ' in filename or 'Å' in filename:
                newName = replaceNorwegianLetters(filename)
                replaceFilename(foldername, filename, newName)

if __name__ == "__main__":
    print('Insert path to the folder tree in which you want to replace norwegian letters:')
    folderTree = input()           
    renameFolders(folderTree)
    renameFiles(folderTree)



