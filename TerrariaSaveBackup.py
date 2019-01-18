import shutil
import os
import datetime
from pathlib import Path
src = os.path.expanduser(r'~\Documents\My Games\Terraria\ModLoader\Worlds\\')
des = os.path.expanduser(r'~\Documents\My Games\Terraria\ModLoader\Backups' + datetime.datetime.now().strftime("\%m-%d-%Y %I%M %p"))
print(des)
files = os.listdir(src)
if not os.path.exists(des):
	os.mkdir(des)
for eachFile in files:
	shutil.copy(src + eachFile, des)
