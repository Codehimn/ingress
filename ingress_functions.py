#definiciones
#!/usr/bin/python



def enviar_cmdshell(cmdshell,var='',mostrar=1):
	# if mostrar :print(var)
	cmdshell.stdin.write(var)
	cmdshell.stdin.flush()
	stdout=[]	
	while True:
		line = cmdshell.stdout.readline(1)
		# print(line)
		if '>' == line or  '#' == line: break

def posible_hack(all_portal,date_now):
	for i in all_portal:
		if i.hacks_restantes > 0:
			# (date_now - min(port_sig.ultimo_hack for port_sig in all_portal) )
			return(1)

	print('Hackeado TODO :D')
	exit(0)
	return(0)

def touch_x_y(cmdshell,X_mouse, Y_mouse, X_mouse2 = '', Y_mouse2 = '',device_touch = 'event1'):
	com_click = 'sendevent /dev/input/{} 3 0 {}; '.format(device_touch,X_mouse)
	com_click = com_click + 'sendevent /dev/input/{} 3 1 {}; '.format(device_touch,Y_mouse)
	com_click = com_click + 'sendevent /dev/input/{} 0 0 0; '.format(device_touch)
	com_click = com_click + 'sendevent /dev/input/{} 0 0 0; '.format(device_touch)
	com_click = com_click + 'sendevent /dev/input/{} 1 272 1; '.format(device_touch)
	com_click = com_click + 'sendevent /dev/input/{} 0 0 0; '.format(device_touch)
	if X_mouse2 :
		com_click = com_click + 'sendevent /dev/input/{} 3 0 {}; '.format(device_touch, X_mouse2)
		com_click = com_click + 'sendevent /dev/input/{} 3 1 {}; '.format(device_touch, Y_mouse2)
		com_click = com_click + 'sendevent /dev/input/{} 0 0 0; '.format(device_touch)
	com_click = com_click + 'sendevent /dev/input/{} 1 272 0; '.format(device_touch)
	com_click = com_click + 'sendevent /dev/input/{} 0 0 0; '.format(device_touch)

	enviar_cmdshell(cmdshell,com_click +'\n' , '')


def portal_siguiente_class(port_act,all_portal,date_now,Hack_time,Hack_time_burn):
	distancia_menor = 9999
	portal_ret=0
	# while portal_ret==0:		
	for port_sig in all_portal:
		distancia_temp=  abs(port_act.lat-port_sig.lat)  + abs(port_act.lon-port_sig.lon) 
		if date_now - port_sig.ultimo_hack  > Hack_time_burn: port_sig.hacks_restantes  = 4
		if port_sig.hacks_restantes > 0 and (date_now - port_sig.ultimo_hack) > Hack_time and distancia_temp < distancia_menor and distancia_temp != 0 :
			portal_ret=port_sig
			distancia_menor=distancia_temp
		print (str(date_now - port_sig.ultimo_hack) + str(Hack_time))
		print ( str(distancia_temp) + ' - ' + str(distancia_menor))
		print ( str(port_act.lat)  + ' - ' + str(port_act.lon))
		print ( str(port_sig.lat)  + ' - ' + str(port_sig.lon))

	# if portal_ret==0 :
	# 	if posible_hack(all_portal,date_now) : print('.')

	return(portal_ret, round(distancia_menor * 0.008 , 2))

# Definiciones para drops

def drop_items_bluestack(cmdshell,item, cant = 1, accion = 'drop',key = ''): # key = 0 = normal
	XCord = 28380 + 750
	YCord = 6575 - 5650

	i_esp = 0
	for lvl in range(17):
		if str(lvl) in item  : XCord = XCord - (lvl * 750)

	if "R" in item : YCord = YCord + (5650)
	if "X" in item : YCord = YCord + (5650 * 2)
	if "U" in item : YCord = YCord + (5650 * 3)
	if "C" in item : YCord = YCord + (5650 * 4)
	if "M" in item : YCord = YCord + (5650 * 5)

	for i in range(cant):
		i_esp = i_esp + 1
		if i_esp > 10 and accion == 'drop' :
			enviar_cmdshell(cmdshell,'sleep ' + str(4500 /1000) + '\n')
			i_esp = 0
			cant = cant - 10

		# 		touch_x_y(cmdshell,31051, 30481) ;OPS
		touch_x_y(cmdshell,31228, 31021) #OPS
		enviar_cmdshell(cmdshell,'sleep ' + str(600 /1000) + '\n')

		touch_x_y(cmdshell,XCord, YCord) #ITEM
		enviar_cmdshell(cmdshell,'sleep ' + str(800 /1000) + '\n')

		if accion == 'drop'  :
			if key :
				enviar_cmdshell(cmdshell,'sleep ' + str(1200 /1000) + '\n')
				touch_x_y(cmdshell,5637, 16321)#Llave
				enviar_cmdshell(cmdshell,'sleep ' + str(3200 /1000) + '\n')
			else:
				# touch_x_y(cmdshell,3343, 16820)#Otros
				touch_x_y(cmdshell,3050,	23921)#Drop
				enviar_cmdshell(cmdshell,'sleep ' + str(500 /1000) + '\n')

		if accion == 'recicle' :
			if key :
				touch_x_y(cmdshell,5637, 16296)#Llave
				enviar_cmdshell(cmdshell,'sleep ' + str(3200 /1000) + '\n')
			else:
				# touch_x_y(cmdshell,3343, 16820);Otros
				touch_x_y(cmdshell,3050,	28925)#Drop
				enviar_cmdshell(cmdshell,'sleep ' + str(500 /1000) + '\n')
				enviar_cmdshell(cmdshell,'sleep ' + str(1500 /1000) + '\n') # key client ingress

