#!/usr/bin/python2.7
import socket
import sys
import traceback

host = 'localhost'
port = 50007

try:
    # crea el socket de bienvenida
    s = socket.socket()
    print('Socket de bienvenida creado')
    
    s.bind((host,port)) # asocia el socket a un puerto
    
    s.listen(0)
    
    # espera por una solicitud de conexion
    conn, addr = s.accept()
    print('Conectado con %s : %s' % (addr[0],str(addr[1])))
    
    while True:
        # recibe texto del cliente
        data = conn.recv(1024)
        print("received: "+data)
        
        # devuelve texto en mayusculas
        conn.send(data.upper())
        
        # revisa por conexion terminada
        if data == '':
            print('Conexion terminada')
            break
    
    s.close()

except (KeyboardInterrupt, Exception):
    print('')
    traceback.print_exception(*sys.exc_info())
    s.close()
    print("Exiting")

