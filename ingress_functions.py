#definiciones
#!/usr/bin/python

import sqlite3
from queue import Queue, Empty  # python 3.x
from threading  import Thread
import re 			#regularexpresion
from datetime import timedelta, datetime

import sys
from time import sleep
from subprocess import *
import pickle #para crear un txt con los portales
import random
import os



Hack_time=timedelta(seconds=310)
Hack_time_burn=timedelta(hours=4)
time_ini=datetime.now() - Hack_time


def enqueue_output(out, queue):
	while 1:		
		line = out.readline(1)
		# print(line)
		if '>' == line or '$' == line or '#' == line: 
			queue.put(line)

	out.close()

def enviar_cmdshell(var='',mostrar=1):

	# if mostrar :print(var)
	cmdshell.stdin.write(var)
	cmdshell.stdin.flush()

	# print ('xx' +var)
	while 1:
		try:  
			line = q.get(timeout=200) # or q.get(timeout=.1) # q.get_nowait()
		except Empty:	
			print('timeout')
			cmdshell.stdin.write('\n')
			return('#')
		else:	
			return(line)
	
def mock_location_disable():

	enviar_cmdshell("am start -a com.nianticproject.ingress -n com.nianticproject.ingress/.NemesisActivity\n")

	enviar_cmdshell( "screencap -p /sdcard/ingress_imgs/screen.png\n")
	check_output( 'adb pull /sdcard/ingress_imgs/screen.png'.split(' ') )
		
	respu =  str(check_output( 'ImageMagick-6.8.9-0\\convert screen.png -crop 1x1+750+700 -depth 8 txt:'.split(' ') ) )
	matchObj=re.findall('#([A-F0-9]*?) ', respu)
	for i in matchObj: 
		if '282828' in str(i)  : touch_x_y(15800 , 24500)

	respu =  str(check_output( 'ImageMagick-6.8.9-0\\convert screen.png -crop 1x1+150+650 -depth 8 txt:'.split(' ') ) )
	matchObj=re.findall('#([A-F0-9]*?) ', respu)
	for i in matchObj: 
		if '1E4145' in str(i)  : touch_x_y(15800 , 24500)

	enviar_cmdshell("am start -a com.nianticproject.ingress -n com.nianticproject.ingress/.NemesisActivity\n")

	return (str(i))

def posible_hack(all_portal,date_now):
	for i in all_portal:
		if i.hacks_restantes > 0:
			# (date_now - min(port_sig.ultimo_hack for port_sig in all_portal) )
			return(1)

	print('Hackeado TODO :D')
	exit(0)
	return(0)

def touch_x_y(X_mouse, Y_mouse, X_mouse2 = '', Y_mouse2 = '',device_touch = 'event1'):
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

	enviar_cmdshell(com_click +'\n' , '')


def portal_siguiente_class(port_act,date_now = datetime.now(),Hack_time = Hack_time - timedelta(seconds=10) ,Hack_time_burn = Hack_time_burn,min_lvl = 0,solo_print=0):
	distancia_menor = 9999
	portal_ret=0
	# while portal_ret==0:	

	sql.execute('select * from portals')
	rows = sql.fetchall ()
	for port_sig in rows:
		distancia_temp = abs(port_act['lat']-port_sig['lat']) +  abs(port_act['lon']-port_sig['lon'])
		
		dif_date =date_now - datetime.strptime(port_sig['ultimo_hack'], '%Y-%m-%d %H:%M:%S.%f')

		if dif_date > Hack_time_burn:
			sql.execute('update portals set hacks_restantes = 4 where lat = {} and lon = {} '.format( port_sig['lat'] ,port_sig['lon']) )
			if solo_print == 0: db.commit() #Commit the change

		if port_sig['lvl'] >= min_lvl  and port_sig['hacks_restantes'] > 0 and dif_date > Hack_time and distancia_temp < distancia_menor and distancia_temp != 0 :
			portal_ret=port_sig
			distancia_menor=distancia_temp

	# print("hackear( {'lat' : {} ,'lon' : {} }, 0)".format(port_sig['lat'] , port_sig['lon']))
	# print("hackear( {'nombre' : "+str(portal_ret['nombre'])+", 'lat' : "+str(portal_ret['lat'])+" ,'lon' : "+str(portal_ret['lon'])+" }, 0)" )
	print('am start -a com.nianticproject.ingress -n com.nianticproject.ingress/cm.nianticproject.ingress.NemesisActivity;am startservice --ez no_history true --ei lat '+str(portal_ret['lat'])+' --ei long '+str(portal_ret['lon'])+' -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.2; sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\'" ; am force-stop com.lexa.fakegpsdonate ;casa Gabor' ) 

	return(portal_ret, round(distancia_menor * 0.008 , 2))


