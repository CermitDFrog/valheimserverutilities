#!python3
import shutil
from datetime import datetime
from os import path
from pathlib import Path
import json

scriptDescription = """Archives worlds found in specified worlds directory of config into a zipfile named VHworldsyyyymmddhhmmss in the specified directory in the config file.
After archiving is complete, checks the size of the directory versus the maxBackupSize. If the directory size is greater than the specified max, 
the script starts deleting the oldest files in the archive until the file size is under max."""


def readconfig(config):
    with open(config, 'r') as f:
        return json.load(f)


def checkDirSize(dirpath, size):
    '''Returns True if directory is greater in size than value provided.'''

    basepath = Path(dirpath)
    return sum(path.getsize(f) for f in basepath.glob('**/*') if f.is_file()) > size


def getoldest(dirpath):
    '''Returns the oldest file in the supplied path.'''
    return min([f for f in Path(dirpath).glob('**/*')], key=path.getctime)


config = readconfig('config.json')
zipName = path.join(config["backupPath"],'VHworlds' + datetime.now().strftime('%Y%m%d%H%M%S'))
shutil.make_archive(zipName, 'zip', base_dir=config["worldPath"])
maxarch = config["maxBackupSize"] * 1048576

oldestfile = (config["backupPath"])
if checkDirSize(config["backupPath"], maxarch):
    while checkDirSize(config["backupPath"], maxarch):
        oldestfile = getoldest(config["backupPath"])
        Path(oldestfile).unlink()
