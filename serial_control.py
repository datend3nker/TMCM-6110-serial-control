import serial
import re
#The name of the serial object hase to be "board", 9600 bit per secund and standard will be port "COM5" on windows and "//dev//ttyACM0" on linux!
def serial_setup(os, baud):
    port = 'COM5'
    if os == "win":
        port = 'COM5'
    else:
        port = '//dev//ttyACM0'
    try:
        global board 
        board = serial.Serial(port, baud)
    except:
        raise Exception("Wrong port or baud rate")
    return board.is_open

def serial_sendcommand(Address = 1, Command = 3, Type = 0, Motor = 0, Value = 0):
    instruction = [Address, Command, Type, Motor, "0x00", "0x00", "0x00", "0x00"]
    #prepeare the "Value" to be send
    hexValue = hex(Value) # convert value into a hex value
    hexval = hexValue.split('x') #removes the '0x'
    hexval.remove('0')
    hexval=" ".join(hexval)
    hexval= hexval[::-1]
    hexsplitval = re.findall('..?',hexval) #splits the hexpattern after every secund hexvalue 
    #__________________________________________________________________________________________________>
    #puts the "hexsplitval" into the instruction list in the right order
    try:
        countinstr = 7
        for x in hexsplitval:
            instruction[countinstr] = '0x' +(x[::-1])
            countinstr += -1
    except:
        raise Exception("The Value ",Value," is to big and can not be proccesed")
    #__________________________________________________________________________________________________>
    #converts the hex string into an integer
    try:
        countinstr = 7
        while countinstr >= 4:
              instruction[countinstr] = int(instruction[countinstr], base=16)
              countinstr += -1         
    except:
        raise Exception("Error in translating the hexstrin into an integer")
    #__________________________________________________________________________________________________>
    #calculates the checksum for the last bit
    try:
        checksum = 0
        for x in instruction:
            checksum += x
        if checksum >= 256:
            checksum += -256
        instruction.append(checksum)
    except:
        raise Exception("Error in calculating the checksum")
    board.write(instruction)

def serial_receive():
    counter = 0
    answerbin = [0, 0, 0,]
    answer = 0
    answerbin[0] = board.readline(1)
    answerbin[1] = board.readline(1)
    answerbin[2] = board.readline(1)
    answer = int.from_bytes( answerbin[2], "little")
    #__________________________________________________________________________________________________>
    #dictionary with all status codes wich could be possibly resived by the TMCM-6110
    status = {
        100: "Successfully executed, no error",
        101: "Command loaded into TMCL program EEPROM",
        1: "Wrong checksum",
        2: "Invalid command",
        3: "Wrong type",
        4: "Invalid value",
        5: "Con1guration EEPROM locked",
        6: "Command not available"}
    #__________________________________________________________________________________________________>
    return(status[answer])
#example#__________________________________________________________________________________________________>
