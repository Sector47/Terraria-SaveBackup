import shutil
import os
import datetime
from distutils.dir_util import copy_tree
from pathlib import Path

# backup Worlds. 

# set the file locations of current saves and backup location to variables.
src = os.path.expanduser(r'~\Documents\My Games\Terraria\Worlds\\')
des = os.path.expanduser(r'~\Documents\My Games\Terraria\WorldBackups' + datetime.datetime.now().strftime("\%m-%d-%Y %I%M %p"))

# make the new folders for backing up files
FolderWorldBackup = os.path.expanduser(r'~\Documents\My Games\Terraria\WorldBackups\\')
FolderPlayerBackup = os.path.expanduser(r'~\Documents\My Games\Terraria\PlayerBackups\\')

if not os.path.exists(FolderPlayerBackup):
	os.mkdir(FolderPlayerBackup)
if not os.path.exists(FolderWorldBackup):
	os.mkdir(FolderWorldBackup)


print(des)
files = os.listdir(src)

# make a new directory for backups if no such folder exists.
if not os.path.exists(des):
	os.mkdir(des)

# Copy each file in worlds to new directory.
copy_tree(src, des)

# backup Players

# set the file locations of current saves and backup location to variables.
src = os.path.expanduser(r'~\Documents\My Games\Terraria\Players\\')
des = os.path.expanduser(r'~\Documents\My Games\Terraria\PlayerBackups' + datetime.datetime.now().strftime("\%m-%d-%Y %I%M %p"))
print(des)
files = os.listdir(src)

# make a new directory for backups if no such folder exits.
if not os.path.exists(des):
	os.mkdir(des)

# Copy each file in Players to new directory.
copy_tree(src, des)
