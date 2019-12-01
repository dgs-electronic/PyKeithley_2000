import serial

class Keithley2000:
    def __init__(self, instrument):
        self.dmm = instrument
        self.dmm.baudrate = 19200
        self.dmm.termination = '\n'
        self.dmm.timeout = 10

    def getidentity(self):
        self.dmm.write(b'*IDN?\n')
        return self.dmm.readline()

    def reset(self):
        self.dmm.write(b'*RST\n')

    def setRemote(self):
        self.dmm.write(b':SYST:REM\n')

    def setLocal(self):
        self.dmm.write(b':SYST:LOC\n')

    def read(self):
        self.reset()
        self.dmm.write(b':READ?\n')
        val = self.dmm.readline()
        return float(val)

#main
ser = serial.Serial('/dev/ttyUSB0',19200)  # open serial port

MM = Keithley2000(ser)
print(MM.getidentity())

print(MM.read())

#ser.baudrate = 19200
#ser.timeout = 10
#ser.termination = '\n' #Linefeed als Zeilenende


#ser.write(b':MEAS:VOLT:DC?\n')
#print(ser.readline())

#ser.write(b':SYST:LOC\n')

MM.setLocal()
ser.close()