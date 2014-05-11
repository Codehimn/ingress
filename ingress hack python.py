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

cmdshell = Popen(['cmd'], bufsize=1, stdout=PIPE,stdin=PIPE,stderr=PIPE,universal_newlines=True)

while cmdshell.stdout.readline(1) != '>': pass #limpiamos el stdout :D
try:  
	q
except NameError:	
	q = Queue()
	t = Thread(target=enqueue_output, args=(cmdshell.stdout, q))
	t.daemon = True # thread dies with the program
	t.start()


# getevent -lp /dev/input/event1
# ; am startservice --ez no_history true --ei lat 39583947 --ei long 2657041 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.4; am force-stop com.lexa.fakegpsdonate ;casa Gabor

# am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity;am startservice --ez no_history true --ei lat 39583947 --ei long 2657041 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.2; sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name='mock_location'" ; am force-stop com.lexa.fakegpsdonate ;casa Gabor
os.chdir(os.getcwd() )

if enviar_cmdshell(cmdshell,q,"adb shell\n") != "$":
	enviar_cmdshell(cmdshell,q,"adb kill-server\n")
	enviar_cmdshell(cmdshell,q,"adb shell\n")

enviar_cmdshell(cmdshell,q,"su\n")


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


Hack_time=timedelta(seconds=310)
Hack_time_burn=timedelta(hours=4)
time_ini=datetime.now() - Hack_time

enviar_cmdshell(cmdshell,q,"am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity\n")
# exit(0)
limpieza_inventario(cmdshell,q,check_output)

# import browser #recargar los portales

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
	#agrego o actualizo lista de portales
	if Portales:		portales_arr.append ( portal ([Portales.group(1),Portales.group(2),Portales.group(3),Portales.group(4),Portales.group(5),time_ini,4]  )	)
	# add_update_portals	()
	# if Portales:		portales_arr.append ( portal ({'nombre' : Portales.group(1),'lat' : int(float (Portales.group(2)) * 1000000),'lon' : int(float (Portales.group(3)) * 1000000),'lvl' : int(Portales.group(4)),'deployds' : int(Portales.group(5)),'ultimo_hack' : time_ini,'hacks_restantes' : 4}  )	)

distancia_actual = 10
enviar_cmdshell(cmdshell,q,'sleep 2.5\n')	

# 39.583265
# 2.657453

portal_actual	= portales_arr[0]
Hacks_efectuados=0
while 1:

	hackear(cmdshell,q, portal_actual, distancia_actual,re,check_output,random)
	Hacks_efectuados+=1
	if Hacks_efectuados > 10 :
		Hacks_efectuados = 0
		limpieza_inventario(cmdshell,q,check_output)

	#reducir 1 en hackeables:
	ind = [i for i, x in enumerate(portales_arr) if x == portal_actual][0]
	portales_arr[ind].ultimo_hack = datetime.now()
	portales_arr[ind].hacks_restantes -=  1
	
	while 1: 
		portal_siguiente,distancia_siguiente 	= portal_siguiente_class( portal_actual ,portales_arr,datetime.now(),Hack_time - timedelta(seconds=10),Hack_time_burn,min_lvl =3)
		if portal_siguiente != 0 : break
		print('esperando nuevo hack posible...')
		enviar_cmdshell(cmdshell,q,'sleep 60\n')	
	distancia_actual = distancia_siguiente

	portal_actual = portal_siguiente
