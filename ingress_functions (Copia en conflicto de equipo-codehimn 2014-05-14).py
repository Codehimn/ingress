#definiciones
#!/usr/bin/python

import binascii
# data=b'0x9F86010001000000080000000100000043000000000A50616E74616C6C612037FFFFFFFF0014426F746F6E2050616E74616C6C6173322E6A706705417269616C0A000000000105000000000000FF01016A020000030000004100000067000000013900000000013701000800000000'
# print(binascii.a2b_hex(data))

def HexToByte( hexStr ):
    """
    Convert a string hex byte values into a byte string. The Hex Byte values may
    or may not be space separated.
    """
    # The list comprehension implementation is fractionally slower in this case    
    #
    #    hexStr = ''.join( hexStr.split(" ") )
    #    return ''.join( ["%c" % chr( int ( hexStr[i:i+2],16 ) ) \
    #                                   for i in range(0, len( hexStr ), 2) ] )
 
    bytes = []
    hexStr = ''.join( hexStr.split(" ") )
    for i in range(0, len(hexStr), 2):
        bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

    return ''.join( bytes )

n = '9F86010001000000080000000100000043000000000A50616E74616C6C612037FFFFFFFF0014426F746F6E2050616E74616C6C6173322E6A706705417269616C0A000000000105000000000000FF01016A0200000300000041000000670000000139000000000137010008000000002'

# print( HexToByte( n ) )


import base64
# hex_data ='57696C6C20796F7520636F6E76657274207468697320484558205468696E6720696E746F20415343494920666F72206D653F2E202E202E202E506C656565656173652E2E2E212121'
hex_data ='b9F86010001000000080000000100000043000000000A50616E74616C6C612037FFFFFFFF0014426F746F6E2050616E74616C6C6173322E6A706705417269616C0A000000000105000000000000FF01016A0200000300000041000000670000000139000000000137010008000000002'

print(HexToByte(hex_data) )



import binascii
# print ( base64.decodestring('b9F86010001000000080000000100000043000000000A50616E74616C6C612037FFFFFFFF0014426F746F6E2050616E74616C6C6173322E6A706705417269616C0A000000000105000000000000FF01016A0200000300000041000000670000000139000000000137010008000000002') )









import sqlite3
from queue import Queue, Empty  # python 3.x
from threading  import Thread


def enqueue_output(out, queue):
	while 1:		
		line = out.readline(1)
		# print(line)
		if '>' == line or '$' == line or '#' == line: 
			queue.put(line)

	out.close()

def enviar_cmdshell(cmdshell,q,var='',mostrar=1):

	# if mostrar :print(var)
	cmdshell.stdin.write(var)
	cmdshell.stdin.flush()

	# print ('xx' +var)
	while 1:
		try:  
			line = q.get(timeout=300) # or q.get(timeout=.1) # q.get_nowait()
		except Empty:	
			print('timeout')
			cmdshell.stdin.write('\n')			
		else:	
			return(line)
	
def mock_location_disable(cmdshell,q,re,check_output):

	enviar_cmdshell(cmdshell,q, "screencap -p /sdcard/ingress_imgs/screen.png\n")
	check_output( 'adb pull /sdcard/ingress_imgs/screen.png'.split(' ') )
		
	respu =  str(check_output( 'ImageMagick-6.8.9-0\\convert screen.png -crop 1x1+750+700 -depth 8 txt:'.split(' ') ) )
	matchObj=re.findall('#([A-F0-9]*?) ', respu)
	for i in matchObj: 
		if '282828' in str(i)  : touch_x_y(cmdshell,q,15800 , 24500)

	respu =  str(check_output( 'ImageMagick-6.8.9-0\\convert screen.png -crop 1x1+150+650 -depth 8 txt:'.split(' ') ) )
	matchObj=re.findall('#([A-F0-9]*?) ', respu)
	for i in matchObj: 
		if '1E4145' in str(i)  : touch_x_y(cmdshell,q,15800 , 24500)

	return (str(i))

def posible_hack(all_portal,date_now):
	for i in all_portal:
		if i.hacks_restantes > 0:
			# (date_now - min(port_sig.ultimo_hack for port_sig in all_portal) )
			return(1)

	print('Hackeado TODO :D')
	exit(0)
	return(0)

def touch_x_y(cmdshell,q,X_mouse, Y_mouse, X_mouse2 = '', Y_mouse2 = '',device_touch = 'event1'):
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

	enviar_cmdshell(cmdshell,q,com_click +'\n' , '')


