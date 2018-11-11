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
port = 50007

# crea un socket usando direcciones IP (opcion AF_INET) y
# usando una comunicacion confiable mediante TCP (opcion SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# se conecta al servidor
s.connect((host , port))

print('Conectado a %s' % (host))

try:
    while True:
        s.send('cliente: %s' % (random_str().lower()))
        print("response: "+s.recv(1024))
        time.sleep(2)

except (KeyboardInterrupt):
    print("\nExiting")
    s.close()
    sys.exit(0)
except (Exception):
    print('')
    traceback.print_exception(*sys.exc_info())
    s.close()
    sys.exit(1)
