#clases



def enviar_cmdshell(cmdshell,var='',mostrar=1):
	if mostrar :print(var)

	cmdshell.stdin.write(var)
	cmdshell.stdin.flush()

	stdout=[]	
	while True:
		line = cmdshell.stdout.readline(1)
		# print(line)
		if '>' == line or  '#' == line: break
			
	# return ''.join(stdout)


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



class portal_siguiente_class(object):
	"""docstring for portal_siguiente_class"""
	def __init__(self, var,var2,date,Hack_time):
		super(portal_siguiente_class, self).__init__()
		distancia_menor=99999
		x,y=var[1],var[2]	
		for port in var2:
			distancia_temp=abs(float(var[1])-float(port[1])) + abs(float(var[2])-float(port[2]))
			if var[4]>1 and date-var[3]>Hack_time and distancia_temp<distancia_menor and distancia_temp != 0:
				self.portal=portal(port)				
				distancia_menor=distancia_temp
		self.distancia = round(distancia_menor * 18000,2)

class portal(object):
	"""docstring for portal"""
	def __init__(self, var):
		super(portal, self).__init__()
		self.nombre 		= var[0]
		self.lat 			= int(float (var[1]) * 1000000) 
		self.lon 			= int(float (var[2]) * 1000000) 
		self.ultimo_hack 	= var[3]
		self.hacks_restantes= var[4]


# Definiciones para drops

def DropItems_bluestack(cmdshell,item, cant = 1, accion = 'drop',key = ''): # key = 0 = normal
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


def Up_Items_bluestacks(cant = 1):
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





