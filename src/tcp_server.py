#!/usr/bin/python2.7
import socket
import sys
import traceback
import threading

ansi_colors = [
    '\033[1;32m', # ANSI_GREEN
    '\033[1;31m', #  ANSI_RED
    '\033[1;35m', # ANSI_PURPLE
    '\033[1;33m', # ANSI_YELLOW
    '\033[1;34m', # ANSI_BLUE
    '\033[0m' # ANSI_NOCOLOR
]


class Client(threading.Thread):
    """
    Cliente conectado al server 
    """
  
    def __init__(self, socket_cliente, datos_cliente, color=ansi_colors[-1]):
        
        threading.Thread.__init__(self)
        self.conn = socket_cliente
        self.datos_str = datos_cliente[0] + ":" + str(datos_cliente[1]) # Datos del cliente
        self.color=color
        print(self.color+"El cliente " + self.datos_str + " se ha conectado"+ansi_colors[-1])

    def run(self):
        """
        Una vez hecha la conexion se reciben los datos
        """  
        while True:
            # recibe texto del cliente
            data = self.conn.recv(1024)
            print(self.color+"received: "+data+ansi_colors[-1])

            # devuelve texto en mayusculas
            self.conn.send(data.upper())

            # revisa por conexion terminada
            if data == '':
                print(self.color+'Conexion con ' + self.datos_str + ' terminada'+ansi_colors[-1])
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

    try:
        s.bind((host,port)) # asocia el socket a un puerto
    except (Exception):
        print('')
        traceback.print_exception(*sys.exc_info())
        s.close()
        print("El socket " + str(host) + ':' + str(port) + " ya esta en uso")
        sys.exit(2)

    print('Se escuchan conexiones entrantes')
    s.listen(0)

    while True:
        try:
            # espera por una solicitud de conexion
            socket_cliente, datos_cliente = s.accept()
        except (KeyboardInterrupt):
            print("\nExiting")
            s.close()
            sys.exit(0)
        except (Exception):
            print('')
            traceback.print_exception(*sys.exc_info())
            s.close()
            sys.exit(1)

        hilo_cliente = Client(socket_cliente,
                              datos_cliente,
                              ansi_colors[len(clients)])
        hilo_cliente.start()
        clients.append(hilo_cliente) #Ingresa el cliente en la lista  

if __name__ == "__main__": 
    main() 
