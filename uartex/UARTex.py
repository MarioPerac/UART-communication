from threading import Thread, Lock
from uartex.Parameters import *
import uartex.UART as UART
import time


class SetOfParameters:
    quaternionParam = QuaternionParam(0, 0, 0, 0)
    lock_set = Lock()

    @staticmethod
    def quaternion_parameters():
        with SetOfParameters.lock_set:
            q0, q1, q2, q3 = SetOfParameters.quaternionParam.parameters

        return q0, q1, q2, q3

    @staticmethod
    def input_parameters_in_set(q0, q1, q2, q3):
        with SetOfParameters.lock_set:
            SetOfParameters.quaternionParam.set_parameters(q0, q1, q2, q3)


class PositionOfBaseReceiver(Thread):
    serial_object = None
    start_char = '<'
    end_char = '>'
    separator = '|'
    uart_port = None
    baud_rate = None
    END = False
    CALIBRATION = False

    def __int__(self):
        Thread.__init__(self)

    @staticmethod
    def set_serial_object(serial_object):
        PositionOfBaseReceiver.serial_object = serial_object

    @staticmethod
    def close_communication():
        PositionOfBaseReceiver.END = True

    @staticmethod  # message type <|q0|q1|q2|q3|>
    def parse_message(message):
        values = message.split(PositionOfBaseReceiver.separator)
        q0 = 0
        q1 = 0
        q2 = 0
        q3 = 0

        if len(values) == 6:
            q0 = float(values[1])
            q1 = float(values[2])
            q2 = float(values[3])
            q3 = float(values[4])

        return q0, q1, q2, q3

    def run(self):

        while not PositionOfBaseReceiver.END:
            message = UART.read_until_end_char(PositionOfBaseReceiver.serial_object,
                                               PositionOfBaseReceiver.start_char,
                                               PositionOfBaseReceiver.end_char)
            q0, q1, q2, q3 = PositionOfBaseReceiver.parse_message(message)

            if q0 != 0 or q1 != 0 or q2 != 0 or q3 != 0:
                SetOfParameters.input_parameters_in_set(q0, q1, q2, q3)
                time.sleep(0.01)  
        if PositionOfBaseReceiver.serial_object.is_open:
            PositionOfBaseReceiver.serial_object.close()