# Definiciones para drops

def drop_items_bluestack(item, cant = 1, accion = 'drop',key = ''): # key = 0 = normal
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

	touch_x_y(31228, 31021) #OPS

	for i in range(cant):
		i_esp = i_esp + 1
		if i_esp > 10 and accion == 'drop' :
			enviar_cmdshell('sleep ' + str(4500 /1000) + '\n')
			i_esp = 0
			cant = cant - 10

		touch_x_y(XCord, YCord) #ITEM
		enviar_cmdshell('sleep ' + str(150 /1000) + '\n')

		if accion == 'drop'  :
			touch_x_y(31228, 31021) #OPS
			enviar_cmdshell('sleep ' + str(600 /1000) + '\n')

			if key :
				touch_x_y(XCord, YCord) #ITEM
				enviar_cmdshell('sleep ' + str(2000 /1000) + '\n')
				touch_x_y(5800, 16550)#Llave
				enviar_cmdshell('sleep ' + str(2000 /1000) + '\n')
			else:
				# touch_x_y(3343, 16820)#Otros
				touch_x_y(3050,	23921)#Drop
				enviar_cmdshell('sleep ' + str(500 /1000) + '\n')

		if accion == 'recicle' :
			if key :
				touch_x_y(5637, 16296)#Llave
				enviar_cmdshell('sleep ' + str(3200 /1000) + '\n')
			else:
				# touch_x_y(3343, 16820);Otros
				touch_x_y(3050,	28925)#recicle
				enviar_cmdshell('sleep ' + str(150 /1000) + '\n')
				# enviar_cmdshell('sleep ' + str(1500 /1000) + '\n') # key client ingress

def up_items_bluestacks(cant = 1):
	for i in range(cant):
		touch_x_y(10355, 17635)
		enviar_cmdshell('sleep ' + str(300 /1000) + '\n')
		# touch_x_y(5500, 17635);llave
		# touch_x_y(9000, 17635)
		# touch_x_y(3670, 17635)
		touch_x_y(3690, 17635)
		enviar_cmdshell('sleep ' + str(2000 /1000) + '\n')

def hackear( portal_actual,distancia_actual):
	print( 'Hakeando {} {} {} '.format(portal_actual['nombre'],portal_actual['lvl'],distancia_actual))
 
	enviar_cmdshell('am startservice --ez no_history true --ei lat {} --ei long {} -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate\n'.format(portal_actual['lat'] + random.randrange(-50,50),portal_actual['lon'] + random.randrange(-50,50)))

	enviar_cmdshell('sleep '+ str(distancia_actual + 1 ) + '\n' )	
	touch_x_y(12000,16500)#click en portal
	enviar_cmdshell('sleep 0.5\n')		

	enviar_cmdshell('sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\' " \n')		
	mock_location_disable()	
		
	enviar_cmdshell('am startservice --ez no_history true --ei lat {} --ei long {} -n com.lexa.fakegpsdonate/.FakeGPSService\n'.format(portal_actual['lat'],portal_actual['lon']))

	for i in range(10):
		touch_x_y(21560, 30440)#hack
		enviar_cmdshell('sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\' " \n' , '')							
	enviar_cmdshell('am force-stop com.lexa.fakegpsdonate\n')
	enviar_cmdshell('sleep 0.5\n')
	touch_x_y(32768, 5) #abajo de hack
	enviar_cmdshell('sleep 0.5\n')
	touch_x_y(32768, 5) #abajo de hack

	sql.execute('update portals set hacks_restantes = hacks_restantes -1, ultimo_hack = "{}" where lat = {} and lon = {} '.format( datetime.now() ,portal_actual['lat'] ,portal_actual['lon']) )
	db.commit() #Commit the change

class portal(object):
	"""docstring for portal"""
	def __init__(self, var):
		super(portal, self).__init__()
		self.nombre 		= var[0]		
		self.lat 			= int(float (var[1]) * 1000000) 
		self.lon 			= int(float (var[2]) * 1000000) 
		self.lvl 			= int(var[3])
		self.deployds	 	= int(var[4])
		self.ultimo_hack 	= var[5]
		self.hacks_restantes= int(var[6])

