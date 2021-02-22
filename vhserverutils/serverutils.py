#!python3
import shutil
from datetime import datetime
from os import path as ospath
from pathlib import Path


class backup():
    """Utilities for backing up the server and cleaning the directory."""

    def __init__(self):
        pass

    def checkDirSize(self, dirpath, size):
        """Returns True if directory is greater in size than value provided."""

        basepath = Path(dirpath)
        return sum(ospath.getsize(f) for f in basepath.glob('**/*') if f.is_file()) > size

    def getoldest(self, dirpath):
        """Returns the oldest file in the supplied path."""
        return min([f for f in Path(dirpath).glob('**/*')], key=ospath.getctime)

    def archive(self, worldPath, backupPath):
        """Archives worldpath into backupPath"""
        zipName = ospath.join(backupPath,'VHworlds' + datetime.now().strftime('%Y%m%d%H%M%S'))
        shutil.make_archive(zipName, 'zip', base_dir=worldPath)

    def deleteold(self, backupPath, maxsize):
        """Checks current size of backupPath, and deletes oldest
        files until it is smaller than maxsize"""

        maxarch = maxsize * 1048576
        oldestfile = (backupPath)
        if self.checkDirSize(backupPath, maxarch):
            while self.checkDirSize(backupPath, maxarch):
                oldestfile = self.getoldest(backupPath)
                Path(oldestfile).unlink()
