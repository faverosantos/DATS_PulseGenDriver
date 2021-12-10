# DATS_PulseGenDriver
A simple driver for the PulseGen board V00 R00. \
A code made by Fávero Santos @ Curitiba, Paraná, Brazil in 10/12/2021. \
favero.santos@gmail.com

# Requirements
pyserial 3.5 \
python-dateutil 2.8.1

# About

A ideia desse código é prover ao usuário uma API de integração com a placa Pulse Gen V00 R00. Atualmente, apenas os canais 0 e 1 estão habilitados por padrão no produto.

Modo de usar

1. Importar o módulo pgdriver.py usando "from pgdriver import PGDriver".

2. Instanciar um objeto do tipo PGDriver usando "myPGDriver = PGDriver()"

3. Chamar as funções na ordem:

i. myPGDriver.connect(comPort, baudrate) - conecta com a porta serial \
i.i. comPort é uma string da porta a ser utilizada, por exemplo, COM4) \
i.ii. baudrate é a taxa de comunicação dados, por padrão 115200


ii. myPGDriver.configure(numberOfPulses, repetitionRate) - configura a operação do gerador de pulsos \
ii.i. numberOfPulses é a quantidade de pulsos concatenados de 6 ns em 6 ns. Mínimo 1, máximo 14. \
ii.ii. repetitionRate é a taxa com que os pulsos concatenados serão repetidos. Mínimo 10 Hz, Máximo 100 kHz. \

iii. myPGDriver.enable() - habilita a geração dos pulsos

iv. myPGDriver.disable() - desabilita a geração dos pulsos

v. myPGDriver.disconnect() - deconecta a serial

Cada uma das funções possui um sleep de 1 segundo após serem chamadas como medida de proteção contra command spamming.

# Código exemplo
Um código exemplo é fornecido com essa API em formato de módulo Python. O usuário poderá rodar main.py e verificar com um osciloscópio a aplicação do circuito.