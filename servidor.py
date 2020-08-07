import socket
import time
#instanciamos un objeto para trabajar con el socket
server_address = ('127.0.0.1', 55687)
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#Puerto y servidor que debe escuchar
ser.bind(server_address)
print('starting up on {} port {}'.format(*server_address))
#Aceptamos conexiones entrantes con el metodo listen. Por parametro las conexiones simutaneas.
ser.listen(1)
 
#Instanciamos un objeto cli (socket cliente) para recibir datos
cli, addr = ser.accept()

'''
esta es una simulacion de la respuesta que vendra del equipo
'''
mensaje='MSH|^~\&|cobas infinity 2.5|Roche Diagnostics|Receiver Application|Receiver Facility|20200616122014||OUL^R21^OUL_R21|6FE5440F-8043-41FB-8E19-47E7EEAD01EB|P|2.3|||ER|ER||8859/1'
mensaje+='PID|1'
mensaje+='ORC|RE|PCCC2-ISE1|||IP||^^^^^^R'
mensaje+='OBR|1|PCCC2-ISE1||ALL|||||||||||^^^^^^Q||||||||||||^^^^^R'
mensaje+='OBX|1||109||99|ng/mL||Normal, No Alarm|PCCC2_001-L1^CS-cobas6kv2-1-ISE1-R1-GLU-L1|A^3|F|||20200616121951|^^^C6K-ISE1.800|||800.800'


while True:
  time.sleep
  #time.sleep(5)
  recibido = cli.recv(1024)
  print(recibido)
  print ("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))
  
  #manda mensaje al cliente
  cli.send(mensaje)
cli.close()
ser.close()

print("Conexiones cerradas")