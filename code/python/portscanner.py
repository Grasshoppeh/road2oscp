#!/bin/python3

__author__ = 'Richard Ellis'
__credits__ = 'Heath Adams'
__version__ = '1.0'

#My first take on a quick port scanning script in python. Goal was the practice the usage of the socket library. I already had previosu knowlegdge of python.
#Areas that could be improved are an argument to 
# - scan the search space for ip addresses
# - multiproccessing on the socket_connect
# - using the time library to make it not run everything at once
# - for checking inet_aton grabing the failure execption and exiting? Not sure maybe in that case it better to traceback???

import sys
import socket
import argparse
from datetime import datetime

#Get arguments from the command line
parser = argparse.ArgumentParser()
parser.add_argument("ip", default='127.0.0.1', help='IP you want to scan')
parser.add_argument('-s', '--start', type=int, default=1, help='Port to start scanning from. Default 55')
parser.add_argument('-e', '--end', type=int, default=65535, help='Port to end scanning from. Default 85')
args = parser.parse_args()

if args.start > args.end or args.start < 1 or args.end < 1 or args.start > 65535 or args.end > 65535:
    sys.exit('Start/end arguments invalid logic')

#Scan in a given port range and ip
if socket.inet_aton(args.ip):
    target = socket.gethostbyname(sys.argv[1])

try:
    print("Starting scan")
    for port in range(args.start,args.end):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target,port))
        if result == 0:
            print("OPEN: port {openport} is open".format(openport=port))
        sock.close()
    print("Scan finished")
except KeyboardInterrupt:
    sys.exit("\nExiting program")
except socket.gaierror:
    sys.exit('\n Hostname could not be resolved.')
except socket.error:
    sys.exit('\nCouldnt connect to server.')

