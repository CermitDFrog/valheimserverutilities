#!python3
import shutil
from datetime import datetime
from os import path
from pathlib import Path
import json


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

oldestfile = (config["backupPath"])
if checkDirSize(config["backupPath"], 1073741824):
    while checkDirSize(config["backupPath"], 1073741824):
        oldestfile = getoldest(config["backupPath"])
        Path(oldestfile).unlink()
