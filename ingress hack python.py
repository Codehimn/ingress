# from subprocess import Popen, PIPE	# Import the module

import re 			#regularexpresion
import sys
from time import sleep
from datetime import timedelta, datetime
from subprocess import *
import pickle #para crear un txt con los portales
import random
import os
from ingress_functions import *

cmdshell = Popen(['cmd'], stdout=PIPE,stdin=PIPE,stderr=PIPE,universal_newlines=True)
while cmdshell.stdout.readline(1) != '>': pass #limpiamos el stdout :D

# getevent -lp /dev/input/event1
# ; am startservice --ez no_history true --ei lat 39583947 --ei long 2657041 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.4; am force-stop com.lexa.fakegpsdonate ;casa Gabor

# am startservice --ez no_history true --ei lat 39583947 --ei long 2657041 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.4; sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name='mock_location'" ; am force-stop com.lexa.fakegpsdonate ;casa Gabor
os.chdir(os.getcwd() )

if enviar_cmdshell(cmdshell,"adb shell\n") != "$":
	enviar_cmdshell(cmdshell,"adb kill-server\n")
	enviar_cmdshell(cmdshell,"adb shell\n")
enviar_cmdshell(cmdshell,"su\n")

# drop_items_bluestack(cmdshell,'X5', 250, accion = 'drop',key = '')
# drop_items_bluestack(cmdshell,'X4', 210, accion = 'drop',key = '')
# drop_items_bluestack(cmdshell,'R3', 214, accion = 'recicle',key = '')
# drop_items_bluestack(cmdshell,'X3', 415, accion = 'recicle',key = '')
# drop_items_bluestack(cmdshell,'X1', 5, accion = 'recicle',key = '')
# drop_items_bluestack(cmdshell,'X2', 160, accion = 'recicle',key = '')
# drop_items_bluestack(cmdshell,'C1', 32, accion = 'recicle',key = '')
# drop_items_bluestack(cmdshell,'C1', 32, accion = 'recicle',key = '')
# drop_items_bluestack(cmdshell,'X10', 10, accion = 'recicle',key = '')
# drop_items_bluestack(cmdshell,'U8', 80, accion = 'drop',key = 1)
# exit(0)


Hack_time=timedelta(seconds=310)
Hack_time_burn=timedelta(hours=4)
time_ini=datetime.now() - Hack_time

enviar_cmdshell(cmdshell,"am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity\n")

limpieza_inventario(cmdshell,check_output)
# exit(0)
import browser #recargar los portales

fo=open("portales.list",'r', encoding="UTF-8")	# print ('Name of the file jj: ' , fo.name)
# fo=open("portales palma mallorca.au3",'r', encoding="UTF-8")	# print ('Name of the file jj: ' , fo.name)

stri=fo.read();	# print ("Read String is : ", str)
fo.close()			# Close opend file

portales_arr		=[]

exp_titulo		= 'title="(.*?)"'
exp_portales 	= '\[(.*?),(.*?)\]'
exp_Level		= 'class="L([0-8])"'
exp_deploids 	= '%</td><td>(.*?)</td><td'

exp_all=exp_titulo+'.*?'+exp_portales+'.*?'+exp_Level+'.*?'+exp_deploids

matchObj=re.findall('Capture(.*?)help apGain', stri)
matchObj.sort()

for i in matchObj:	
	Portales=re.search(exp_all , i)
	if Portales:		portales_arr.append ( portal ( [Portales.group(1),Portales.group(2),Portales.group(3),Portales.group(4),Portales.group(5),time_ini,4]  )	)

distancia_actual = 10
enviar_cmdshell(cmdshell,'sleep 2.5\n')	


# if os.path.exists('outfile.txt'):
# 	output = open('outfile.txt', 'rb')
# 	for port_load in pickle.load(output):
# 		ind = [i for i, por in enumerate(portales_arr) if port_load.lat == por.lat and  port_load.lon == por.lon ][0]
# 		portales_arr[ind].ultimo_hack 		= port_load.ultimo_hack
# 		portales_arr[ind].hacks_restantes 	= port_load.hacks_restantes
# 	output.close()

portal_actual	= portales_arr[0]
Hacks_efectuados=0
while 1:

	hackear(cmdshell, portal_actual, distancia_actual,re,check_output,random)
	Hacks_efectuados+=1
	if Hacks_efectuados > 10 :
		Hacks_efectuados = 0
		limpieza_inventario(cmdshell,check_output)

	#reducir 1 en hackeables:
	ind = [i for i, x in enumerate(portales_arr) if x == portal_actual][0]
	portales_arr[ind].ultimo_hack = datetime.now()
	portales_arr[ind].hacks_restantes -=  1
	
	while 1: 
		portal_siguiente,distancia_siguiente 	= portal_siguiente_class( portal_actual ,portales_arr,datetime.now(),Hack_time - timedelta(seconds=10),Hack_time_burn,min_lvl =3)
		if portal_siguiente != 0 : break
		print('esperando nuevo hack posible...')
		enviar_cmdshell(cmdshell,'sleep 60\n')	
	distancia_actual = distancia_siguiente

	linea = ''
	# for y in portales_arr:		
	# 	for i in dir(y):
	# 		if  '_' not in str(i)[0] :
	# 			linea +=  i + ' = ' + str ( getattr(y, i) )	 + " , " 
	# 	linea += '\n'
	# print (linea) 
	
	portal_actual = portal_siguiente

	output = open('outfile.txt', 'wb')
	pickle.dump(portales_arr, output)
	output.close()
	# enviar_cmdshell(cmdshell,"exit\nexit\n")
	# out, err = cmdshell.communicate()

	# exit(0)


#funciones