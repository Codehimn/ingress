# from subprocess import Popen, PIPE	# Import the module

import re 			#regularexpresion
import sys
from time import sleep
from datetime import timedelta, datetime
from subprocess import *

# sleep(6000)

from ingress_functions import *

cmdshell = Popen(['cmd'], stdout=PIPE,stdin=PIPE,stderr=PIPE,universal_newlines=True)

enviar_cmdshell(cmdshell,"adb kill-server\n")
enviar_cmdshell(cmdshell,"adb shell\n")
enviar_cmdshell(cmdshell,"su\n")
enviar_cmdshell(cmdshell,"am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity\n")


Hack_time=timedelta(seconds=310)
time_ini=datetime.now() - Hack_time

fo=open("portales palma mallorca.au3",'r', encoding="UTF-8")	# print ('Name of the file jj: ' , fo.name)

stri=fo.read();	# print ("Read String is : ", str)
fo.close()			# Close opend file

portales_dict		={}
portales_lst_todos	=[]

exp_deploids 	= '%</td><td>(.*?)</td><td'
exp_portales 	= '\[(.*?),(.*?)\]'
exp_titulo		= 'title="(.*?)"'
exp_all=exp_titulo+'.*?'+exp_portales+'.*?'+exp_deploids

matchObj=re.findall('Capture(.*?)help apGain', stri)
matchObj.sort()

for i in matchObj:	
	Portales=re.search(exp_all , i)
	if Portales:
		portales_dict[Portales.group(1)]=[Portales.group(1),Portales.group(2),Portales.group(3),time_ini,4]  	
											#titulo,		   X,				Y,			,tiemp,  hacks
		portales_lst_todos.append( [Portales.group(1),Portales.group(2),Portales.group(3),time_ini,4]  )

distancia_actual = 15
enviar_cmdshell(cmdshell,'sleep 2.5\n')	
for x in sorted(portales_dict):

	portal_actual		= portal(portales_dict[x])
	portal_siguiente 	= portal_siguiente_class( portales_dict[x],portales_lst_todos,datetime.now(),Hack_time - timedelta(seconds=10))
	
	# enviar_cmdshell(cmdshell,'am startservice --ez no_history true --ei lat {} --ei long {} -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate\n'.format(portal_siguiente.portal.lat,portal_siguiente.portal.lon))
	enviar_cmdshell(cmdshell,'am startservice --ez no_history true --ei lat 39583947 --ei long 2657041 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.4; am force-stop com.lexa.fakegpsdonate \n')

	DropItems_bluestack(cmdshell,"U8", 228,'drop',1) #llaves

	exit(0)

	enviar_cmdshell(cmdshell,'sleep '+ str(distancia_actual + 1 ) + '\n' )
	distancia_actual = portal_siguiente.distancia
	touch_x_y(cmdshell,12000,16500)#click en portal
	enviar_cmdshell(cmdshell,'sleep 2.5\n')	
	
	# adb.mock_location(0)

	enviar_cmdshell(cmdshell,'sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\' " ;\n')		
	enviar_cmdshell(cmdshell,'am startservice --ez no_history true --ei lat {} --ei long {} -n com.lexa.fakegpsdonate/.FakeGPSService\n'.format(portal_siguiente.portal.lat,portal_siguiente.portal.lon))
	
	for i in range(10):
		enviar_cmdshell(cmdshell,'sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\' " ;\n' , '')					
		touch_x_y(cmdshell,21560, 30440)#hack
	enviar_cmdshell(cmdshell,'am force-stop com.lexa.fakegpsdonate\n')
	enviar_cmdshell(cmdshell,'sleep 1\n')
	touch_x_y(cmdshell,4360, 26655) #OK en portal
	touch_x_y(cmdshell,3000, 15598) #abajo de hack
	touch_x_y(cmdshell,3000, 15598) #abajo de hack

	portal_actual.ultimo_hack = datetime.now()
	portal_actual.hacks_restantes = portal_actual.hacks_restantes - 1

	# enviar_cmdshell(cmdshell,"exit\nexit\n")
	# out, err = cmdshell.communicate()

	# print(out)

	# exit(0)


#funciones

