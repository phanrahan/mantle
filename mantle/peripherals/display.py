from copy import deepcopy
from magma import *
from mantle import *

__all__ = ['DisplayRefresh']

#      a
#     ---
#  f |   | b
#     -g-
#  e |   | c
#     ---    . dp
#      d

# common anode
ca = [[1, 1, 1, 1, 1, 1, 0, 0],
      [0, 1, 1, 0, 0, 0, 0, 0],
      [1, 1, 0, 1, 1, 0, 1, 0],
      [1, 1, 1, 1, 0, 0, 1, 0],
      [0, 1, 1, 0, 0, 1, 1, 0],
      [1, 0, 1, 1, 0, 1, 1, 0],
      [1, 0, 1, 1, 1, 1, 1, 0],
      [1, 1, 1, 0, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 0, 1, 1, 0],
      [1, 1, 1, 0, 1, 1, 1, 0],
      [0, 0, 1, 1, 1, 1, 1, 0],
      [1, 0, 0, 1, 1, 1, 0, 0],
      [0, 1, 1, 1, 1, 0, 1, 0],
      [1, 0, 0, 1, 1, 1, 1, 0],
      [1, 0, 0, 0, 1, 1, 1, 0]]

cc = deepcopy(ca)

for i in range(16):
    s = ca[i]
    t = cc[i]
    for j in range(len(s)):
        t[j] = 1 - s[j]


def hex4seg8(mode="CC"):
    rom = cc if mode == 'CC' else ca
    return ROM16xN(rom)


def Refresh(digits, refresh, mode="CC"):
    """
    A 4-digit LED display.

    refresh is 2-bits
    """

    # Mux(height, width) -> [I, S]
    mux = Mux(4,4)
    digit = mux(digits[0], digits[1], digits[2], digits[3], refresh)

    segment8 = hex4seg8()
    segment8(digit)

    decode4 = Decoder(2, invert=(mode == 'CC'))
    decode4(refresh)

    return segment8, decode4


class DisplayRefresh(Peripheral):
    name = 'DisplayRefresh'

    IO = ["output cathodes", Array(8,Bit), "output anodes", Array(4,Bit)]

    def __init__(self, fpga, name='display'): 
        Peripheral.__init__(self, fpga, name)

    def on(self):
        for i in range(8):
            gpio = self.cathodes[i].getgpio()
            gpio.output().on()
        for i in range(4):
            gpio = self.anodes[i].getgpio()
            gpio.output().on()

        Peripheral.on(self)
        return self

    def setup(self, main):
        TIMER = main.systimer.O
        A4 = In(Array4)
        DIGITS = array(A4(), A4(), A4(), A4())

        cathodes, anodes = Refresh( DIGITS, TIMER[16:18] )

        wire( cathodes, main.CATHODES )
        wire( anodes,   main.ANODES )

        display = AnonymousCircuit(
                    "digit0", DIGITS[0],
                    "digit1", DIGITS[1],
                    "digit2", DIGITS[2],
                    "digit3", DIGITS[3])

        #main.DIGITS = DIGITS

        setattr(main, self.name, display)
