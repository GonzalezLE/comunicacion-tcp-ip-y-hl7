import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.listen(1)
# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 55687)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data connection.recv(1024)
    data = sock.recv(1024)
    message = 'Hola soy el cliente'
    #sock.sendall(message)
    sock.send(message)



finally:
    print('closing socket')
    sock.close()