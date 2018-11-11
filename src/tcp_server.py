#!/usr/bin/python2.7
import socket
import sys
import traceback
import threading


class Client(threading.Thread):
    """
    Cliente conectado al server 
    """
  
    def __init__(self, socket_cliente, datos_cliente):
        
        threading.Thread.__init__(self)
        self.conn = socket_cliente
        self.datos_str = datos_cliente[0] + ":" + str(datos_cliente[1]) # Datos del cliente
        print("El cliente " + self.datos_str + " se ha conectado")

    def run(self):
        """
        Una vez hecha la conexion se reciben los datos
        """  
        while True:
            # recibe texto del cliente
            data = self.conn.recv(1024)
            print("received: "+data)

            # devuelve texto en mayusculas
            self.conn.send(data.upper())

            # revisa por conexion terminada
            if data == '':
                print('Conexion con ' + self.datos_str + ' terminada')
                break

        self.conn.close()


def main():
    """
    Programa principal
    """
    host = 'localhost'
    port = 50007
    clients = [] # lista de clientes

    # crea el socket de bienvenida
    s = socket.socket()
    print('Socket de bienvenida creado')

    s.bind((host,port)) # asocia el socket a un puerto

    print('Se escuchan conexiones entrantes')
    s.listen(0)

    while True:
        try:
            # espera por una solicitud de conexion
            socket_cliente, datos_cliente = s.accept()
            #print('Conectado con %s : %s' % (addr[0],str(addr[1])))
        except (KeyboardInterrupt, Exception):
            print('')
            traceback.print_exception(*sys.exc_info())
            s.close()
            print("Exiting")
            quit(1)

        hilo_cliente = Client(socket_cliente, datos_cliente)
        hilo_cliente.start()
        clients.append(hilo_cliente) #Ingresa el cliente en la lista  

if __name__ == "__main__": 
    main() 
