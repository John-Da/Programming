import socket
from _thread import *
import sys


server = "192.168.178.97"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))


s.listen(2) # empty -> multi clients 
print("Waiting for a connection, Server Started")


pos = [(0, 0), (100, 100)]
def threaded_client(conn):
    conn.send(str.encode('Connected'))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            
            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client,(conn,))