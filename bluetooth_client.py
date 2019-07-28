from bluetooth import *

def btclient_setup(host = 'B8:27:EB:32:E3:27', port = 1):
    try:
        global client_sock
        client_sock=BluetoothSocket( RFCOMM )
        client_sock.connect((host, port))
    except:
        raise Exception("Couldn't setup the client socket")
    return client_sock, True, port, 

def btclient_send(message):
    client_sock.send(message)
    return True