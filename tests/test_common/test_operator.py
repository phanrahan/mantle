from magma import *
import os
os.environ["MANTLE"] = "lattice"
from magma.testing import check_files_equal
from mantle.common.operator import and_, nand, or_, nor, xor, nxor, invert, lsl, lsr, eq, add, sub, lt, le, gt, ge, neg
import operator
from mantle import And, Or, XOr, Add, Sub, EQ, ULT, ULE, UGT, UGE, SLT, SLE, SGT, SGE, Invert, Negate

def check(file_name):
    return check_files_equal(
        __file__,
        "build/{}".format(file_name),
        "gold/{}".format(file_name)
    )

def check_unary_operator(op, instance_op, wrapped=True):
    wrapped_suffix = ""
    if wrapped:
        wrapped_suffix = "_wrapped"
    name = 'check_unary_{}'.format(op.__name__)
    circ = DefineCircuit(name, "I", In(Bits(4)), "O", Out(Bits(4)))
    wire(op(circ.I), circ.O)
    EndDefine()
    assert repr(circ) == """\
{name} = DefineCircuit("{name}", "I", In(Bits(4)), "O", Out(Bits(4)))
inst0 = {instance_op}4{wrapped_suffix}()
wire({name}.I, inst0.I)
wire(inst0.O, {name}.O)
EndCircuit()\
""".format(name=name, instance_op=instance_op, wrapped_suffix=wrapped_suffix)

def check_unary_overloaded_operator(op, expected_instance, T=Bits, out_type=Bits(4)):
    name = 'check_unary_{}_overloaded_{}'.format(op.__name__, str(T(4)))
    circ = DefineCircuit(name, "I", In(T(4)), "O", Out(out_type))
    wire(op(circ.I), circ.O)
    EndDefine()
    assert repr(circ) == """\
{name} = DefineCircuit("{name}", "I", In({T}), "O", Out({out_type}))
inst0{expected_instance}
wire({name}.I, inst0.I)
wire(inst0.O, {name}.O)
EndCircuit()\
""".format(name=name, out_type=str(out_type), T=str(T(4)), expected_instance=repr(expected_instance))

def check_binary_operator(op, expected_instance, T=Bits, out_type=Bits(4)):
    name = 'check_binary_{}_{}'.format(op.__name__, str(T(4)))
    circ = DefineCircuit(name, "I0", In(T(4)), "I1", In(T(4)), "O", Out(out_type))
    wire(op(circ.I0, circ.I1), circ.O)
    EndDefine()
    assert repr(circ) == """\
{name} = DefineCircuit("{name}", "I0", In({T}), "I1", In({T}), "O", Out({out_type}))
inst0{expected_instance}
wire({name}.I0, inst0.I0)
wire({name}.I1, inst0.I1)
wire(inst0.O, {name}.O)
EndCircuit()\
""".format(name=name, out_type=str(out_type), T=str(T(4)), expected_instance=repr(expected_instance))

def check_binary_overloaded_operator(op, expected_instance, T=Bits, out_type=Bits(4)):
    name = 'check_binary_{}_overloaded_{}'.format(op.__name__, str(T(4)))
    circ = DefineCircuit(name, "I0", In(T(4)), "I1", In(T(4)), "O", Out(out_type))
    wire(op(circ.I0, circ.I1), circ.O)
    EndDefine()
    assert repr(circ) == """\
{name} = DefineCircuit("{name}", "I0", In({T}), "I1", In({T}), "O", Out({out_type}))
inst0{expected_instance}
wire({name}.I0, inst0.I0)
wire({name}.I1, inst0.I1)
wire(inst0.O, {name}.O)
EndCircuit()\
""".format(name=name, out_type=str(out_type), T=str(T(4)), expected_instance=repr(expected_instance))

def check_operator_three_args(op, instance_op):
    name = 'check_{}_three_args_{}'.format(op.__name__, str(T(4)))
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

def test_bitwise():
    check_unary_operator(invert, "Invert")
    check_unary_overloaded_operator(operator.invert, Invert(4))
    binary_bits_ops = [
        (and_, operator.and_, And(2, 4)),
        (or_ , operator.or_, Or(2, 4) ),
        (xor , operator.xor, XOr(2, 4)),
    ]
    for args in binary_bits_ops:
        print("Testing {}".format(args))
        check_binary_operator(args[0], args[2])
        check_binary_overloaded_operator(args[1], args[2])

    check_unary_operator(neg, "Negate", wrapped=False)
    check_unary_overloaded_operator(operator.neg, Negate(4), T=SInt)

    binary_arith_ops = [
        (add , operator.add, Add(4, cin=False)),
        (sub , operator.sub, Sub(4)),
    ]
    for args in binary_arith_ops:
        print("Testing {}".format(args))
        check_binary_operator(args[0], args[2], T=Bits)
        check_binary_overloaded_operator(args[1], args[2], T=UInt)
        check_binary_overloaded_operator(args[1], args[2], T=SInt)

    compare_ops = [
        # (eq, operator.eq, EQ(4) ),
        (lt, operator.lt, ULT(4), SLT(4)),
        (le, operator.le, ULE(4), SLE(4)),
        (gt, operator.gt, UGT(4), SGT(4)),
        (ge, operator.ge, UGE(4), SGE(4))
    ]
    for args in compare_ops:
        print("Testing {}".format(args))
        check_binary_operator(args[0], args[2], out_type=Bit)
        if args[0] == eq:
            check_binary_overloaded_operator(args[1], args[2], out_type=Bit)
        else:
            check_binary_overloaded_operator(args[1], args[2], T=UInt, out_type=Bit)
            check_binary_overloaded_operator(args[1], args[3], T=SInt, out_type=Bit)
