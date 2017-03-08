from magma import Peripheral
from mantle import Counter

class Timer(Peripheral):
    def __init__(self, fpga, name='systimer', n=32):
        Peripheral.__init__(self, fpga, name)
        self.n = n

    def bits(self, n):
        self.n = n
        return self

    def on(self):
        self.fpga.clock.on()
        Peripheral.on(self)
        return self

    def setup(self, main):
        setattr(main, self.name, Counter(self.n))
