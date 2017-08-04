##Created by FransHBotes
##Usage: 
##Synops: Use the attack for diversion, test response of security systems.
##        Several companies still make use of file drops and pickups to transfer data, when
##        access to the specified location is denied,  business operations can be stalled.
##        Without knowing the network by heart this offers an easy attack method. 
##Version: 0.1       
##Parameters: $crawl_limit: set amount of computers to extract from AD, 0 extracts all.
## Be prepared to wait when extracting all computers.
##
##
##IMPORTS##
import subprocess
import sys
import socket
import time
import signal
from timeit import default_timer as timer


##PARAMETERS##
crawl_limit = "15000"
ds_query = "dsquery * -filter (objectclass=computer) -attr dNSHostName  -limit " + crawl_limit
domain_comps = []
active_comps = []
file_shares = {}
host_name = ''
port = 80
pingpassed = 0
pingfailed = 0
maxCount = 20

def main_function():
##INITIATE PROGRAM##
  try:
    print("ShareAttack! Launched")
    print("Gathering AD information....")
    signal.signal(signal.SIGINT, signal_handler)
##CRAWL ACTIVE DIRECTORY FOR ALL COMPUTERS##
    domain_comps  = subprocess.check_output(ds_query,universal_newlines=True).splitlines()
##ONLY KEEP LIVE COMPUTERS##
    for comp in range(1, len(domain_comps)):
      host_name = domain_comps[comp]
      ping_host(host_name)
    print ("Active computers found!")
    print(active_comps) 
	
##USE CUSTOM MADE SHARELOCATOR TO LOCATE THE FILESHARES FOR ALL THE COMPUTERS##
    print(".........")
    print("Launching ShareLocator")
    for acomp in range(0, len(active_comps)):
      activecomp = active_comps[acomp]
      print("ShareLocator " + activecomp)
      ShareLocator = "ShareLocator " + activecomp
      file_shares[activecomp] =  subprocess.check_output(ShareLocator,universal_newlines=True).split(',')

    print("Shares Found!")
    print(file_shares) 

  except subprocess.CalledProcessError:
    pass

#**********************************************************************#
def signal_handler(signal, frame):
    """ Catch Ctrl-C and Exit """
    sys.exit(0)


def ping_host(hostname):
  count = 0
  try:
    current_IP = socket.gethostbyname(hostname.strip())
    if current_IP != '':
      active_comps.append(current_IP)

  except socket.gaierror:
    pass
    
 #**********************************************************************#
if __name__ == '__main__':
    main_function()
