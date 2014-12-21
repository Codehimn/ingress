from subprocess import Popen, PIPE	# Import the module
import re 			#regularexpresion
import sys
import time

from datetime import timedelta, datetime

Hack_time=timedelta(seconds=310)
time_ini=datetime.now() - Hack_time

fo=open("portales diciembre.au3",'r', encoding="utf8")	# print ('Name of the file jj: ' , fo.name)

str=fo.read();	# print ("Read String is : ", str)
fo.close()			# Close opend file

portales_dict={}
portales_lst_todos=[]

exp_deploids 	= '%</td><td>(.*?)</td><td'
exp_portales 	= '\[(.*?),(.*?)\]'
exp_titulo		= 'title="(.*?)"'
exp_all=exp_titulo+'.*?'+exp_portales+'.*?'+exp_deploids

matchObj=re.findall('Capture(.*?)help apGain', str)

for i in matchObj:	
	Portales=re.search(exp_all , i)
	if Portales:
		portales_dict[Portales.group(1)]=[Portales.group(1),Portales.group(2),Portales.group(3),time_ini,4]  	
											#titulo,		   X,				Y,			,tiemp,  hacks
		portales_lst_todos.append( [Portales.group(1),Portales.group(2),Portales.group(3),time_ini,4]  )

def portal_siguiente(var):
	distancia_menor=99999
	Y_menor=0
	x,y=var[1],var[2]	
	for port in portales_lst_todos:
		distancia_temp=abs(abs(float(var[1]))-abs(float(port[1])))+abs(abs(float(var[2]))-abs(float(port[2])))
		if var[4]>1 and datetime.now()-time_ini>Hack_time and distancia_temp<distancia_menor and distancia_temp != 0:
			Y_menor=port[0]
			distancia_menor=distancia_temp
	return (Y_menor)

class portal_siguiente_class(object):
	"""docstring for portal_siguiente_class"""
	def __init__(self, var):
		super(portal_siguiente_class, self).__init__()
		distancia_menor=99999
		Y_menor=0
		x,y=var[1],var[2]	
		for port in portales_lst_todos:
			distancia_temp=abs(abs(float(var[1]))-abs(float(port[1])))+abs(abs(float(var[2]))-abs(float(port[2])))
			if var[4]>1 and datetime.now()-time_ini>Hack_time and distancia_temp<distancia_menor and distancia_temp != 0:
				self.portal=portal(port)
				self.distancia
				distancia_menor=distancia_temp
		self.portal_id = Y_menor	

class portal(object):
	"""docstring for portal"""
	def __init__(self, var):
		super(portal, self).__init__()
		self.nombre 			= var[0]
		self.cord_X 			= var[1]
		self.cord_y 			= var[2]
		self.ultimo_hack 		= var[3]
		self.hacks_restantes 	= var[4]



# def touch_x_y(X_mouse, Y_mouse, X_mouse2 = '', Y_mouse2 = ''):
# 	cworsend2('sendevent /dev/input/'+device_touch+' 3 0 ' + X_mouse)
# 	cworsend2('sendevent /dev/input/'+device_touch+' 3 1 ' + Y_mouse)
# 	cworsend2('sendevent /dev/input/'+device_touch+' 0 0 0')
# 	cworsend2('sendevent /dev/input/'+device_touch+' 0 0 0')
# 	cworsend2('sendevent /dev/input/'+device_touch+' 1 272 1')
# 	cworsend2('sendevent /dev/input/'+device_touch+' 0 0 0')
# 	if X_mouse2 != '':
# 		cworsend2('sendevent /dev/input/'+device_touch+' 3 0 ' + X_mouse2)
# 		cworsend2('sendevent /dev/input/'+device_touch+' 3 1 ' + Y_mouse2)
# 		cworsend2('sendevent /dev/input/'+device_touch+' 0 0 0')
# 	cworsend2('sendevent /dev/input/'+device_touch+' 1 272 0')
# 	cworsend2('sendevent /dev/input/'+device_touch+' 0 0 0')


def cworsend2(var):
	# ConsoleWrite( var & @CRLF)
	print(var + '\n')


for x in portales_dict:
	algo = portal_siguiente_class( portales_dict[x] )

algo = portal(portales_dict['Fuente Ramon Roger'])


algo = portal_siguiente_class( portales_dict['Fuente Ramon Roger'] )
# print(algo.portal)

lat = format( float (portales_dict[portal_siguiente( portales_dict['Fuente Ramon Roger'] )] [1]), '.6f' )
lon = format( float (portales_dict[portal_siguiente( portales_dict['Fuente Ramon Roger'] )] [2] ), '.6f' )

print( int(4139.7679))
DistanciaMS = round(float(lat) * 8000000, 5)
# 41397679
# 316632864
# 12345678
print( DistanciaMS)	 
exit(0)

cworsend2("am startservice --ez no_history true --ei lat "+lat+" --ei long "+lon+" -n com.lexa.fakegpsdonate/.FakeGPSService")
cworsend2("am force-stop com.lexa.fakegpsdonate")

# time.sleep(60)

# p1=Popen(['cmd.exe'], stdin=PIPE)
# output =p1.communicate(input='ping 127.0.0.1\n'.encode()) 
# print (output)
# p1.stdin.close()
# p1.wait()

