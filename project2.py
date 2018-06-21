#!usr/bin/python2

import commands
import time
import webbrowser

menu='''
press 1 to check current time and date
press 2 to scan all your MAC address in your  connected network
press 3 to shutdown your machine in 15 minute
press 4 to search something on google
press 5 to logout from your current machine
press 6 to shutdown all connected system in your network
press 7 to update status in facebook 
press 8 to list ip addresss of given website
'''

print menu
choice=raw_input("Enter your choice: ")

print " 			********************************* 			"

if choice == '1' :
	print "current date and time is "
	print time.ctime()

elif choice == '2' :
	print
	x=commands.getoutput('cat /sys/class/net/*/address')
	print x

elif choice == '3' :
	print "your machine will be shutdown after 1 minutes. plz save your data...."
	commands.getoutput("sudo shutdown +1")

elif choice == '4' :
	find=raw_input("enter your query : ")
	print "your query is searching on google plz wait..."
	webbrowser.open_new_tab("https://www.google.com/search?q="+find)

elif choice == '5' :
	print "logouting your current machine"
	commands.getoutput('logout')

elif choice == '6' :
	print "shutdown all connected system in your network"
	

elif choice == '7' :
	print "upate status in facebook"
	username=raw_input("enter your username : ")
	passwd=raw_input("enter your password : ")	
	webbrowser.open_new_tab(" ")


elif choice == '8' :
	web=raw_input("enter your website : ")
	ip=commands.getoutput("host "+web)
	print ip

else :
	print "wrong choice"
	print "TRY AGAIN !"
