#/bin/python3
# TODO: Make a local version (maybe, or just get rid of the option aspect); make an option to save; Also do some maintenance in case of bad characters, if there is a space in the hostname it won't do an opsdb query, etc.
# TODO: Perhaps make this a legacy thing to MASH, allow console, set clone bit, add some OSTK stuff
import os
import sys
import subprocess
import pwd
import getpass
from socket import *


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



# Greet the user and EULA

newline = "\n"
print(newline)
print("*********************************************************************************************************************")
print("Hello " + os.environ['USER'] + " ,this script goes through all the basic locations for HW error reporting." + newline + "Please only use this tool on hosts you have permission for! Enjoy :)" )
print("*********************************************************************************************************************")

print(newline + newline)


remote_usage = input("Would you like to run this as a remote tool? ")

if remote_usage =='yes':
	hostname = input("Great, let me start by getting your hostname! ")
	print("Looks good to me, next let's see what you want to do")
	host = hostname
	print("Great, thank you. Let's look up this host real quick")

	# Get info on the host
	subprocess.run(["opsdb", "--fqdn", host, "--getentry", "locroom,locarea,locrow,locrack,locshelf,ytag,serialno,mac,manufacturer,model,eow_time,netswitch,sport,is_openstack_managed"])

	print(newline + "That sure is a host, let's see what's going on with it")

	# Open a file in users home directory for the option to save, and also to clean up the output of mote
	f = open("hwcheck.txt", "w")

	#Run mote on the host
	subprocess.run(["mote", "-r", host, "-C", "/home/dmakowski/hwchecks.sh"], stdout=f)

	print(newline + "There you go, take a look and see what you can find out.")

	#Clean up the dirty output of mote
	p1 = "cat hwcheck.txt | cut -d':' -f2-10"
	p2 = os.system(p1)
	print(p2)

if remote_usage == 'no':
#  print("Then please upload this tool to your affected host and run it locally on there, have a great day!")
  sys.exit(0)

else:
  sys.exit(0)
