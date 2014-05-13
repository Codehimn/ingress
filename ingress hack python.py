import os

from ingress_functions import *

limpieza_inventario()
# exit(0)
# import browser #recargar los portales
read_portal_file()
# exit(0)

distancia_actual = 0
enviar_cmdshell('sleep 2.5\n')	

# 39.583265
# 2.657453

portal_actual	= select_first_portal()
print(portal_actual)

Hacks_efectuados=0
while 1:

	hackear( portal_actual, distancia_actual)

	Hacks_efectuados+=1
	if Hacks_efectuados > 10 :
		Hacks_efectuados = 0
		limpieza_inventario()

	while 1: 
		portal_siguiente,distancia_siguiente 	= portal_siguiente_class( portal_actual ,min_lvl =3)
		if portal_siguiente != 0 : break
		print('esperando nuevo hack posible...')
		enviar_cmdshell('sleep 60\n')	
	distancia_actual = distancia_siguiente

	portal_actual = portal_siguiente
