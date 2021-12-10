# A code by Fávero Santos @ Curitiba, Paraná, Brazil in 09/12/2021

from pgdriver import PGDriver

def main():
    print("Main says: aloha!")


    myPGDriver = PGDriver()

    comPort = 'COM4'
    baudrate = 115200
    numberOfPulses = 1
    repetitionRate = 10000

    myPGDriver.connect(comPort, baudrate)
    myPGDriver.configure(numberOfPulses, repetitionRate)
    myPGDriver.enable()
    myPGDriver.disable()
    myPGDriver.disconnect()

    print("Main says: see you, space cowboy!")

if __name__ == '__main__':
    main()