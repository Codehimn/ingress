#!/usr/bin/env python
 
# firefox.py
 
import telnetlib
 
HOST = 'localhost'
PORT = 4242
 
def open_curr_tab(url):
	tn = telnetlib.Telnet(HOST, PORT)
	cmd = "content.location.href = '{url}'\n".format(url=url)    
	tn.read_until( b"repl> " ) 
	tn.write( cmd.encode('UTF-8') )
	# tn.write(b'document.getElementById("GmailAddress").value="pepe" \n')
	tn.write(b"document.getElementById('GmailAddress').value='pepe' \n")
	# tn.write(b'document.getElementById("FirstName").value="pepe"\n')
	# tn.write(b'document.getElementById("FirstName").value="pepe"\n')
	# tn.write(b'document.getElementById("FirstName").value="pepe"\n')
	# # print( tn.read_all() ) 
	print(tn.read_until( b"repl> " , 10) )
	tn.write(b"repl.quit()\n")

#############################################
 
if __name__ == "__main__":
	open_curr_tab('https://accounts.google.com/signup')

#GmailAddress