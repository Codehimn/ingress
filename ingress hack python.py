# from subprocess import Popen, PIPE	# Import the module

import re 			#regularexpresion
import sys
from time import sleep
from datetime import timedelta, datetime
from subprocess import *

import pickle

import os



# sleep(6000)

from ingress_functions import *

cmdshell = Popen(['cmd'], stdout=PIPE,stdin=PIPE,stderr=PIPE,universal_newlines=True)

enviar_cmdshell(cmdshell,"adb kill-server\n")
enviar_cmdshell(cmdshell,"adb shell\n")
enviar_cmdshell(cmdshell,"su\n")

enviar_cmdshell(cmdshell,"am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity\n")


Hack_time=timedelta(seconds=310)
time_ini=datetime.now() - Hack_time

fo=open("portales.list",'r', encoding="UTF-8")	# print ('Name of the file jj: ' , fo.name)

# fo=open("portales palma mallorca.au3",'r', encoding="UTF-8")	# print ('Name of the file jj: ' , fo.name)

stri=fo.read();	# print ("Read String is : ", str)
fo.close()			# Close opend file

portales_arr		=[]

exp_deploids 	= '%</td><td>(.*?)</td><td'
exp_portales 	= '\[(.*?),(.*?)\]'
exp_titulo		= 'title="(.*?)"'
exp_all=exp_titulo+'.*?'+exp_portales+'.*?'+exp_deploids

matchObj=re.findall('Capture(.*?)help apGain', stri)
matchObj.sort()

for i in matchObj:	
	Portales=re.search(exp_all , i)
	if Portales:
		portales_arr.append ( [Portales.group(1),Portales.group(2),Portales.group(3),time_ini,4]  	)
											#titulo,		   X,				Y,			,tiemp,  hacks

distancia_actual = 15
enviar_cmdshell(cmdshell,'sleep 2.5\n')	


if os.path.exists('outfile.txt'):
	output = open('outfile.txt', 'rb')
	portales_arr = pickle.load(output)
portales_arr =sorted(portales_arr)
portal_actual	= portal(portales_arr[0])

while 1:

	portal_siguiente,distancia_siguiente 	= portal_siguiente_class( portal_actual ,portales_arr,datetime.now(),Hack_time - timedelta(seconds=10))
	
	enviar_cmdshell(cmdshell,'am startservice --ez no_history true --ei lat {} --ei long {} -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate\n'.format(portal_actual.lat,portal_actual.lon))

	enviar_cmdshell(cmdshell,'sleep '+ str(distancia_actual + 1 ) + '\n' )
	distancia_actual = distancia_siguiente
	touch_x_y(cmdshell,12000,16500)#click en portal
	enviar_cmdshell(cmdshell,'sleep 2.5\n')		

	enviar_cmdshell(cmdshell,'sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\' " ;\n')		
	enviar_cmdshell(cmdshell,'am startservice --ez no_history true --ei lat {} --ei long {} -n com.lexa.fakegpsdonate/.FakeGPSService\n'.format(portal_actual.lat,portal_actual.lon))
	
	for i in range(10):
		touch_x_y(cmdshell,21560, 30440)#hack
		enviar_cmdshell(cmdshell,'sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\' " ;\n' , '')							
	enviar_cmdshell(cmdshell,'am force-stop com.lexa.fakegpsdonate\n')
	enviar_cmdshell(cmdshell,'sleep 1\n')
	touch_x_y(cmdshell,32768, 5) #abajo de hack
	enviar_cmdshell(cmdshell,'sleep 1\n')
	touch_x_y(cmdshell,32768, 5) #abajo de hack

	# for i in portales_arr:
	# 	print(i)
	
	ind = [i for i, x in enumerate(portales_arr) if x[0] == portal_actual.nombre][0]
	portales_arr[ind][3] = datetime.now()
	portales_arr[ind][4] = portales_arr[ind][4] - 1
	

	portal_actual = portal_siguiente

	output = open('outfile.txt', 'wb')
	pickle.dump(portales_arr, output)


	# enviar_cmdshell(cmdshell,"exit\nexit\n")
	# out, err = cmdshell.communicate()

	# exit(0)


#funciones

