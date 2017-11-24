from escpos import printer
from escpos.escpos import EscposIO
class print_TM9:

    def __init__(self, *args):
        self.label = "Test Print"
        # Need to find the port for this printer
        self.print_port = "/dev/ttyx"


    def print_test(self):
        self.print_instance.text(self.label)
        with EscposIO(printer.Serial(self.print_port)) as p:
            p.set(font='a', height=2, align='right', text_type='bold')
            p.writelines('Test position and Font\n', font='b')

    def printWeighIn(self):
        self.print_instance = printer.Serial(self.print_port)

    def printWeighOut(self):
        self.print_instance = printer.Serial(self.print_port)
