# import serial module to communicate with arduino
import serial
import json
import encodings


# declare COm PORT AND baud rate

global COMPORT
global BAUDRATE

COMPORT='COM8'
BAUDRATE=9600

# define a function to read data
def read_serial():


    # use try and except block t avoid run time errors
    try:
        arduinodata=serial.Serial(COMPORT, BAUDRATE, timeout=1)

        while arduinodata.inWaiting:            # check if data is coming
            data=arduinodata.readline()         # read line by line data
            data=data.decode('ascii')           # decode data into ascii
            print("Arduino says ", data)        # print data
    except:
        print('Cannot read Data from Com Port')

def write_data():
    # always use try and except block while writing a function
    try:

        user_input=input(' Enter Data !')       # define data that user will input

        arduinodata=serial.Serial(COMPORT,BAUDRATE,timeout=1) # define object to communicate

        data_send=user_input.encode('utf-8')   # before sending data you have to encode the data
        arduinodata.write(data_send)           # after encoding data send it to Controller
    except:
        print('Error Cannot Send Data ! ')


if __name__ == '__main__':               # check if its main  file
    read_serial()                        # run main loop

