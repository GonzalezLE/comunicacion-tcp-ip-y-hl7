import socket
import time
server_address = ('127.0.0.1', 55687)

obj = socket.socket()

obj.connect(server_address)
print("Conectado al servidor")
 
while True:
  time.sleep(5)
  mens = "Hola soy el cliente"
  obj.send(mens)
  respuest_servidor=obj.recv(1024)
  print(respuest_servidor)
#Cerramos la instancia del objeto servidor
obj.close()

#Imprimimos la palabra Adios para cuando se cierre la conexion
print("Conexion cerrada")