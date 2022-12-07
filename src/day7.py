from __future__ import annotations
from dataclasses import dataclass
from typing import List
import sys

@dataclass
class Folder:
    name: str
    subFolders: List["Folder"]
    files: List["File"]
    parentFolder: Folder or None
    
        
@dataclass
class File:
    name: str
    size: int
    

def task_1():
    with open("resources/inputFiles/input7.txt") as f:
        lines = f.readlines()
        map(lambda el: el.replace("\n", ""), lines)
        
        root = buildFileTree(lines)
        folderSizes = calculateFolderSize(root)
        
        overallSize = 0
        for _, size in folderSizes.items():
            if size <= 100000:
                overallSize += size
        
        return overallSize

        
def buildFileTree(lines):
    currentFolder = None
    for line in lines:
        line = str(line)
        line.replace("\n", "")
        if line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            pass
        elif line.startswith("$ cd .."):
            currentFolder = currentFolder.parentFolder
        elif line.startswith("$ cd"):
            folderName = line.replace("$ cd", "").replace(" ", "").replace("\n", "")
            if currentFolder is not None:
                newFolder = Folder(name=folderName, files=list(), parentFolder=currentFolder, subFolders=list())
                newFolder.name = buildName(currentFolder, newFolder)
                currentFolder.subFolders.append(newFolder)
                currentFolder = newFolder
            else:
                currentFolder = Folder(name=folderName, subFolders=list(), files=list(), parentFolder=None)
        else:
            fileSize, fileName = line.replace("\n", "").split(" ")
            currentFolder.files.append(File(fileName.replace(" ", ""), int(fileSize)))

    while currentFolder.name != "/":
        currentFolder = currentFolder.parentFolder
    return currentFolder


def calculateFolderSize(folder: Folder) -> dict:
    folders = {}
    size = sumFiles(folder)
    for childFolder in folder.subFolders:
        folders = folders | calculateFolderSize(folder=childFolder)
        size += folders[childFolder.name]
    folders[folder.name] = size
    return folders


def sumFiles(folder: Folder) -> int:
    size = 0
    for file in folder.files:
        size += file.size
    return size

def buildName(parentFolder: Folder, folder: Folder) -> str:
    return parentFolder.name + "-" + folder.name
            

def task_2():
    with open("resources/inputFiles/input7.txt") as f:
        lines = f.readlines()
        map(lambda el: el.replace("\n", ""), lines)
        
        root = buildFileTree(lines)
        folderSizes = calculateFolderSize(root)
        
        overallSpace = 70000000
        updateSpace = 30000000
        
        usedSpace = folderSizes["/"]
        freeSpace = overallSpace - usedSpace
        neededSpace = updateSpace - freeSpace
        
        smallestSpace = sys.maxsize
        for _, space in folderSizes.items():
            if space >= neededSpace:
                if space < smallestSpace:
                    smallestSpace = space
             
        return smallestSpace
        

print("Task 1:", task_1())
print("Task 2:", task_2())