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
Hack_time_burn=timedelta(hours=4)
time_ini=datetime.now() - Hack_time

# fo=open("portales.list",'r', encoding="UTF-8")	# print ('Name of the file jj: ' , fo.name)

fo=open("portales palma mallorca.au3",'r', encoding="UTF-8")	# print ('Name of the file jj: ' , fo.name)

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
	if Portales:		portales_arr.append ( portal ( [Portales.group(1),Portales.group(2),Portales.group(3),time_ini,4]  )	)
															#titulo,		   X,				Y,			,tiemp,  hacks
distancia_actual = 15
enviar_cmdshell(cmdshell,'sleep 2.5\n')	


# if os.path.exists('outfile.txt'):
# 	output = open('outfile.txt', 'rb')
# 	portales_arr = pickle.load(output)

# for i in portales_arr:
	# if not i.hacks_restantes:	
# 	print(i.nombre + ' ' + str(i.hacks_restantes))
# exit(0)

portal_actual	= portales_arr[0]
while 1:

	hackear(cmdshell, portal_actual, distancia_actual)
	#reducir 1 en hackeables:
	ind = [i for i, x in enumerate(portales_arr) if x.nombre == portal_actual.nombre][0]
	portales_arr[ind].ultimo_hack = datetime.now()
	portales_arr[ind].hacks_restantes -=  1

	portal_siguiente,distancia_siguiente 	= portal_siguiente_class( portal_actual ,portales_arr,datetime.now(),Hack_time - timedelta(seconds=10),Hack_time_burn)
	while portal_siguiente == 0: 
		print('esperando nuevo hack posible...')
		enviar_cmdshell(cmdshell,'sleep 60\n')	
		portal_siguiente,distancia_siguiente 	= portal_siguiente_class( portal_actual ,portales_arr,datetime.now(),Hack_time - timedelta(seconds=10),Hack_time_burn)
		continue
	distancia_actual = distancia_siguiente

	linea = ''
	for y in portales_arr:		
		for i in dir(y):
			if  '_' not in str(i)[0] :
				linea +=  i + ' = ' + str ( getattr(y, i) )	 + " , " 
		linea += '\n'
	print (linea) 
	
	portal_actual = portal_siguiente

	output = open('outfile.txt', 'wb')
	pickle.dump(portales_arr, output)

	# enviar_cmdshell(cmdshell,"exit\nexit\n")
	# out, err = cmdshell.communicate()

	# exit(0)


#funciones