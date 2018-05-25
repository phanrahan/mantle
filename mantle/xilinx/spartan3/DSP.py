class MULT18X18():

    def __init__(self, clk=True, site=None, **kwargs):
        self.inst = inst("MULT18X18SIO", site, **kwargs)

        self.setcfgs({
            "AREG": "0",
            "BREG": "0",
            "B_INPUT": "DIRECT",
            "CEAINV": "CEA",
            "CEBINV": "CEB",
            "CEPINV": "CEP",
            "CLKINV": "CLK",
            "PREG": "0",
            "PREG_CLKINVERSION": "0",
            "RSTAINV": "RSTA",
            "RSTBINV": "RSTB",
            "RSTPINV": "RSTP"
        })

        if clk is not None:
            if clk is True:
                clk = clock()
            wire(clk, self.inst.CLK)

        A, B = [], []
        for i in xrange(18):
            A += [self.inst.getpin("A%d" % i)]
            B += [self.inst.getpin("B%d" % i)]
        self.I = [[A], [B]]

        self.O = []
        for i in xrange(36):
            self.O += [self.inst.getpin("P%d" % i)]