def limpieza_inventario():

	enviar_cmdshell("am start -a com.nianticproject.ingress -n com.nianticproject.ingress/.NemesisActivity\n")
	touch_x_y(32768, 5) #abajo de hack
	enviar_cmdshell('sleep ' + str(500 /1000) + '\n')
	touch_x_y(31228, 31021) #OPS
	enviar_cmdshell('sleep 1\n')

	check_output( 'adb shell screencap -p /sdcard/screen.png'.split(' ') )
	check_output( 'adb pull /sdcard/screen.png'.split(' ') )
	check_output( 'adb shell rm /sdcard/screen.png'.split(' ') )
	# check_output( 'ImageMagick-6.8.9-0\\Convert screen.png -depth 3 -rotate -90 -shave 0x70 -threshold 10% crop_page.jpg'.split(' ') )

	# check_output( 'ImageMagick-6.8.9-0\\Convert screen.png -brightness-contrast 30,30 -depth 1 -rotate -90 -shave 0x70 -fuzz 0% -fill rgb(0,0,0) -opaque rgb(0,255,255) -fill rgb(255,255,255) -threshold 10% crop_page.jpg'.split(' ') )
	check_output( 'ImageMagick-6.8.9-0\\Convert screen.png -brightness-contrast 10,60 -rotate -90 -fuzz 0% -fill rgb(0,0,0) -opaque rgb(0,255,255) -fill rgb(255,255,255) -opaque rgb(255,0,0) crop_page.jpg'.split(' ') )
# -normalize
	check_output( 'Tesseract-ocr\\tesseract.exe crop_page.jpg screen_to_txt -psm 6 nobatch Lnumeros' )

	f = open("screen_to_txt.txt",'r')
	out = f.readlines() # will append in the list out
	f.close()

	itm_type = [[1,1,0], [1,2,0], [1,3,200], [1,4,100],[1,5,200],[2,1,0], [2,2,0], [2,3,100], [2,10,0], [4,1,0],[5,1,0],[5,2,0]]


	muchos_items=0	
	for line in out:  
		line=line.replace('-','0') 			
		if 'tems' in line and 'XM' in line:	
			print(line)	
			line = line.replace(': ',' ')
			line = line.replace(':',' ')
			line = line.replace(',','')

			if int(line.split(' ')[1] ) > 1300: #si tiene mas de X items
				muchos_items=1

		itm_type_spl = line.split(' ')
		if muchos_items==1 and len(itm_type_spl) == 6:
			for itm in itm_type:	
				if 'L{} '.format(itm[1]) == line[0:3]:
					cant= int(itm_type_spl[ itm[0] ] )
					min_cant = itm[2]					
					if cant > min_cant:  
						cant -= min_cant
					else:
						cant = int( cant * 0.8 ) # un 80%
					print(str(itm) + 'cant:' + str(cant) )

					if itm[0] == 1 :itm[0] = 'R' + str(itm[1])
					if itm[0] == 2 :itm[0] = 'X' + str(itm[1])
					if itm[0] == 3 :itm[0] = 'U' + str(itm[1])
					if itm[0] == 4 :itm[0] = 'C' + str(itm[1])
					if itm[0] == 5 :itm[0] = 'M' + str(itm[1])

					drop_items_bluestack( itm[0] , cant, accion = 'recicle',key = '')

	enviar_cmdshell("am start -a com.nianticproject.ingress -n com.nianticproject.ingress/.NemesisActivity\n")
	

	# drop_items_bluestack('X5', 70, accion = 'drop',key = '')
	# drop_items_bluestack('X4', 210, accion = 'drop',key = '')
	# drop_items_bluestack('U8', 100, accion = 'recicle',key = 1)

	# drop_items_bluestack('X1', 100, accion = 'recicle',key = '')
	# drop_items_bluestack('X2', 100, accion = 'recicle',key = '')		
	# drop_items_bluestack('X3', 50, accion = 'recicle',key = '')
	# drop_items_bluestack('C1', 100, accion = 'recicle',key = '')
	# drop_items_bluestack('R1', 100, accion = 'recicle',key = '')
	# drop_items_bluestack('R2', 100, accion = 'recicle',key = '')	
	# drop_items_bluestack('R3', 50, accion = 'recicle',key = '')	
	# drop_items_bluestack('X10', 100, accion = 'recicle',key = '')



def connect_db():
	location = 'portal_list.db'
	conn = sqlite3.connect(location)
	conn.row_factory = sqlite3.Row
	c = conn.cursor()	
	quer = 'create table if not exists portals (nombre text,lat integer,lon integer,lvl integer,deployds integer,ultimo_hack dateime,hacks_restantes integer , PRIMARY KEY(lat,lon))'
	c.execute(quer)
	return(c,conn)

