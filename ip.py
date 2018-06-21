#!/usr/bin/python

import commands
import time

option='''
press 0 to check for wifi.
press 1  to check internet cable on your machine.
press 2 to check internet access.
press 3 to check for google access.
'''

print " "
print " *************************** "

print option

choice=raw_input("Enter your choice: ")

print "  "

if choice == '0' :
	print"plz wait wifi is checking..."
	time.sleep(2)
	w=commands.getoutput('iwconfig')
	print w
	
	if 'ESSID:off' in w :
		print "wifi is not conneccted"
		out = "wifi is not connected"
		commands.getoutput('notify send '+ out)
		commands.getoutput('echo wifi is not connected | festival --tts')
	else :
		print "wifi is connected"
		print w
		out = "wifi is connected"
		commands.getoutput('notify send '+ out)
		commands.getoutput('echo wifi is connected | festival --tts')

elif choice == '1' :
	print"plz wait internet cable is being checked.."
	time.sleep(2)
	x=commands.getoutput('sudo mii-tool enp3s0')
	print x
	
	if 'link ok' in x :
		print "cable is conneccted"
		out = "connected"
		commands.getoutput('notify send '+ out)
		commands.getoutput('echo connected | festival --tts')
	else :
		print "cable is not connected"
		out = "not connected"
		commands.getoutput('notify send '+ out)
		commands.getoutput('echo not connected | festival --tts')

elif choice == '2':
	print "internet connectivity is checking in a  while.."
	time.sleep(2)
	y=commands.getoutput('ping -c 1 -W 1 8.8.8.8')
	print y

	if '0% packet loss' in y :
		print "internet conitivity  is all right"
		out = "internet is alright"
		commands.getoutput('notify send '+ out)
		commands.getoutput('echo internet is all right | festival --tts')	

	else :
		print "internet conitivity is not right"
		out = "no internet "
		commands.getoutput('notify send '+ out)
		commands.getoutput('echo no interent | festival --tts')

elif choice == '3' :
	print "loading google web page"
	time.sleep(2)

	z=commands.getoutput('firefox 172.217.166.164')
	commands.getoutput('notify send opening google page')
	commands.getoutput('echo loading google page | festival --tts')
else:
	print "wrong choice."
	print "TRY AGAIN !"
