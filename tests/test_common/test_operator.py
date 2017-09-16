from magma import *
import os
os.environ["MANTLE"] = "lattice"
from magma.testing import check_files_equal
from mantle.common.operator import and_

def check(file_name):
    return check_files_equal(
        __file__,
        "build/{}".format(file_name),
        "gold/{}".format(file_name)
    )


def test_and_2():
    circ = DefineCircuit('main', "I0", In(Bits(4)), "I1", In(Bits(4)), "O",
            Out(Bits(4)))
    wire(and_(circ.I0, circ.I1), circ.O)
    EndDefine()
    compile("build/test_and_2", circ)
    print(repr(circ))
    assert repr(circ) == """\
main = DefineCircuit("main", "I0", In(Bits(4)), "I1", In(Bits(4)), "O", Out(Bits(4)))
inst0 = And2x4()
wire(main.I0, inst0.I0)
wire(main.I1, inst0.I1)
wire(inst0.O, main.O)
EndCircuit()\
"""

    assert check("test_and_2.v")


def test_and_3():
    circ = DefineCircuit('main', "I0", In(Bits(4)), "I1", In(Bits(4)), "I2",
            In(Bits(4)), "O", Out(Bits(4)))
    wire(and_(circ.I0, circ.I1, circ.I2), circ.O)
    EndDefine()
    compile("build/test_and_3", circ)
    print(repr(circ))
    assert repr(circ) == """\
main = DefineCircuit("main", "I0", In(Bits(4)), "I1", In(Bits(4)), "I2", In(Bits(4)), "O", Out(Bits(4)))
inst0 = And3x4()
wire(main.I0, inst0.I0)
wire(main.I1, inst0.I1)
wire(main.I2, inst0.I2)
wire(inst0.O, main.O)
EndCircuit()\
"""

    assert check("test_and_3.v")
