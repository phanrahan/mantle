import re
from magma import *
from ..kintex7 import PS7Wrap 
from loam import Peripheral

__all__ = ['PS7']


class PS7(Peripheral):
    def __init__(self, fpga):
        name = "PS7"
        Peripheral.__init__(self, fpga, name)

    def on(self):
        Peripheral.on(self)
        fpga = self.fpga
         
        #Read ps7_constraints file to config the GPIO with correct ucf info (and turn on)
        #Also save the pins in ps7pins
        fileName = os.path.dirname(__file__) + "/ps7_constraints.ucf"
        with open(fileName,'r') as constraints:
            lines = constraints.readlines()
        
        fpga.ps7pins = {}
        for line in lines:
            reobj = re.findall("NET\s+\"(\S+)\"\s+(.*);",line)
            if not reobj:
                continue
            reobj = reobj[0]
            name = reobj[0]
            opts = reobj[1].split(" | ")
            loc = None
            ucfopts = {}
            for opt in opts:
                opt = re.sub("\s+","",opt)
                optobj = re.findall("(.*)=\"?([^\"]*)\"?",opt)[0]
                if optobj[0]=="LOC":
                    loc = optobj[1]
                else:
                    ucfopts[optobj[0]] = optobj[1]
            assert(loc)
            loc = re.sub("\"","",loc)
            fpga.ps7pins[name] = pin = getattr(fpga,loc)
            pin.setucfopts(ucfopts)
            pin.rename(name).on()

        #for key, val in fpga.ps7pins.items():
        #    print(key, pin.direction)

        #Orient the iopads correctly by refrenceing the ps7Wrap circuit type
        def flipdir(port):
            if port.isinput():
                return OUTPUT
            elif port.isoutput():
                return INPUT
            else:
                return INOUT
        
        ps7 = PS7Wrap()
        for name in ps7.interface.ports:
            if not name in fpga.ps7pins:
                continue
            port = ps7.interface.ports[name]
            n = 0
            if isinstance(type(port),ArrayKind):
                n = len(port)
            if n:
                for i in range(n):
                    aname = "%s[%d]" % (name,i)
                    fpga.ps7pins[aname].reorient(flipdir(port))
            elif name in fpga.ps7pins: #TODO Hack to get around the clock
                fpga.ps7pins[name].reorient(flipdir(port))

        return self

    def setup(self, main):
        
        def wireit(port1,port2):
            if port1.isoutput():
                #print('wiring',port1,'to',port2)
                wire(port1,port2)
            else:
                #print('wiring',port2,'to',port1)
                wire(port2,port1)
        
        fpga = main.fpga

        #Instantiate ps7 circuit and wire up ports to fpga.ps7pins
        ps7inst = PS7Wrap()()
        for name in ps7inst.interface.ports:
            mainport = getattr(main, name, None)
            if not mainport:
                continue
            port = ps7inst.interface.ports[name]
            wireit(port, mainport)

        main.CLKIN = ps7inst.interface.ports['CLK']
        main.RST_n = ps7inst.interface.ports['RST_n']
        assert(main.CLKIN)
