from magma import *

__all__ = ['_DCM', 'DCM']

_DCM = DeclareCircuit('DCM',
            "CLKIN", In(Bit),
            "CLKFB", In(Bit),
            "PSCLK", In(Bit),
            "PSEN", In(Bit),
            "PSINCDEC", In(Bit),
            "RST", In(Bit),
            "CLKFX", In(Bit))

def DCM( freq, basefreq=32):

    """
    Instantiate a Digital Clock Manager

    >>> DCM(freq,basefreq=32)

    O's clockrate is freq (in Mhz). clockin should be set to
    the frequency of the input clock.
    """

    (mult, div), bestfreq = findbestclock(freq, basefreq)
    if freq != bestfreq:
        print("%d * %d / %d (%g) ~= %g" % (basefreq,
                                           mult,
                                           div,
                                           bestfreq,
                                           freq))

    params = {}
    params["CLK_FEEDBACK"] = '"NONE"'
    params["CLKFX_DIVIDE"] = str(div)
    params["CLKFX_MULTIPLY"] = str(mult)
    params["DUTY_CYCLE_CORRECTION"] = '"FALSE"'
    params["STARTUP_WAIT"] = '"FALSE"'
    #params["X_CLKIN_PERIOD"] = '"31.25"'
    #for attr in ["PSEN", "PSINCDEC", "RST", "PSCLK"]:
    #    params[attr + "INV"] = '"%s"' % attr

    dcm = _DCM(**params)
    for attr in ["PSEN", "PSINCDEC", "RST", "PSCLK"]:
        wire(GND, getattr(dcm, attr))
    wire(GND, dcm.CLKFB)

    return AnonymousCircuit("input I", dcm.CLKIN, "output O", dcm.CLKFX)


def findbestclock(freq, basefreq):
    bestfreq = freq
    bestdiff = 1024.
    bestclock = None
    for i in range(2, 33):
        f1 = basefreq * i
        for j in range(1, 33):
            f2 = f1 / float(j)
            diff = abs(f2 - freq)
            if diff < bestdiff:
                bestdiff = diff
                bestfreq = f2
                best = (i, j)
    return best, bestfreq

if __name__ == '__main__':
    from parts.xilinx.spartan6.primitives.BUF import BUFG
    d = DefineCircuit('main', "input CLKIN", Bit, "output CLKOUT", Bit)
    dcm = DCM(50)
    bufg = BUFG()
    wire(d.CLKIN, dcm.I)
    wire(dcm, bufg)
    wire(bufg, d.CLKOUT)
    EndCircuit()
    compiledefinitions('main.v', d)