def add_update_portals(var):

	sql.execute('select * from portals where lat = {} and lon = {} '.format(var['lat'] ,var['lon']))
	row = sql.fetchone()
	if row is None:
		#not exists
		sql.execute("insert into portals values('{}',{},{},{},{},'{}',{} )".format(var['nombre'],var['lat'] ,var['lon'],var['lvl'] ,var['deployds'],var['ultimo_hack'],var['hacks_restantes']  ))
	else:
		#exists
		sql.execute("update portals set lvl = {} , deployds = {} , ultimo_hack = '{}' , hacks_restantes = {} where lat = {} and lon = {} ".format(var['lvl'],var['deployds'],var['ultimo_hack'],var['hacks_restantes'] , var['lat'] ,var['lon']))
	db.commit() #Commit the change



def select_portal(lat,lon):
	var={}
	sql.execute('select * from portals where lat = {} and lon = {} '.format(lat,lon))
	row = sql.fetchone()

	var['nombre'] = row['nombre']
	var['lat'] = row['lat']
	var['lon'] = row['lon']
	var['lvl'] = row['lvl']
	var['deployds'] = row['deployds']
	var['ultimo_hack'] = row['ultimo_hack']
	var['hacks_restantes'] = row['hacks_restantes']


	db.commit() #Commit the change
	return(var)

def select_first_portal():
	sql.execute('select lat,lon from portals limit 1')
	row = sql.fetchone()
	if row is None: 
		print(':( no hay portales en la bd')
		exit(0)
	else : 
		return(select_portal(row['lat'],row['lon']))


def read_portal_file():
	fo=open("portales.list",'r', encoding="UTF-8")	# print ('Name of the file jj: ' , fo.name)
	# fo=open("portales palma mallorca.au3",'r', encoding="UTF-8")	# print ('Name of the file jj: ' , fo.name)

	stri=fo.read();	# print ("Read String is : ", str)
	stri = stri.replace( "'" , '')
	fo.close()			# Close opend file

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
		# if Portales:		portales_arr.append ( portal ([Portales.group(1),Portales.group(2),Portales.group(3),Portales.group(4),Portales.group(5),time_ini,4]  )	)
		# add_update_portals	()
		if Portales:		add_update_portals({'nombre' : Portales.group(1),'lat' : int(float (Portales.group(2)) * 1000000),'lon' : int(float (Portales.group(3)) * 1000000),'lvl' : int(Portales.group(4)),'deployds' : int(Portales.group(5)),'ultimo_hack' : time_ini,'hacks_restantes' : 4}  )	

	# os.rename("portales.list", "portales_process.list")
	print('portales_db creado')


def Ubicacion_ok():
	#oto , ver si se puede hackear
	return(c,conn)

try:	sql
except NameError:	sql,db = connect_db()

cmdshell = Popen(['cmd'], bufsize=1, stdout=PIPE,stdin=PIPE,stderr=PIPE,universal_newlines=True)

while cmdshell.stdout.readline(1) != '>': pass #limpiamos el stdout :D
try:  
	q
except NameError:	
	q = Queue()
	t = Thread(target=enqueue_output, args=(cmdshell.stdout, q))
	t.daemon = True # thread dies with the program
	t.start()

if enviar_cmdshell("adb shell\n") != "$":
	enviar_cmdshell("adb kill-server\n")
	enviar_cmdshell("adb shell\n")

enviar_cmdshell("su\n")

enviar_cmdshell("am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity\n")




#funciones _viejad

# def portal_siguiente_class(port_act,all_portal,date_now,Hack_time,Hack_time_burn,min_lvl = 0):
# 	distancia_menor = 9999
# 	portal_ret=0
# 	# while portal_ret==0:		
# 	for port_sig in all_portal:
# 		distancia_temp=  abs(port_act.lat-port_sig.lat)  + abs(port_act.lon-port_sig.lon) 
# 		if date_now - port_sig.ultimo_hack  > Hack_time_burn: port_sig.hacks_restantes  = 4
# 		if port_sig.lvl >= min_lvl  and port_sig.hacks_restantes > 0 and (date_now - port_sig.ultimo_hack) > Hack_time and distancia_temp < distancia_menor and distancia_temp != 0 :
# 			portal_ret=port_sig
# 			distancia_menor=distancia_temp

# 	return(portal_ret, round(distancia_menor * 0.008 , 2))
