import socket
import threading  # Use the threading module instead of _thread
import sys

# Server configuration
server = ""
port = 5555

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server and port
try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))
    sys.exit()

# Start listening for connections
s.listen(2)  # Allow up to 2 clients to connect
print("Waiting for a connection, Server Started")

def threaded_client(conn):
    conn.send(str.encode("Welcome to the server!"))  # Send a welcome message
    while True:
        try:
            data = conn.recv(2048)  # Receive data from the client
            if not data:
                print("Disconnected")
                break
            print("Received: ", data.decode())  # Print the received data
            conn.send(data)  # Echo the received data back to the client
        except:
            break

    conn.close()  # Close the connection when done
    print("Connection closed.")

while True:
    conn, addr = s.accept()  # Accept a new connection
    print("Connected to: ", addr)
    
    # Start a new thread for the client using threading.Thread
    client_thread = threading.Thread(target=threaded_client, args=(conn,))
    client_thread.start()