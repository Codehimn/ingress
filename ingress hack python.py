import os
os.system('taskkill /f /im adb.exe')

from ingress_functions import *

enviar_cmdshell("am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity\n")

limpieza_inventario()

# exit(0)
# import browser #recargar los portales
# read_portal_file()
# exit(0)

distancia_actual = 0
enviar_cmdshell('sleep 2.5\n')	

portal_actual	= select_first_portal()
print(portal_actual)

Hacks_efectuados=0
for x in range (300):
	hackear( portal_actual, distancia_actual,opcion =2)
	Hacks_efectuados+=1
	if Hacks_efectuados > 15 :
		Hacks_efectuados = 0
		limpieza_inventario()

	while 1: 
		portal_siguiente,distancia_siguiente 	= portal_siguiente_class( portal_actual ,min_lvl =3)
		if portal_siguiente != 0 : break
		print('esperando nuevo hack posible...')
		enviar_cmdshell('sleep 60\n')	
	distancia_actual = distancia_siguiente

	portal_actual = portal_siguiente
