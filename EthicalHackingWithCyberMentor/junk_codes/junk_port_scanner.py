#!/bin/python3


import sys
import socket
from datetime import datetime

if (len(sys.argv) == 2):
    target = socket.gethostbyname(sys.argv[1])
    
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 junk_scanner.py <IP>")
    sys.exit()


print("-" * 50)
print("Scanning target: " + target)
print("Started: "+ str(datetime.now))
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))   
        print("Scanning port " + str(port) + "...")
        if result == 0:
            print("Port " + str(port) + " is open!")
        s.close()
except KeyboardInterrupt:
    print("\nExiting program!")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved!")
    sys.exit()

except socket.error:
    print("Socket in error!")
    sys.exit()