def portal_siguiente_class(port_act,all_portal,date_now,Hack_time,Hack_time_burn,min_lvl = 0):
	distancia_menor = 9999
	portal_ret=0
	# while portal_ret==0:		
	for port_sig in all_portal:
		distancia_temp=  abs(port_act.lat-port_sig.lat)  + abs(port_act.lon-port_sig.lon) 
		if date_now - port_sig.ultimo_hack  > Hack_time_burn: port_sig.hacks_restantes  = 4
		if port_sig.lvl >= min_lvl  and port_sig.hacks_restantes > 0 and (date_now - port_sig.ultimo_hack) > Hack_time and distancia_temp < distancia_menor and distancia_temp != 0 :
			portal_ret=port_sig
			distancia_menor=distancia_temp
		# print (str(date_now - port_sig.ultimo_hack) + str(Hack_time))
		# print ( str(distancia_temp) + ' - ' + str(distancia_menor))
		# print ( str(port_act.lat)  + ' - ' + str(port_act.lon))
		# print ( str(port_sig.lat)  + ' - ' + str(port_sig.lon))

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

	touch_x_y(cmdshell,q,31228, 31021) #OPS

	for i in range(cant):
		i_esp = i_esp + 1
		if i_esp > 10 and accion == 'drop' :
			enviar_cmdshell(cmdshell,q,'sleep ' + str(4500 /1000) + '\n')
			i_esp = 0
			cant = cant - 10

		touch_x_y(cmdshell,q,XCord, YCord) #ITEM
		enviar_cmdshell(cmdshell,q,'sleep ' + str(150 /1000) + '\n')

		if accion == 'drop'  :
			touch_x_y(cmdshell,q,31228, 31021) #OPS
			enviar_cmdshell(cmdshell,q,'sleep ' + str(600 /1000) + '\n')

			if key :
				touch_x_y(cmdshell,q,XCord, YCord) #ITEM
				enviar_cmdshell(cmdshell,q,'sleep ' + str(2000 /1000) + '\n')
				touch_x_y(cmdshell,q,5800, 16550)#Llave
				enviar_cmdshell(cmdshell,q,'sleep ' + str(2000 /1000) + '\n')
			else:
				# touch_x_y(cmdshell,q,3343, 16820)#Otros
				touch_x_y(cmdshell,q,3050,	23921)#Drop
				enviar_cmdshell(cmdshell,q,'sleep ' + str(500 /1000) + '\n')

		if accion == 'recicle' :
			if key :
				touch_x_y(cmdshell,q,5637, 16296)#Llave
				enviar_cmdshell(cmdshell,q,'sleep ' + str(3200 /1000) + '\n')
			else:
				# touch_x_y(cmdshell,q,3343, 16820);Otros
				touch_x_y(cmdshell,q,3050,	28925)#recicle
				enviar_cmdshell(cmdshell,q,'sleep ' + str(150 /1000) + '\n')
				# enviar_cmdshell(cmdshell,q,'sleep ' + str(1500 /1000) + '\n') # key client ingress

def up_items_bluestacks(cant = 1):
	for i in range(cant):
		touch_x_y(cmdshell,q,10355, 17635)
		enviar_cmdshell(cmdshell,q,'sleep ' + str(300 /1000) + '\n')
		# touch_x_y(cmdshell,q,5500, 17635);llave
		# touch_x_y(cmdshell,q,9000, 17635)
		# touch_x_y(cmdshell,q,3670, 17635)
		touch_x_y(cmdshell,q,3690, 17635)
		enviar_cmdshell(cmdshell,q,'sleep ' + str(2000 /1000) + '\n')

def hackear(cmdshell,q, portal_actual,distancia_actual,re,check_output, random):
	print( 'Hakeando {} {} {} '.format(portal_actual.nombre,portal_actual.lvl,distancia_actual))
 

	enviar_cmdshell(cmdshell,q,'am startservice --ez no_history true --ei lat {} --ei long {} -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate\n'.format(portal_actual.lat + random.randrange(-50,50),portal_actual.lon + random.randrange(-50,50)))

	enviar_cmdshell(cmdshell,q,'sleep '+ str(distancia_actual + 1 ) + '\n' )	
	touch_x_y(cmdshell,q,12000,16500)#click en portal
	enviar_cmdshell(cmdshell,q,'sleep 0.5\n')		

	enviar_cmdshell(cmdshell,q,'sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\' " \n')	
	mock_location_disable(cmdshell,q,re,check_output)
	enviar_cmdshell(cmdshell,q,"am start -a com.nianticproject.ingress -n com.nianticproject.ingress/.NemesisActivity\n")
		
	enviar_cmdshell(cmdshell,q,'am startservice --ez no_history true --ei lat {} --ei long {} -n com.lexa.fakegpsdonate/.FakeGPSService\n'.format(portal_actual.lat,portal_actual.lon))

	for i in range(10):
		touch_x_y(cmdshell,q,21560, 30440)#hack
		enviar_cmdshell(cmdshell,q,'sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name=\'mock_location\' " \n' , '')							
	enviar_cmdshell(cmdshell,q,'am force-stop com.lexa.fakegpsdonate\n')
	enviar_cmdshell(cmdshell,q,'sleep 0.5\n')
	touch_x_y(cmdshell,q,32768, 5) #abajo de hack
	enviar_cmdshell(cmdshell,q,'sleep 0.5\n')
	touch_x_y(cmdshell,q,32768, 5) #abajo de hack


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

