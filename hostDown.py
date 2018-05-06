#/bin/python3
# TODO: Make a check for "sudo ipmitool sel elist | tail -20"; Make a check for sudo cat /var/log/messages|[mcelog]; uptime; sudo -l (to print for the user in case tools are in different locations); 
#Also need to look into making this remote... perhaps just running mote, provide options for either specific tools or just a gambit
import os
import subprocess
import pwd
from socket import *


# Greet the user and EULA

newline = "\n"
print(newline)
print("Hello " + os.environ['USER'] + " ,this script goes through all the basic locations for HW error reporting." + "\n" + "Please only use this tool on hosts you have permission for! Enjoy :)" )

print(newline + newline)


remote_usage = input("Would you like to run this as a remote tool? ")

if remote_usage == 'no':
  print("Then please upload this tool to your affected host and run it locally on there, have a great day!")
  sys.exit(0)
if remote_usage =='yes':
  host = input("Great, let me start by getting your hostname!")
  print("Looks good to me, next let's see what you want to do")
  
    
  
else:
  sys.exit(0)
  


#subprocess.run(["sudo", "-l"])
#print(newline)


# Start with sudo hwconfig


#subprocess.run(["sudo", "hwconfig"])
#print(newline)

#subprocess.run(["sudo ipmitool sel elist | tail", "-20"])
