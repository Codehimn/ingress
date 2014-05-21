
from subprocess import *
from time import sleep
import win32com.client

import glob, os

oShell = win32com.client.Dispatch("Wscript.Shell")
dirdocs = oShell.SpecialFolders("MyDocuments")
dirdocs = str(dirdocs) + '\\img_temp'

# while 1:
# 	os.system('taskkill /f /im adb.exe')
# 	filelist = glob.glob(dirdocs + '\\*.*')
# 	for f in filelist:
# 		os.remove(f)

# 	cmdshell = check_output(['py' , 'ingress hack python.py'] )

# 	# data = cmdshell.stdout.readlines()
# 	# for line in data:
# 	# 	print (line)
# 	print ('repite ')
# 	sleep(10)


from time import time
for x in range (1):
	start = time()
	# check_output('ImageMagick-6.8.9-0\\convert C:\\Users\\Codehimn\\Documents\\img_temp\\screen_test.png -crop 1x1+1087+715 -threshold 50% txt:')
	end = time()
	elapsed = end - start
	print(elapsed)


print(''.join(sorted('21373216318abc')))