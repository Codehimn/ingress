import os
# os.remove('portal_list.db')
# getevent -lp /dev/input/event1
os.system('taskkill /f /im adb.exe')

from ingress_functions import *
import sys


# unload_capsule(150)
# exit(0)
if len (sys.argv) > 1:
	if sys.argv[1] == 'casa':
		enviar_cmdshell("am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity\n")
		enviar_cmdshell('am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity;am startservice --ez no_history true --ei lat 39583947 --ei long 2657041 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.2; sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\'" ; am force-stop com.lexa.fakegpsdonate \n ;casa Gabor')
		exit(0)
	elif sys.argv[1] == 'recargar_portales':
		# import browser #recargar los portales
		read_portal_file()
		exit(0)
	elif 1 == 2:
		hackear( portal_actual, distancia_actual,opcion =2)
		while not deployd(portal_actual):
				pass




# limpieza_inventario()
# exit(0)
# getevent -lp /dev/input/event1


distancia_actual = 0
enviar_cmdshell('sleep 2.5\n')	

#el_portal = portal()
#el_portal.select_first_portal()
#print(el_portal.lat)
#print(el_portal.lon)

#exit(0)

portal_actual	= select_first_portal()
print(portal_actual)


hackear( portal_actual, distancia_actual,opcion =2)
while not deployd(portal_actual):
		pass


Hacks_efectuados=0
for x in range (300):


	Hacks_efectuados+=1
	if Hacks_efectuados > 15 :
		Hacks_efectuados = 0
		# limpieza_inventario()

	while 1: 
		# portal_siguiente,distancia_siguiente 	= portal_siguiente_class( portal_actual ,min_lvl =0,team_distinct = 'RES',max_deployds=7)
		portal_siguiente,distancia_siguiente 	= portal_siguiente_class( portal_actual ,min_lvl =2)
		if portal_siguiente != 0 : break
		print('esperando nuevo hack posible...')
		enviar_cmdshell('sleep 60\n')	
	distancia_actual = distancia_siguiente

	portal_actual = portal_siguiente

	hackear( portal_actual, distancia_actual,opcion =2)
	while not deployd(portal_actual):
			pass
