from magma import *
import os
os.environ["MANTLE"] = "lattice"
from magma.testing import check_files_equal
from mantle.common.operator import and_, nand, or_, nor, xor, nxor

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
    assert repr(circ) == """\
main = DefineCircuit("main", "I0", In(Bits(4)), "I1", In(Bits(4)), "O", Out(Bits(4)))
inst0 = And2x4()
wire(main.I0, inst0.I0)
wire(main.I1, inst0.I1)
wire(inst0.O, main.O)
EndCircuit()\
"""

    compile("build/test_and_2", circ)
    assert check("test_and_2.v")


def test_and_3():
    circ = DefineCircuit('main', "I0", In(Bits(4)), "I1", In(Bits(4)), "I2",
            In(Bits(4)), "O", Out(Bits(4)))
    wire(and_(circ.I0, circ.I1, circ.I2), circ.O)
    EndDefine()
    assert repr(circ) == """\
main = DefineCircuit("main", "I0", In(Bits(4)), "I1", In(Bits(4)), "I2", In(Bits(4)), "O", Out(Bits(4)))
inst0 = And3x4()
wire(main.I0, inst0.I0)
wire(main.I1, inst0.I1)
wire(main.I2, inst0.I2)
wire(inst0.O, main.O)
EndCircuit()\
"""

    compile("build/test_and_3", circ)
    assert check("test_and_3.v")

def check_binary_operator(op, instance_op):
    name = 'check_binary_{}'.format(op.__name__)
    circ = DefineCircuit(name, "I0", In(Bits(4)), "I1", In(Bits(4)), "O", Out(Bits(4)))
    wire(op(circ.I0, circ.I1), circ.O)
    EndDefine()
    assert repr(circ) == """\
{name} = DefineCircuit("{name}", "I0", In(Bits(4)), "I1", In(Bits(4)), "O", Out(Bits(4)))
inst0 = {instance_op}2x4()
wire({name}.I0, inst0.I0)
wire({name}.I1, inst0.I1)
wire(inst0.O, {name}.O)
EndCircuit()\
""".format(name=name, instance_op=instance_op)

def check_operator_three_args(op, instance_op):
    name = 'check_{}_three_args'.format(op.__name__)
    circ = DefineCircuit(name, "I0", In(Bits(4)), "I1", In(Bits(4)),  "I2", In(Bits(4)), "O", Out(Bits(4)))
    wire(op(circ.I0, circ.I1, circ.I2), circ.O)
    EndDefine()
    assert repr(circ) == """\
{name} = DefineCircuit("{name}", "I0", In(Bits(4)), "I1", In(Bits(4)), "I2", In(Bits(4)), "O", Out(Bits(4)))
inst0 = {instance_op}3x4()
wire({name}.I0, inst0.I0)
wire({name}.I1, inst0.I1)
wire({name}.I2, inst0.I2)
wire(inst0.O, {name}.O)
EndCircuit()\
""".format(name=name, instance_op=instance_op)

def test_nand():
    check_binary_operator(nand, "NAnd")
    check_operator_three_args(nand, "NAnd")

def test_or():
    check_binary_operator(or_, "Or")
    check_operator_three_args(or_, "Or")

def test_nor():
    check_binary_operator(nor, "NOr")
    check_operator_three_args(nor, "NOr")

def test_xor():
    check_binary_operator(xor, "XOr")
    check_operator_three_args(xor, "XOr")

def test_nxor():
    check_binary_operator(nxor, "NXOr")
    check_operator_three_args(nxor, "NXOr")
