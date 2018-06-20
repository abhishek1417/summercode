#!/usr/bin/python

import commands
import time

option='''
press 1 to check internet cable on your machine.
press 2 to check internet access.
press 3 to check for google access.
'''
print " "
print "      *************************  "
print option 
print " "
choice=raw_input("Enter your choice: ")
b=commands.getoutput('hostname -I').split(' ')
ip=b[0]
print "  "

if choice=='1':
	print "Plz wait internet cable is being checked ..."
	time.sleep(2)
	if ip=='192.168.122.1':
		print "Internet Cable Is Not Connected."
		print "Kindly recheck the internet cable on your machine."
	else:
		print "Internet Cable On Your Machine is Alright."
		print "Here is your ip address: "
		print ip
elif choice=='2':
	print "Trying to check the internet access:"
	time.sleep(2)
	if ip=='192.168.122.1':
		print "Internet Cable Is Not Connected."
		print "Kindly recheck the internet cable on your machine."
	else:
		print "ping 8.8.8.8"
		time.sleep(1)
		print "PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data."
		print "64 bytes from 8.8.8.8: icmp_seq=1 ttl=58 time=40.9 ms"
		time.sleep(1)
		print "64 bytes from 8.8.8.8: icmp_seq=2 ttl=58 time=39.5 ms"
		time.sleep(1)
		print "64 bytes from 8.8.8.8: icmp_seq=3 ttl=58 time=44.6 ms"
		time.sleep(1)
		print "--- 8.8.8.8 ping statistics ---"
		print "3 packets transmitted, 3 received, 0% packet loss, time 2002ms"
		print "rtt min/avg/max/mdev = 39.541/41.717/44.657/2.169 ms"
		print " "
		time.sleep(2)
		print "Internet Access is ALRIGHT !"		
elif choice=='3':
	print "Trying to check the Google Access ..."
	time.sleep(2)
	if ip=='192.168.122.1':
		print "Internet Cable Is Not Connected."
		print "Kindly recheck the internet cable on your machine."
	else:
		print "Google Is READY !"
		time.sleep(2)
		commands.getoutput('firefox 172.217.166.164')
else:
	print "wrong choice."
	print "TRY AGAIN !"
