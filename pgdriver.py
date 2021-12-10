# A code by Fávero Santos @ Curitiba, Paraná, Brazil in 09/12/2021

import serial
import time

DEBUG_MODE = True

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
            raise Exception("Erro ao inicializar a porta: " + self.port)
        time.sleep(1)

        if DEBUG_MODE:
            print("Pulse Generator Driver: conectado!")

    def configure(self, nPulses, repRate):
        self.numberOfPulses = nPulses
        self.repetitionRate = repRate

        message = "frequency:" + str(self.repetitionRate) + "\r\n"
        try:
            self.handler.write(message.encode())
        except Exception as e:
            raise Exception("Erro ao escrever a frequência!")
        time.sleep(1)

        message = "pulse:" + str(self.numberOfPulses) + "\r\n"
        try:
            self.handler.write(message.encode())
        except Exception as e:
            raise Exception("Erro ao escrever a quantidade de pulsos!")
        time.sleep(1)

        if DEBUG_MODE:
            print("Pulse Generator Driver: configurado!")

    def enable(self):
        message = "enable" + "\r\n"
        try:
            self.handler.write(message.encode())
        except Exception as e:
            raise Exception("Erro ao escrever 'enable'")
        time.sleep(1)

        if DEBUG_MODE:
            print("Pulse Generator Driver: enabled!")

    def disable(self):
        message = "disable" + "\r\n"
        try:
            self.handler.write(message.encode())
        except Exception as e:
            raise Exception("Erro ao escrever 'disable'")
        time.sleep(1)

        if DEBUG_MODE:
            print("Pulse Generator Driver: disabled!")

    def disconnect(self):
        try:
            self.handler.close()
        except Exception as e:
            raise Exception("Erro ao fechar a porta " + self.port)
        time.sleep(1)

        del self.handler

        if DEBUG_MODE:
            print("Pulse Generator Driver: disconnected!")
