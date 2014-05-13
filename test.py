from time import sleep
from subprocess import *

for i in range (1,30):
	x=str(i)
	check_output('adb shell screencap -p /sdcard/screen{}.png'.format(x).split(' ') )
	check_output('adb pull /sdcard/screen{}.png C:\\Users\\Codehimn\\Dropbox\\ingress\\img'.format(x).split(' ') )
	check_output('adb shell rm /sdcard/screen{}.png'.format(x).split(' ') )
	check_output( 'ImageMagick-6.8.9-0\\Convert C:\\Users\\Codehimn\\Dropbox\\ingress\\img\\screen{}.png -rotate -90 C:\\Users\\Codehimn\\Dropbox\\ingress\\img\\screen{}.png'.format(x,x).split(' ') )



# 	{'lat': 39560323, 'lvl': 2, 'deployds': 4, 'ultimo_hack': '2014-05-11 16:24:43.567394', 'nombre': 'Font de sa Plaça', 'hacks_restantes': 3, 'lon': 2673577}
# [Cancelled]