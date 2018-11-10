#!/usr/bin/python2.7
import time
import socket
import string
import sys
import traceback
from random import *

min_char = 8
max_char = 12

def random_str():
    """
    Genera un string de caracteres aleatorios con una longitud de
    entre [min_char, max_char].
    """
    allchar = string.ascii_letters
    rs = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return rs

# direccion de loopback
host = 'localhost'

# puerto del servidor
port = 50008

# crea un socket usando direcciones IP (opcion AF_INET) y
# usando una comunicacion de datagramas mediante UDP (opcion SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        s.sendto('cliente: %s' % (random_str().lower()), (host,port))
        print("response: "+s.recv(1024))
        time.sleep(2)

except (KeyboardInterrupt, Exception):
    print('')
    traceback.print_exception(*sys.exc_info())
    s.close()
    print("Exiting")


