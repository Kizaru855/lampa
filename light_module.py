from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

app = QtWidgets.QApplication([])
ui = uic.loadUi("UI.ui")
ui.setWindowTitle("Световой модуль")

serial = QSerialPort()
serial.setBaudRate(115200)  #скорость опроса
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portList.append(port.portName())
ui.comL.addItems(portList)

def onOpen():
    serial.setPortName(ui.comL.currentText())
    serial.open(QIODevice.ReadWrite)

def onClose():
    serial.close()

def SerialSend(data):   #список int
    txs = ""
    for value in data:
        txs += str(value)
        txs += ','
    txs = txs[:-1]
    txs += ';'
    serial.write(txs.encode())

def lamp_control(val):
    SerialSend([0, val])

def servo1_control(val):
    SerialSend([1, val])

def servo2_control(val):
    SerialSend([2, val])

#serial.readyRead.connect(onRead)

ui.openB.clicked.connect(onOpen)
ui.closeB.clicked.connect(onClose)

ui.lampdial.valueChanged.connect(lamp_control)
ui.servo1.valueChanged.connect(servo1_control)
ui.servo2.valueChanged.connect(servo2_control)

ui.show()
app.exec()
