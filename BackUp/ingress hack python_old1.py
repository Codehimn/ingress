import subprocess	# Import the module
import re 			#regularexpresion
import sys

from datetime import timedelta, datetime

Hack_time = timedelta(minutes=5)
time_ini = datetime.now() - Hack_time

fo = open("portales diciembre.au3",'r', encoding="utf8")
# print ('Name of the file jj: ' , fo.name)

str = fo.read();
# print ("Read String is : ", str)
# Close opend file
fo.close()

portales_dict = {}

exp_deploids 	= '%</td><td>(.*?)</td><td'
exp_portales 	= '\[(.*?),(.*?)\]'
exp_titulo		= 'title="(.*?)"'
exp_all = exp_titulo + '.*?' +exp_portales + '.*?' + exp_deploids

matchObj = re.findall('Capture(.*?)help apGain', str)

for i in matchObj:	
	Portales = re.search(exp_all , i)
	if Portales:	
		portales_dict[Portales.group(1)] = [Portales.group(1),Portales.group(2),Portales.group(3),time_ini]
	# print ( portales_dict[Portales.group(1)] )



# Ask the user for input

try:
    host = input("Enter a host to ping: ")	
except EOFError:
    break

# Set up the echo command and direct the output to a pipe
p1 = subprocess.Popen(['ping', '-c 2', host], stdout=subprocess.PIPE)

# Run the command
output = p1.communicate()[0]

print (output)