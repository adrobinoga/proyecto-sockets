#!/usr/bin/python2.7
import socket
import sys
import traceback

host = 'localhost'
port = 50008

try:
    # crea un socket usando direcciones IP (opcion AF_INET) y
    # usando una comunicacion de datagramas mediante UDP (opcion SOCK_DGRAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.bind((host,port)) # asocia el socket a un puerto
    
    while True:
        # recibe texto del cliente
        (data,address) = s.recvfrom(1024)
        print("received: %s, from: %s" % (data,address))
        
        # devuelve texto en mayusculas al mismo socket del que recibio
        s.sendto(data.upper(),address)

except (KeyboardInterrupt, Exception):
    print('')
    traceback.print_exception(*sys.exc_info())
    s.close()
    print("Exiting")