def limpieza_inventario(cmdshell,q,check_output):

	touch_x_y(cmdshell,q,32768, 5) #abajo de hack
	enviar_cmdshell(cmdshell,q,'sleep ' + str(500 /1000) + '\n')
	touch_x_y(cmdshell,q,31228, 31021) #OPS
	enviar_cmdshell(cmdshell,q,'sleep 1\n')

	check_output( 'adb shell screencap -p /sdcard/screen.png'.split(' ') )
	check_output( 'adb pull /sdcard/screen.png'.split(' ') )
	check_output( 'adb shell rm /sdcard/screen.png'.split(' ') )
	check_output( 'ImageMagick-6.8.9-0\\Convert screen.png -brightness-contrast 10,80 -rotate -90 -fuzz 0% -fill rgb(0,0,0) -opaque rgb(0,255,255) -fill rgb(255,255,255) -opaque rgb(255,0,0) crop_page.png'.split(' ') )

	check_output( 'Tesseract-ocr\\tesseract.exe crop_page.png screen_to_txt nobatch Lnumeros' )

	f = open("screen_to_txt.txt",'r')
	out = f.readlines() # will append in the list out
	f.close()

	itm_type = [[1,1,0], [1,2,0], [1,3,200], [1,4,100],[1,5,200],[2,1,0], [2,2,0], [2,3,100], [2,10,0], [4,1,0],[4,2,0],[5,1,0],[5,2,0]]


	muchos_items=0	
	for line in out:  
		line=line.replace('-','0') 			
		if 'tems' in line and 'XM' in line:	
			print(line)	
			line = line.replace(': ',' ')
			line = line.replace(':',' ')
			line = line.replace(',','')

			if int(line.split(' ')[1] ) > 1500: #si tiene mas de X items
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

					drop_items_bluestack(cmdshell, itm[0] , cant, accion = 'recicle',key = '')

	enviar_cmdshell(cmdshell,q,"am start -a com.nianticproject.ingress -n com.nianticproject.ingress/.NemesisActivity\n")
	

	# drop_items_bluestack(cmdshell,'X5', 70, accion = 'drop',key = '')
	# drop_items_bluestack(cmdshell,'X4', 210, accion = 'drop',key = '')
	# drop_items_bluestack(cmdshell,'U8', 100, accion = 'recicle',key = 1)

	# drop_items_bluestack(cmdshell,'X1', 100, accion = 'recicle',key = '')
	# drop_items_bluestack(cmdshell,'X2', 100, accion = 'recicle',key = '')		
	# drop_items_bluestack(cmdshell,'X3', 50, accion = 'recicle',key = '')
	# drop_items_bluestack(cmdshell,'C1', 100, accion = 'recicle',key = '')
	# drop_items_bluestack(cmdshell,'R1', 100, accion = 'recicle',key = '')
	# drop_items_bluestack(cmdshell,'R2', 100, accion = 'recicle',key = '')	
	# drop_items_bluestack(cmdshell,'R3', 50, accion = 'recicle',key = '')	
	# drop_items_bluestack(cmdshell,'X10', 100, accion = 'recicle',key = '')



def connect_db():
	location = 'portal_list.db'
	conn = sqlite3.connect(location)
	c = conn.cursor()	
	quer = 'create table if not exists portals (nombre text,lat integer,lon integer,lvl integer,deployds integer,ultimo_hack text,hacks_restantes integer , PRIMARY KEY(lat,lon))'
	c.execute(quer)
	return(c,conn)


try:	sql
except NameError:	sql,db = connect_db()

sql.execute('select * from portals where lat = {} and lon = {} '.format(3,1))
row = sql.fetchone()
if row is None:
  #not exists
  sql.execute("insert into portals values('{}' , {},{},{},{},'{}',{} )".format(var[0],int(float (var[1]) * 1000000) ,int(float (var[2]) * 1000000),int(var[3]) ,int(var[4]),var[5],int(var[6])  ))
else:
  #exists
  print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))


# sql.execute('select * from portals')
# all_rows = sql.fetchall()
# for row in all_rows:
#     # row[0] returns the first column in the query (name), row[1] returns email column.
#     print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

db.commit() #Commit the change
