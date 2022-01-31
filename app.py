#imports
import shutil
import os
from tkinter import *
from tkinter import filedialog

def openFile(): # gets called when a user wants to select a file to backup
    global filepath
    filepath = filedialog.askdirectory()
    label = Label(text=f'Selected File To Backup: {filepath}')
    label.pack()

def openBackupDestination(): # gets called when a user wants to select where they want to store the backup file
    global backupDestination
    backupDestination = filedialog.askdirectory()
    label = Label(text=f'Selected Backup File Destination: {backupDestination}')
    label.pack()

def configFileLocation(): # configs the current location of the program to get ready to store the backup file
    global backupfileLocation
    global backupFileName
    backupFileName = 'BackUpFile'
    backupFileName = f'\{backupFileName}'
    backupfileLocation = os.getcwd()
    label = Label(text=f'Config Complete(program directory): {backupfileLocation}')
    backupfileLocation = backupfileLocation + backupFileName
    label.pack()

def getBackupFile(): # gets the location of the backup file and copies it to the programs directory
    if (os.path.exists(backupfileLocation)): # if the backupFileLocation already exists, it removes it
        shutil.rmtree(backupfileLocation)
    
    shutil.copytree(filepath, backupfileLocation) # moves the file to the programs directory

def moveSourceFileToDestination(): # moves the backup file from the programs directory to the users backup file destination
    src = backupfileLocation
    target = backupDestination
    path = backupDestination + backupFileName
    if (os.path.exists(path)): # if the path already exists, remove it.
        shutil.rmtree(path)
    shutil.move(src, target) # move the backupfile from program directory to the user file destination

def backupFile(): # calls the functions to backup the file
    getBackupFile()
    moveSourceFileToDestination()


# the user interface
window = Tk()
window.geometry('700x200')
configBtn = Button(text='Config', command=configFileLocation)
SelectFileBtn = Button(text='Select File To Backup', command=openFile)
SelectFileDestinationBtn = Button(text='Select Backup Destination', command=openBackupDestination)
BackupFileBtn = Button(text="Backup File", command=backupFile)
configBtn.pack()
SelectFileBtn.pack()
SelectFileDestinationBtn.pack()
BackupFileBtn.pack()
window.mainloop()