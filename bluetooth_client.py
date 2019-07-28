from bluetooth import *
import sys
host = 'B8:27:EB:32:E3:27'
port = 1
# Create the client socket
try:
    sock=BluetoothSocket( RFCOMM )
    sock.connect((host, port))
except:
    raise Exception("Couldn't setup the client socket")
sock.send("Hello World!")
sock.close()