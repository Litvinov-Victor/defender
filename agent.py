import os
import logging
import wget
import time

starttime=time.time()
logging.basicConfig(filename="logs/main.log", level=logging.INFO)
dataFileHost = 'https://dev.solvers.group/defender/hosts'
dataFileNameHost = 'C:\WINDOWS\system32\drivers\etc\hosts'


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

    time.sleep(600.0 - ((time.time() - starttime) % 600.0))
