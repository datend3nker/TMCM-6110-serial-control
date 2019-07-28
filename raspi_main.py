from serial_control import *
from bluetooth_server import *
try:
    serial_setup('linux', 9600)
    bt = btserver_setup()
    server = bt[1]
    print(bt[2])
except:
    raise Exception("Culdn't connect to port")
while True:
    test = btserver_receive()
    if test == b'GOTO_0':
        serial_sendcommand(1, 4, 0, 0, 0)
        pass
    elif test == b'GOTO_1':
        serial_sendcommand(1, 4, 0, 0, 500000)
        pass
    elif test == b'EXIT':
        break
    else:
        client.send('Unknown Command')
        print("Unknown command")