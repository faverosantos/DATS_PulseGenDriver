# A code by Fávero Santos @ Curitiba, Paraná, Brazil in 09/12/2021

import serial
import time

DEBUG_MODE = False

class PGDriver:

    handler = 0
    baudrate = 0
    port = "noPort"
    numberOfPulses = 0
    repetitionRate = 0

    def __init__(self):
        pass

    def connect(self, comPort, baud):
        self.baudrate = baud
        self.port = comPort

        try:
            self.handler = serial.Serial(comPort, baud)
        except Exception as e:
            raise Exception("Exception: error while initializing port " + self.port) + "."
        time.sleep(1)

        if DEBUG_MODE:
            print("DEBUG_MODE: Pulse Generator Driver: connected.")

    def configure(self, nPulses, repRate):
        if 14 >= nPulses >= 1:
            self.numberOfPulses = nPulses
        else:
            self.numberOfPulses = 14
            print("WARNING: number of pulses set to 14.")

        if 100000 >= repRate >= 10:
            self.repetitionRate = repRate
        else:
            self.repetitionRate = 100000
            print("WARNING: repetition rate set to 100 kHz.")

        message = "frequency:" + str(self.repetitionRate) + "\r\n"
        try:
            self.handler.write(message.encode())
        except Exception as e:
            raise Exception("Exception: error while trying to write frequency value.")
        time.sleep(1)

        message = "pulse:" + str(self.numberOfPulses) + "\r\n"
        try:
            self.handler.write(message.encode())
        except Exception as e:
            raise Exception("Exception: error while trying to write number of pulses.")
        time.sleep(1)

        if DEBUG_MODE:
            print("DEBUG_MODE: Pulse Generator Driver: configured.")

    def enable(self):
        message = "enable" + "\r\n"
        try:
            self.handler.write(message.encode())
        except Exception as e:
            raise Exception("Exception: error while writing 'enable'.")

        time.sleep(1)

        if DEBUG_MODE:
            print("DEBUG_MODE: Pulse Generator Driver: enabled.")

    def disable(self):
        message = "disable" + "\r\n"
        try:
            self.handler.write(message.encode())
        except Exception as e:
            raise Exception("Exception: error while writing 'disable'.")
        time.sleep(1)

        if DEBUG_MODE:
            print("DEBUG_MODE: Pulse Generator Driver: disabled.")

    def disconnect(self):
        try:
            self.handler.close()
        except Exception as e:
            raise Exception("Exception: error while trying to close port " + self.port + ".")
        time.sleep(1)

        del self.handler

        if DEBUG_MODE:
            print("DEBUG_MODE: Pulse Generator Driver: disconnected.")
