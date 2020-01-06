import os
import logging
import wget
import time

starttime=time.time()
logging.basicConfig(filename="logs/main.log", level=logging.INFO)
dataFileHost = 'https://dev.solvers.group/ocenkulator/hosts'
dataFileNameHost = 'hosts'

def passage(file_name, folder):
    for element in os.scandir(folder):
        if element.is_file():
            if element.name == file_name:
                yield folder
        else:
            yield from passage(file_name, element.path)

def loadFile():
    if os.access(dataFileNameHost, os.F_OK) == True:
        return True
    else:
        return False

while True:
    if loadFile() == False:
        filename = wget.download(dataFileHost)
        os.rename(filename, u'' + os.getcwd() + '/' + filename)
    else:
        os.remove(dataFileNameHost)
        filename = wget.download(dataFileHost)
        os.rename(filename, u'' + os.getcwd() + '/' + filename)

    print('hosts', os.getcwd())
    time.sleep(600.0 - ((time.time() - starttime) % 600.0))