def up_items_bluestacks(cant = 1):
	for i in range(cant):
		touch_x_y(cmdshell,10355, 17635)
		enviar_cmdshell(cmdshell,'sleep ' + str(300 /1000) + '\n')
		# touch_x_y(cmdshell,5500, 17635);llave
		# touch_x_y(cmdshell,9000, 17635)
		# touch_x_y(cmdshell,3670, 17635)
		touch_x_y(cmdshell,3690, 17635)
		enviar_cmdshell(cmdshell,'sleep ' + str(2000 /1000) + '\n')

def reciclar_bluestacks(veces, key = 0):
	for i in range(veces):
		
		if key == 0 :
			touch_x_y(cmdshell,25920, 12397)
			enviar_cmdshell(cmdshell,'sleep ' + str(800 /1000) + '\n')
			touch_x_y(cmdshell,3277, 26714)
			enviar_cmdshell(cmdshell,'sleep ' + str(600 /1000) + '\n')
		else:
			touch_x_y(cmdshell,31228, 31021) #;OPS
			enviar_cmdshell(cmdshell,'sleep ' + str(1000 /1000) + '\n')
			touch_x_y(cmdshell,18710, 16470)#lLAVE
			enviar_cmdshell(cmdshell,'sleep ' + str(1000 /1000) + '\n')
			touch_x_y(cmdshell,5015, 30750) #Recycle
			enviar_cmdshell(cmdshell,'sleep ' + str(1000 /1000) + '\n')
			touch_x_y(cmdshell,13239, 8846) #Confirm
			enviar_cmdshell(cmdshell,'sleep ' + str(1000 /1000) + '\n')

def hackear(cmdshell, portal_actual,distancia_actual):
	print( 'Hakeando ' + portal_actual.nombre)
	enviar_cmdshell(cmdshell,'am startservice --ez no_history true --ei lat {} --ei long {} -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate\n'.format(portal_actual.lat,portal_actual.lon))

	enviar_cmdshell(cmdshell,'sleep '+ str(distancia_actual + 1 ) + '\n' )	
	touch_x_y(cmdshell,12000,16500)#click en portal
	enviar_cmdshell(cmdshell,'sleep 0.5\n')		

	enviar_cmdshell(cmdshell,'sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\' " ;\n')		
	enviar_cmdshell(cmdshell,'am startservice --ez no_history true --ei lat {} --ei long {} -n com.lexa.fakegpsdonate/.FakeGPSService\n'.format(portal_actual.lat,portal_actual.lon))

	for i in range(10):
		touch_x_y(cmdshell,21560, 30440)#hack
		enviar_cmdshell(cmdshell,'sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\' " ;\n' , '')							
	enviar_cmdshell(cmdshell,'am force-stop com.lexa.fakegpsdonate\n')
	enviar_cmdshell(cmdshell,'sleep 0.5\n')
	touch_x_y(cmdshell,32768, 5) #abajo de hack
	enviar_cmdshell(cmdshell,'sleep 0.5\n')
	touch_x_y(cmdshell,32768, 5) #abajo de hack


class portal(object):
	"""docstring for portal"""
	def __init__(self, var):
		super(portal, self).__init__()
		self.nombre 		= var[0]
		self.lat 			= int(float (var[1]) * 1000000) 
		self.lon 			= int(float (var[2]) * 1000000) 
		self.ultimo_hack 	= var[3]
		self.hacks_restantes= int(var[4])

